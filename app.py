from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


def write_to_file(dict):
    with open("./database.txt", "a") as file_object:
        email = dict['email']
        subject = dict['subject']
        message = dict['message']
        file_object.write(f'\n {email},{subject},{message}')


def write_to_CSV(dict):
    with open("./database.csv", "a", newline='') as csvFile:
        email = dict['email']
        subject = dict['subject']
        message = dict['message']
        csvWriter = csv.writer(csvFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csvWriter.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_CSV(data)
            return redirect('/thankyou.html')
        except Exception as ex:
            print(ex)
            return 'Did not save to database  '
    else:
        return 'Something was wrong try again'

from flask import Flask
from flask import request
from flask import redirect
import smtplib
from dotenv import load_dotenv
import os

import requests


app = Flask(__name__)
@app.route('/', methods=['post', 'get'])
def index():
    if request.method == 'POST':
        form = request.form
        firstname = form.get('firstname')
        lastname = form.get('lastname')
        email = form.get('email')
        login = os.environ["LOGIN"]
        password = os.environ["PASSWORD"]
        server = smtplib.SMTP_SSL('smtp.yandex.ru:465')
        server.login(login, password)
        begin_letter=f'''From: {login}
To: {email}
Subject: Hi
Content-Type: text/plain; charset="UTF-8";
'''
        letter = f'{begin_letter} \nHi, {firstname} {lastname}'.encode('UTF-8')
        server.sendmail(login, email, letter)
        server.quit()
    ip = request.access_route[0]
    url = f"http://ip-api.com/json/{ip}"
    response = requests.get(url)
    response.raise_for_status()
    answer = response.json()
    if answer['status'] == 'success' and (answer['countryCode'] == 'RU' or answer['countryCode'] == 'KZ'):
       return redirect('/ru')
    else:
        with open('index.html', 'r') as file:
            return file.read()


@app.route('/ru')
def ru():
    with open('index2.html', 'r') as file:
        return file.read()
if __name__ == '__main__':
    load_dotenv()
    app.run(host='0.0.0.0', port='8000')
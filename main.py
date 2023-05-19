from flask import Flask
from flask import request
from flask import jsonify
from flask import redirect

import requests



app = Flask(__name__)
@app.route('/')
def index():
    ip = request.access_route[0]
    url = f"http://ip-api.com/json/{ip}"

    response = requests.get(url)
    response.raise_for_status()
    answer = response.json()
    if answer['status'] == 'success' and (answer['countryCode'] == 'RU' or answer['countryCode'] == 'KZ'):
        return redirect('/ru')
    else:
        return '<h1>Main</h1>'


@app.route('/ru')
def ru():
    return '<h1>Главная</h1>'
if __name__ == '__main__':
    app.run()
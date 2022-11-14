#try_flask


from flask import Flask
import json
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return 'nothing is here'

@app.route('/hello')
def hello():
    return '<h1>Hello, World</h1>'

@app.route('/date')
def datums():
    return (f'<h1>Today is {datetime.datetime.now()}</h1>')

@app.route('/lietotajs/<vards>/<vecums>')
def lietotajs(vards,vecums):
    # return f'<h1>{vards}, {vecums}</h1>'
    with open('data.json','w',encoding='UTF-8') as file:
        dict = {'vards': vards,
                'vecums': vecums}

        json.dumps(dict)

app.run(host='0.0.0.0',port=81)
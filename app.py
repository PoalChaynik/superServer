#try_flask


from flask import Flask
import json
import datetime
from flask_cors import CORS

app = Flask(__name__)
app.config["JSON_AS_ASCII"]=False
CORS(app)

@app.route('/')
def index():
    return 'nothing is here'

@app.route('/hello')
def hello():
    return '<h1>Hello, World</h1>'

@app.route('/send/<vards>/<zina>')
def send(vards,zina):
    now = datetime.datetime.now()
    time = now.strftime("%Y/%m/%d, %H:%M:%S")

    # print(vards,zina,time)

    rinda = {
        'zina':zina,
        'vards':vards,
        'laiks':time
    }

    with open('chat.json','r',encoding='utf-8') as fails:
        vecasZinas = fails.read()
        vecieJson = json.loads(vecasZinas)

    vecieJson.append(rinda)

    with open('chat.json','w',encoding='utf-8') as f:
        json.dump(vecieJson,f,indent=2,ensure_ascii=False)

    return 'ok'

@app.route('/date')
def datums():
    return (f'<h1>Today is {datetime.datetime.now()}</h1>')

@app.route('/read')
def read():
    with open('chat.json','r',encoding='utf-8') as r:
        msg = r.read()
    return msg


@app.route('/user/<vards>/<vecums>')
def lietotajs(vards,vecums):
    #return f"{vards} un {vecums}"
    dati = {vards:vecums}
    dati_json = json.dumps(dati)
    #return dati_json
    with open("lietotaji.json","w",encoding="utf-8") as fails:
        json.dump(dati_json,fails,indent=2,ensure_ascii=False)

app.run(host='0.0.0.0',port=81)
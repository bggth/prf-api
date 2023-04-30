#pip install flask
#pip install flask-cors

from flask import Flask
from flask_cors import CORS
from prf import read_office_by_id
import json

app = Flask(__name__)
CORS(app)

@app.route('/offices/<id>')
def office_id(id):
    result = {}
    result['result'] = read_office_by_id(id)
    return json.dumps(result, ensure_ascii=False).encode('utf8')

if __name__=='__main__':
	app.run()
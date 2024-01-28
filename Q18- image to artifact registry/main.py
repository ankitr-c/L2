from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == "__main__":
    context = ('cert.pem', 'key.pem')
    app.run(host='0.0.0.0', port=443, ssl_context=context,debug=True)
    #app.run(host='0.0.0.0',debug=True)
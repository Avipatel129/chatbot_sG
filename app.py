from flask import Flask,request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  

@app.route("/")
def home():
    return "Backend"


@app.route("/input", methods=['POST'])
def get_input():
    data = request.get_json()
    user_input = data['value']
    
    return {"name":"avinash"}

if __name__ == "__main__":
    app.run(debug = True , port = 5000)
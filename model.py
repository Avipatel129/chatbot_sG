from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd
import random 
from flask import Flask,request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  


data = pd.read_csv('Data/Training.csv')
question = pd.read_csv('Data/dataset.csv')

X = data.drop('prognosis', axis=1)
y = data['prognosis']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

question = question[question.applymap(lambda x: 'headache' in str(x)).any(axis=1)]
num,_ = question.shape

index = random.randrange(1,num)

question_list = question.iloc[index].tolist()
question_list = [item for item in question_list if pd.notna(item)]
question_list = [item.strip() for item in question_list]

column_names = X_test.columns.tolist()

input_data = [0] * 132

input_data = pd.DataFrame([input_data], columns=column_names)

DT = DecisionTreeClassifier()
DT.fit(X_train, y_train)

pred = DT.predict(input_data)

@app.route("/")
def home():
    return "Backend"

@app.route("/input", methods=['POST'])
def get_input():
    data = request.get_json()
    user_input = data['value']
    
    if user_input == "Hi Chatbot":
        for symptome in question_list:
            return {"question":"Do You Have {}".format(symptome)}
    

if __name__ == "__main__":
    app.run(debug = True , port = 5000)






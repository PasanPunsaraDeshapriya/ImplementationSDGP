from flask import Flask
from flask import render_template, request, redirect, url_for
from pymongo import *
import csv

app = Flask(__name__)

cluster = MongoClient("mongodb+srv://CS3:OS18@cluster0.a6pcbds.mongodb.net/?retryWrites=true&w=majority")
database = cluster["Sdgp_Test"]
collection = database["career"]
collection_Signup = database["signUp"]
# with open("Data_Files/Enterprising.csv", "r") as file:
#     reader = csv.reader(file)
#     header = next(reader)
#     for row in reader:
#         data = {}
#         for i in range(len(header)):
#             data[header[i]] = row[i]
#         collection.insert_one(data)

retreive = collection.find()
career_list = []
interest_code_list = []
for documents in retreive:
    career_list.append(documents)


@app.route('/')
@app.route('/home')
def home():
    return render_template('Oneth_homePage.html')

@app.route('/careerFinderModel')
def careerFinderModel():
    return render_template('Oneth_careerFinderModel.html')


@app.route('/programFinder')
def programFinder():
    return render_template('ProgramFinder.html')


@app.route('/universityFinder')
def universityFinder():
    return render_template('Oneth_universityFinder.html')

@app.route('/signup', methods=['GET'])
def signup_form():
    return render_template('Nirusan_SignUp.html')


@app.route('/signup', methods=['POST'])
def signup():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    user = {
        'name': name,
        'email': email,
        'password': password
    }
    collection_Signup.insert_one(user)
    return render_template("Nirusan_OptionPage.html")


@app.route('/login')
def login():
    return render_template('Nirusan_Login.html')


@app.route('/careerFinder', methods=['GET'])
def careerFinder():
    return render_template('CareerFinder.html')


@app.route("/my-python-endpoint", methods=["POST"])
def my_python_endpoint():
    data = request.get_json()
    print("Data received from JavaScript:", data)
    stringData = data.upper()
    print(stringData)
    for i in career_list:
        for values in i.values():
            if values == stringData:
                interest_code_list.append(i)

    for i in interest_code_list:
        print(i)
    return "success"

# Showing data to the web page
@app.route("/career")
def career():
    return render_template('Nirusan_CareerDisplay.html', interest_code_list= interest_code_list)

# 127.0.0.1 is the local machines IP address
# 5000 port is for TCP
if __name__ == "__main__":
    app.run(debug=True)

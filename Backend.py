from flask import Flask
from flask import render_template, request, redirect, url_for
from pymongo import *
import csv

app = Flask(__name__)

cluster = MongoClient("mongodb+srv://CS3:OS18@cluster0.a6pcbds.mongodb.net/?retryWrites=true&w=majority")
database = cluster["Sdgp_Test"]
collection = database["career"]
collection_Signup = database["signUp"]
collection_program = database["program"]
collection_university = database["university"]
# with open("Data_Files/Enterprising.csv", "r") as file:
#     reader = csv.reader(file)
#     header = next(reader)
#     for row in reader:
#         data = {}
#         for i in range(len(header)):
#             data[header[i]] = row[i]
#         collection.insert_one(data)

retrieve_career = collection.find()
retrieve_program = collection_program.find();
retrieve_university = collection_university.find();

career_list = []
program_list = []
university_list = []

interest_code_career = []
interest_code_program = []
interest_code_university = []

for documents in retrieve_career:
    career_list.append(documents)

for documents in retrieve_program:
    program_list.append(documents)

for documents in retrieve_university:
    university_list.append(documents)

@app.route('/')
@app.route('/home')
def home():
    return render_template('Oneth_homePage.html')

@app.route('/careerFinderModel')
def careerFinderModel():
    return render_template('Oneth_careerFinderModel.html')

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


@app.route('/login', methods = ['GET'])
def login():
    return render_template('Nirusan_Login.html')

@app.route('/login', methods = ['POST'])
def loginForm():
    # Get login data from form submission
    email = request.form['email']
    password = request.form['password']

    # Check if login data exists in MongoDB
    query = {"email": email, "password": password}
    document = collection_Signup.find_one(query)
    exists = document is not None
    
    if exists:
        print("Account already exits")
    else:
        print("Account not exits")

    return render_template("/Nirusan_OptionPage.html")

@app.route('/careerFinder', methods=['GET'])
def careerFinder():
    return render_template('CareerFinder.html')

@app.route('/programFinder', methods=['GET'])
def programFinder():
    return render_template('ProgramFinder.html')


@app.route("/my-python-endpoint", methods=["POST"])
def my_python_endpoint():
    data = request.get_json()
    print("Data received from JavaScript:", data)
    stringData = data.upper()
    print(stringData)
    for i in career_list:
        for values in i.values():
            if values == stringData:
                interest_code_career.append(i)

    for i in interest_code_career:
        print(i, " for career")
    return "success"

@app.route("/my-python-endpoint2", methods=["POST"])
def my_python_endpoint2():
    data = request.get_json()
    print("Data received from JavaScript:", data)
    stringData = data.upper()
    print(stringData)
    for i in program_list:
        for values in i.values():
            if values == stringData:
                interest_code_program.append(i)

    for i in interest_code_program:
        print(i, " for program")
    return "success"

# Showing data to the web page
@app.route("/career")
def career():
    return render_template('Nirusan_CareerDisplay.html', interest_code_career = interest_code_career)

# Showing data to the web page
@app.route("/program")
def program():
    return render_template('programShow.html', interest_code_program = interest_code_program)

# 127.0.0.1 is the local machines IP address
# 5000 port is for TCP
if __name__ == "__main__":
    app.run(debug=True)

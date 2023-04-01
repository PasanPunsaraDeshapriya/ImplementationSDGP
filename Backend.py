from flask import Flask
from flask import render_template
from pymongo import *
import csv

app = Flask(__name__)

cluster = MongoClient("mongodb+srv://CS3:OS18@cluster0.a6pcbds.mongodb.net/?retryWrites=true&w=majority")
database = cluster["Sdgp_Test"]
collection = database["career"]

with open("CSV_Files/Enterprising.csv", "r") as file:
    reader = csv.reader(file)
    header = next(reader)
    for row in reader:
        data = {}
        for i in range(len(header)):
            data[header[i]] = row[i]
        collection.insert_one(data)

retreive = collection.find()
career_list = []
for documents in retreive:
    career_list.append(documents)

# Showing data to the web page
@app.route("/")
def hello_world():
    return render_template('home.html', career_list = career_list )

@app.route("/about")
def about():
    return render_template('about.html', title="About")

# 127.0.0.1 is the local machines IP address
# 5000 port is for TCP


if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask,render_template,request
import pickle
import numpy as np
app = Flask(__name__)

model=pickle.load(open('my_model.pkl', 'rb'))
@app.route('/')
def hello_world():
    return render_template("careerFinderModel.html")

@app.route('/predict',methods=['POST','GET'])
def predict():
    init_features=[int(x) for x in request.form.values()]
    final = [np.array(init_features)]
    prediction = model.predict_proba(final)

    if prediction == ("in demand"):
        return render_template('careerFinderModel.html',pred="this career is in demand")
    else :
        return render_template('careerFinderModel.html',pred="this career is not in demand")


if __name__ == '  main  ':
    app.run(debug=True)

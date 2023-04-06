from flask import Flask,render_template,request
import pickle
import pandas as pd

from naiveBayesTest2 import tfidf


app = Flask(__name__)


model=pickle.load(open('my_model.pkl', 'rb'))
@app.route('/')
def hello_world():
    return render_template("careerFinderModel.html")

@app.route('/',methods=['POST','GET'])
def predict():
    # console.log('Received request:', req.method, req.url);
    # init_features=[int(x) for x in request.form.values()]
    # final = [np.array(init_features)]
    # prediction = model.predict_proba(final)
    #
    # # if prediction == ("in demand"):
    # #     return render_template('careerFinderModel.html',pred="this career is in demand")
    # # else :
    # #     return render_template('careerFinderModel.html',pred="this career is not in demand")
    #
    # return render_template('prediction.html', prediction="isk maybe is wors")

    with open('my_model.pkl', 'rb') as f:
        mod = pickle.load(f)
    path = 'dataset.csv'
    df = pd.read_csv(path)
    df = df.rename(columns={'career name': 'type of career', 'in demand for the next 10 years?': 'in demand'})
    df['in demand'] = df['in demand'].map({'yes': 'in demand', 'no': 'not in demand'})

    # # Get input text from user
    # input_text = request.json.get('text')


    # Make prediction

    # tfidf = TfidfVectorizer()
    # tfidf.fit_transform(df['text'])
    # text_features = tfidf.transform([init_features])
    # predictions = mod.predict(text_features)
    # final_prediction = np.array(predictions)
    # return final_prediction.tolist()
    # return render_template('prediction.html', prediction="isk maybe is wors")

    text = ['doctor']
    text_features = tfidf.transform (text)
    predictions = mod.predict (text_features)
    print(predictions)


# def post_input():
#     # Load model and data
#     with open('my_model.pkl', 'rb') as f:
#         mod = pickle.load(f)
#     path = 'dataset.csv'
#     df = pd.read_csv(path)
#     df = df.rename(columns={'career name': 'type of career', 'in demand for the next 10 years?': 'in demand'})
#     df['in demand'] = df['in demand'].map({'yes': 'in demand', 'no': 'not in demand'})
#
#     # # Get input text from user
#     # input_text = request.json.get('text')
#     init_features=[int(x) for x in request.form.values()]
#
#     # Make prediction
#     tfidf = TfidfVectorizer()
#     tfidf.fit_transform(df['text'])
#     text_features = tfidf.transform([init_features])
#     predictions = mod.predict(text_features)
#     final_prediction = np.array(predictions)
#     return final_prediction.tolist()
#     return render_template('prediction.html', prediction="isk maybe is wors")


if __name__ == '  main  ':
    app.run(debug=True)

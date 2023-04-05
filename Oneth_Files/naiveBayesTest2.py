import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report

path = 'dataset.csv'
df = pd.read_csv(path)
df.head()

df = df.drop(['career pathway'], axis=1)
print(df.head())

print('found %s datas'% len(df))

print(df['in demand for the next 10 years?'].value_counts())

df = df.rename(columns={'career name': 'type of career', 'in demand for the next 10 years?': 'in demand'})
print(df.head)
df['in demand'] = df['in demand'].map({'yes': 'in demand', 'no': 'not in demand'})
print(df.head)

df = df.groupby('in demand').head(200)

df_label = sns.countplot(x='in demand', data=df)
df_label.set_xticklabels(df['in demand'].unique())
plt.show()

print(df['in demand'].value_counts())

tfidf = TfidfVectorizer()
X = tfidf.fit_transform(df['type of career'])
y = df['in demand']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
clf_nb = MultinomialNB()
clf_nb.fit(X_train, y_train)

MultinomialNB()
pred_nb = clf_nb.predict(X_test)

# import pickle
# with open('my_model.pkl', 'wb') as f:
#      pickle.dump(clf_nb, f)
#
# f = open('my_model.pkl', 'rb')  # 'r' for reading; can be omitted
# mod = pickle.load(f)
#
# print(classification_report(y_test,pred_nb))
#
# text = ['doctor']
# text_features = tfidf.transform (text)
# predictions = mod.predict (text_features)
# print(predictions)

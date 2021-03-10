from flask import Flask, render_template, request
import pandas as pd
import re
import os
import joblib
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/second', methods=['POST'])
def second():
    if request.method == 'POST':
        c1 = request.form['age']
        c2 = request.form['sex']
        c3 = request.form['chest']
        c4 = request.form['bp']
        c5 = request.form['chol']
        c6 = request.form['fbs']
        c7 = request.form['ecg']
        c8 = request.form['heartRate']
        c9 = request.form['eia']
        c10 = request.form['depression']
        c11 = request.form['segment']
        c12 = request.form['color']
        c13 = request.form['thal']

        comment = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13]

        ds = pd.read_csv('heart.csv')

        X = ds.iloc[:, 1:-1]
        X.loc[len(X)] = comment
        X = X.values

        sc = StandardScaler()
        X = sc.fit_transform(X)

        model = joblib.load('model.pkl')
        pred = model.predict(X)[-1]

        print(pred)
        return render_template("result.html", prediction=pred, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5, c6=c6, c7=c7, c8=c8, c9=c9, c10=c10, c11=c11, c12=c12, c13=c13)


if __name__ == '__main__':
    app.run()

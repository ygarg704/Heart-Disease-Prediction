from flask import Flask, render_template, request
import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/predict', methods=['POST'])
def button():
    if request.method == 'POST':
        comment = request.json['data']
        comment = comment.split(",")
        comment = [float(i) for i in comment]
        print(comment)

        df = pd.read_csv('heart.csv')

        X = df.iloc[:, 1:-1]
        X.loc[len(X)] = comment
        X = X.values
        print(X[-1])

        sc = StandardScaler()
        X = sc.fit_transform(X)

        model = joblib.load('model.pkl')
        pred = model.predict(X)[-1]
        print(X[-1])

        if pred == 0:
            predicted = "Heart Disease is not Present"
        else:
            predicted = "Heart Disease is Present"

        preds = {
            "Prediction": predicted
        }

        print(preds)
        return preds

if __name__ == '__main__':
    app.run()


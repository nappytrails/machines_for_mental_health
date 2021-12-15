# import necessary libraries
from flask import Flask, render_template, request
import pickle

# create instance of Flask app
app = Flask(__name__)


# create route that renders index.html template
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/purpose")
def purpose():
    return render_template("purpose.html")

@app.route("/quiz")
def quiz():
    scaler = pickle.load(open("ML/scaler.sav", 'rb'))
    knn_model = pickle.load(open("ML/knn_model.sav", 'rb'))

    country = int(request.form["country"])
    employment = int(request.form["employment"])
    history = int(request.form["history"])
    remote = int(request.form["remote"])
    tech = int(request.form["tech"])
    age = int(request.form["age"])
    gender_input = request.form["gender"]
    if gender_input == "male":
        male = 1
        female = 0
        others = 0
    elif gender_input == "female":
        male = 0
        female = 1
        others = 0
    else:
        male = 0
        female = 0
        others = 1
    
    X = [[age, country, employment, history, remote, tech, female, male, others]]
    X_scaled = scaler.transform(X)

    prediction = knn_model.predict(X_scaled)[0][0]
    print(prediction)


    return render_template("quiz.html", predition=prediction)

if __name__ == "__main__":
    app.run(debug=True)
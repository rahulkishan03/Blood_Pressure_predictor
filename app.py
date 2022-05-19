from flask import Flask, request, render_template
import pandas as pd
import joblib

app = Flask(__name__)

@app.route('/', methods =["POST", "GET"])
def index():
    if request.method == "POST":
        
      age = request.form["age"]
      weight = request.form["weight"]
      
      obj = joblib.load("LR.pkl")
      x = pd.DataFrame([[age, weight]], columns=["Age", "Weight"])
     
      return  render_template("index.html" , pred = obj.predict(x)[0])
    else :
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)

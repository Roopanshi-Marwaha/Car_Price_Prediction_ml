from flask import Flask, render_template,request
import pandas as pd

app = Flask(__name__)
car=pd.read_csv("Cleaned Car.csv")


@app.route("/")
def index():
    companies=sorted(car['company'].unique())
    car_models = sorted(car['name'].unique())
    year = sorted(car['year'].unique(),reverse=True) #reverse mei sort
    fuel_type=car['fuel_type'].unique()
    return render_template("index.html",companies=companies,car_models=car_models,years=year,fuel_types=fuel_type)

@app.route('/predict',methods=['POST'])
def predict():

    return ""

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template, request
import pandas as pd
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open('LinearRegressionModel.pkl', 'rb'))
car = pd.read_csv("Cleaned Car.csv")


@app.route("/")
def index():
    companies = sorted(car['company'].unique())
    car_models = sorted(car['name'].unique())
    year = sorted(car['year'].unique(), reverse=True)  # reverse mei sort
    fuel_type = car['fuel_type'].unique()
    companies.insert(0, "Select Company")
    return render_template(
        "index.html",
        companies=companies,
        car_models=car_models,
        years=year,
        fuel_types=fuel_type
    )


@app.route('/predict', methods=['POST'])
def predict():
    company = request.form['company']
    car_model = request.form['car_model']
    year = int(request.form['year'])
    fuel_type = request.form['fuel_type']
    kms_driven = int(request.form['kilo_driven']) if request.form['kilo_driven'] else 0
    # as year and kms_driven ki value ati hai that is a string so convert into int

    print(company, car_model, year, fuel_type, kms_driven)
    input_df = pd.DataFrame(
        columns=['name', 'company', 'year', 'kms_driven', 'fuel_type'],
        data=[[car_model, company, year, kms_driven, fuel_type]]
    )

    prediction = model.predict(input_df)
    print(prediction)

    return str(np.round(prediction[0], 2))


if __name__ == "__main__":
    app.run(debug=True)
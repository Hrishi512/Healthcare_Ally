from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

sex_map = {'M': 0, 'F': 1}

# Load the trained model
model = joblib.load('models/model.joblib')

# Define a function to preprocess input data
def preprocess_data(data):
    data = pd.DataFrame([data])
    data['SEX'] = data['SEX'].map({'M': 0, 'F': 1})
    print(data)
    return data

@app.route('/', methods=['GET', 'POST'])

def index():
    therapy_suggestion = None
    therapy_suggestion_text = None
    if request.method == 'POST':
        # Process the form data here
        patient_data = {
            'HAEMATOCRIT': float(request.form['HAEMATOCRIT']),
            'HAEMOGLOBINS': float(request.form['HAEMOGLOBINS']),
            'ERYTHROCYTE': float(request.form['ERYTHROCYTE']),
            'LEUCOCYTE': float(request.form['LEUCOCYTE']),
            'THROMBOCYTE': float(request.form['THROMBOCYTE']),
            'MCH': float(request.form['MCH']),
            'MCHC': float(request.form['MCHC']),
            'MCV': float(request.form['MCV']),
            'AGE': int(request.form['AGE']),
            'SEX': request.form['SEX']
        }

        # Preprocess the data
        processed_data = preprocess_data(patient_data)

        # Make predictions using the model
        therapy_suggestion = model.predict(processed_data)

        if therapy_suggestion is not None:
            if therapy_suggestion == 1:
                therapy_suggestion_text = "Medical attention needed; kindly seek advice from a healthcare professional."
            elif therapy_suggestion == 0:
                therapy_suggestion_text = "No further treatment necessary. Enjoy your well-being."

    return render_template('index.html', therapy_suggestion=therapy_suggestion_text)

if __name__ == '__main__':
    app.run(debug=True)
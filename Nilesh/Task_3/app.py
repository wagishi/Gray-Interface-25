from flask import Flask, request, render_template
import joblib
import os
import pandas as pd

app = Flask(__name__)

MODEL_MAP = {
    'rf': 'models/rf_model_pipeline.pkl',
    'svm': 'models/svm_model_pipeline.pkl'
}


@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    selected_key = 'rf'  

    if request.method == 'POST':
        selected_key = request.form['model']
        model_path = MODEL_MAP.get(selected_key)

        if not model_path or not os.path.exists(model_path):
            result = "Model not found!"
            return render_template('index.html', result=result)

        model = joblib.load(model_path)

        input_data =  {
            'Age': int(request.form['Age']),
            'Sex': request.form['Sex'],
            'ChestPainType': request.form['ChestPainType'],
            'RestingBP': int(request.form['RestingBP']),
            'Cholesterol': int(request.form['Cholesterol']),
            'FastingBS': int(request.form['FastingBS']),
            'RestingECG': request.form['RestingECG'],
            'MaxHR': int(request.form['MaxHR']),
            'ExerciseAngina': request.form['ExerciseAngina'],
            'Oldpeak': float(request.form['Oldpeak']),
            'ST_Slope': request.form['ST_Slope']
        }

        
        input_df=pd.Series(input_data).to_frame().T

        prediction = model.predict(input_df)[0]
        result = '💔 Positive for Heart Disease' if prediction == 1 else '💓 No Heart Disease Detected'

    return render_template('index.html',
                           result=result,
                           selected_model=selected_key)

if __name__=="__main__":
    app.run(debug=True)
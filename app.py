from flask import Flask, request, render_template
import joblib
import numpy as np

app = Flask(__name__, static_folder='s')
model = joblib.load('iris_model.pkl')

iris_labels = ['setosa', 'versicolor', 'Virginica']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        features = [
            float(request.form['sepal_length']),
            float(request.form['sepal_width']),
            float(request.form['petal_length']),
            float(request.form['petal_width'])
        ]
        prediction_index = model.predict([features])[0]
        prediction = iris_labels[prediction_index]
        return render_template('index.html', prediction=prediction)
    except Exception as e:
        return render_template('index.html', prediction="Invalid input.")

if __name__ == '__main__':
    app.run(debug=True)


# 🌸 Iris Classifier Web App

An interactive web application built with **Flask** that predicts the species of an iris flower based on user-input features — **sepal length**, **sepal width**, **petal length**, and **petal width**.

<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/4/41/Iris_dataset_scatterplot.svg" width="450"/>
</p>

## 🔍 Overview

This project demonstrates a complete **end-to-end machine learning pipeline**:
- Data preprocessing and model training (Scikit-learn)
- Flask-based web app development
- User interface for real-time prediction

## 🚀 Features
- 💡 Predicts between **Setosa**, **Versicolor**, and **Virginica**
- ✅ Clean, simple HTML-based UI
- 🧠 Model trained using Logistic Regression (can be upgraded to SVM, RF, etc.)
- 📊 Displays prediction result on the same page

## 🧠 Model Info
- **Dataset**: [Iris Dataset](https://archive.ics.uci.edu/ml/datasets/Iris)
- **Model Used**: Logistic Regression (Scikit-learn)
- **Accuracy**: ~97% on test data

## 🛠️ Tech Stack
- **Python** 🐍
- **Flask** for backend
- **HTML/CSS** for frontend
- **Scikit-learn** for ML model

## 📦 Folder Structure
```
Iris-Classifier/
├── static/
│   └── style.css
├── templates/
│   └── index.html
├── model/
│   └── iris_model.pkl
├── app.py
├── requirements.txt
└── README.md
```

## 💻 How to Run Locally
```bash
# Clone the repo
git clone https://github.com/Alpha2027-beep/iris-classifier-app.git
cd iris-classifier-app

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py

## 📜 License
This project is under the [MIT License](LICENSE).




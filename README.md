# 💼 Machine Learning Salary Prediction REST API

A scalable RESTful API built with **Django REST Framework (DRF)** that serves a trained **Machine Learning** model to predict employee salaries based on years of experience and test scores.

---

## 📌 Features

- **Trained ML Model**: Serialized Linear Regression model (`salary_model.pkl`) trained on historical candidate evaluation metrics.
- **RESTful Architecture**: Clean, JSON-based POST endpoint built using Django REST Framework.
- **Fast Inference**: Lightweight model execution providing sub-second predictions.
- **Tested & Verified**: Validated via Postman Desktop Agent with standard HTTP status codes.

---

## 🛠️ Tech Stack

- **Framework**: Django, Django REST Framework (DRF)
- **Machine Learning**: Scikit-Learn, NumPy, Joblib / Pickle
- **Language**: Python 3
- **API Testing**: Postman

---

## 📂 Project Structure

```text
Salary-Prediction-REST-API/
├── ml_project/             # Django project configuration & settings
├── predictor/              # Core Django app containing API views & endpoints
│   ├── views.py            # API request handling & inference logic
│   └── urls.py             # Route configuration
├── manage.py               # Django execution script
├── train.py                # ML model training script
├── salary_model.pkl        # Serialized trained model artifact
└── .gitignore              # Ignored files (virtual environment, cache)


🚀 Getting Started
1. Clone the Repository

Follow these steps to set up and run the project locally on your machine.

1. Clone the Repository


git clone [https://github.com/KChavhan17/Salary-Prediction-REST-API.git](https://github.com/KChavhan17/Salary-Prediction-REST-API.git)
cd Salary-Prediction-REST-API


2. Create and Activate Virtual Environment
Windows:

python -m venv myenv
myenv\Scripts\activate


macOS / Linux:

python3 -m venv myenv
source myenv/bin/activate


3. Install Required Packages

pip install django djangorestframework scikit-learn numpy

4. Run Migrations and Start the Server

python manage.py migrate
python manage.py runserver

The server will start running locally at:

[http://127.0.0.1:8000/](http://127.0.0.1:8000/)

📡 API Endpoint Details


Predict Salary Endpoint


URL: http://127.0.0.1:8000/api/predict/


Method: POST


Header: Content-Type: application/json


Request Body
JSON

{
  "experience": 5,
  "test_score": 90
}

Response

{
  "predicted_salary": 74852.94
}

## 🧪 Postman Testing

| Method | Endpoint | Expected Status | Output |
| :--- | :--- | :--- | :--- |
| **POST** | `/api/predict/` | `200 OK` | `{"predicted_salary": 74852.94}` |

---

## 👩‍💻 Author

| Name | Role | Profile |
| :--- | :--- | :--- |
| **Keerti Chavhan** | Developer | [@KChavhan17](https://github.com/KChavhan17) |

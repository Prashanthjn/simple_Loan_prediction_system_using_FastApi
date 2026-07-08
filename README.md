# Loan Approval Prediction API Built with FastApi


A Machine Learning REST API built with **FastAPI** that predicts whether a loan application is approved based on user input.

## 📌 Features

- Train ML model using Scikit-learn
- Save trained model with Joblib
- REST API using FastAPI
- Predict loan approval
- Interactive API documentation with Swagger UI

## 🛠️ Tech Stack

- Python
- FastAPI
- Scikit-learn
- Pandas
- Joblib
- Uvicorn

## 📂 Project Structure

```
Loan_Approval_Prediction_API_Built_with_FastApi/
│── app_api.py
│── model_training.py
│── data.csv
│── loan_model.joblib
│── requirements.txt
│── .gitignore
```

## ▶️ Installation

Clone the repository:

```bash
git clone https://github.com/Prashanthjn/simple_Loan_prediction_system_using_FastApi.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the API:

```bash
uvicorn FastAPI:app --reload
```

Open in browser:

```
http://127.0.0.1:8000/docs
```

## 📸 API Endpoints

### GET /

Returns the API status.

### POST /predict

Example Request

```json
{
  "age": 25,
  "salary": 50000
}
```

Example Response

```json
{
  "prediction": "Loan Approved"
}
```

---

⭐ If you like this project, feel free to star the repository.



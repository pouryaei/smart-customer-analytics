---

title: Axiomeet Customer Analytics
emoji: 📈
colorFrom: blue
colorTo: purple
sdk: docker
app_port: 8501
pinned: false
---

Current Version: v1.0.0
Status: Production Demo

# Axiomeet Customer Analytics

ML-powered customer churn analytics platform built with Streamlit, Scikit-learn and Docker.

Features:

* Customer churn prediction
* Probability estimation
* Explainable output
* Streamlit dashboard
* Docker deployment


## Features

- Customer churn prediction
- Probability estimation
- Prediction explainability
- FastAPI inference service
- Streamlit dashboard
- MLflow model registry
- Drift detection
- Prediction monitoring
- Retraining trigger
- Docker deployment
- Hugging Face deployment
---

## Tech Stack

### Machine Learning
- Python
- Scikit-Learn
- MLflow

### Backend
- FastAPI

### Frontend
- Streamlit

### MLOps
- Docker
- Docker Compose
- Model Registry
- Monitoring

### Data
- Pandas
- NumPy

### Development
- Git
- Jupyter

### Machine Learning

* Python
* Scikit-Learn
* Logistic Regression

### Data Processing

* Pandas
* NumPy

### Deployment

* Streamlit
* Docker

### Development

* Git
* Jupyter Notebook

---

## System Architecture

```text
User
 ↓
Streamlit UI
 ↓
FastAPI
 ↓
Prediction Service
 ↓
MLflow Registry
 ↓
Monitoring
 ↓
Drift Detection
 ↓
Retraining Trigger
```

---

## MLOps Workflow

```text
Train
 ↓
Register
 ↓
Promote
 ↓
Serve
 ↓
Monitor
 ↓
Detect Drift
 ↓
Retrain
```


## Deployment

Environment support:

- Local development
- Docker Compose
- Hugging Face Spaces

Runtime automatically switches environment configuration.

## Project Structure

```text
app/
src/
artifacts/
data/
docs/
screenshots/
```

## Dataset

Dataset used:

Telco Customer Churn Dataset

Target:

* Churn

Selected Features:

* tenure
* MonthlyCharges
* TotalCharges
* Contract
* InternetService
* PaymentMethod
* Partner
* Dependents
* TechSupport
* OnlineSecurity

---

## Model Performance

| Metric    | Score |
| --------- | ----- |
| Accuracy  | 0.738 |
| Precision | 0.504 |
| Recall    | 0.786 |
| F1 Score  | 0.614 |

---

## Application Preview

### Dashboard

![Dashboard](screenshots/ui.png)

---

### Prediction Example

![Prediction](screenshots/prediction.png)

---

## Run Locally

Clone repository:

```bash
git clone <https://github.com/pouryaei/smart-customer-analytics>
```

Move into project:

```bash
cd smart-customer-analytics
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run application:

```bash
streamlit run app/streamlit/app.py
```

---

## Run With Docker

Build image:

```bash
docker build -t axiomeet-churn .
```

Run container:

```bash
docker run -p 8501:8501 axiomeet-churn
```

Open:

```text
http://localhost:8501
```

---

## Author

Pourya Einolghazaei

ML Engineer • Data Science • MLSecOps Enthusiast

Axiomeet

Email:
[axiomeet@gmail.com](mailto:axiomeet@gmail.com)

Website:
axiomeet.com (coming soon)

---

## License

MIT License

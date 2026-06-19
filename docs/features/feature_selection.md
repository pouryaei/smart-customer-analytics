# Final Selected Features

## Removed

- customerID → identifier
- AvgMonthlySpend → correlated with MonthlyCharges
- TenureGroup_loyal → correlated with tenure

## Final Dataset

Rows: 7043

Features: 15

Target: Churn

## Keep

gender
SeniorCitizen
Partner
Dependents
tenure
PhoneService
MultipleLines
InternetService
OnlineSecurity
OnlineBackup
DeviceProtection
TechSupport
StreamingTV
StreamingMovies
Contract
PaymentMethod
MonthlyCharges
TotalCharges
PaperlessBilling

## Review

None

## Drop

customerID
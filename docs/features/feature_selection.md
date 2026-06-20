## Final Selected Features

## Removed

- customerID → identifier only
- AvgMonthlySpend → highly correlated with MonthlyCharges
- TenureGroup_loyal → highly correlated with tenure
- MultipleLines_No phone service → redundant encoding
- No internet service derived columns → redundant information

---

## Final Dataset

Rows: 7043

Features: 15

Target:
Churn

---

## Final Features

- InternetService_Fiber optic
- PaymentMethod_Electronic check
- MonthlyCharges
- PaperlessBilling
- SeniorCitizen
- PaymentMethod_Credit card (automatic)
- Partner
- Dependents
- TechSupport_Yes
- OnlineSecurity_Yes
- Contract_One year
- TotalCharges
- InternetService_No
- Contract_Two year
- tenure

## Drop

customerID

# Model Selection Summary

Three baseline models were evaluated:

- Logistic Regression
- Decision Tree
- Random Forest

Decision Tree and Random Forest showed severe overfitting.

Logistic Regression achieved the most stable performance.

After hyperparameter tuning:

Parameters:
- C = 0.01
- class_weight = balanced
- penalty = l2

Final Metrics:
- Accuracy = 0.74
- Precision = 0.50
- Recall = 0.79
- F1 = 0.61

Final Decision:

Tuned Logistic Regression was selected because recall and F1 improved while maintaining good generalization.
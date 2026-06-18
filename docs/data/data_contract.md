# Data Contract

## Data Owner

Project Team

## Raw Data

Immutable

## Processed Data

Generated

## Target Column

Churn

## Storage Rules

raw → read only

processed → reproducible

## Dataset

telco_customer_churn.csv

## Data Source

Kaggle

## Data Quality Findings

### TotalCharges

Observed issue:
- Column stored as object

Root cause:
- 11 rows contained blank spaces

Business interpretation:
- Customers with tenure = 0 had no accumulated charges

Resolution:
- Replace blank values with 0
- Convert column to float64
# Bengaluru House Price Prediction

## Overview

This project predicts Bengaluru house prices using Machine Learning based on property features such as:

- Location
- Area Type
- Total Square Feet
- Number of Bathrooms
- Number of Balconies
- BHK

The model is deployed as an interactive Streamlit web application.

---

## Dataset

Bengaluru House Price Dataset

After preprocessing:

- Removed invalid records
- Removed location outliers
- Removed price per sqft outliers
- Performed feature engineering
- Applied One-Hot Encoding

Final dataset size:

- 6626 records
- 217 features

---

## Machine Learning Pipeline

### Data Cleaning

- Handled missing values
- Standardized locations
- Feature engineering

### Outlier Removal

- Sqft/BHK filtering
- Price per sqft filtering
- BHK anomaly detection

### Feature Encoding

- One Hot Encoding
- Location Encoding
- Area Type Encoding

### Model Training

Linear Regression

Performance:

- MAE = 16.35
- RMSE = 27.06
- R² Score = 0.86

---

## Tech Stack

- Python
- Pandas
- NumPy
- Scikit-Learn
- Streamlit

---

## Live Demo

https://disha-house-price-predictor.streamlit.app

---

## Repository

https://github.com/Dishagoyal592/OutriX_project

---

## Author

Disha Goyal
B.E. Robotics & AI Engineering

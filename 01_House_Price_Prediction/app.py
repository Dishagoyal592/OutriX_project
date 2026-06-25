
import streamlit as st
import numpy as np
import pickle
import json

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(BASE_DIR, "house_price_model.pkl"), "rb") as f:
    model = pickle.load(f)

with open(os.path.join(BASE_DIR, "columns.json"), "r") as f:
    data = json.load(f)

columns = data["data_columns"]

st.set_page_config(page_title="Real Estate Price Intelligence", layout="centered")

st.title("🏠 Real Estate Price Intelligence System")
st.write("Predict Bengaluru house prices using a Machine Learning model.")

locations = sorted([
    col.replace("location_", "")
    for col in columns
    if col.startswith("location_")
])

area_type_columns = [
    col for col in columns
    if col.startswith("area_type_")
]

area_types = sorted([
    col.replace("area_type_", "")
    for col in area_type_columns
])

location = st.selectbox("Select Location", locations)
area_type = st.selectbox("Select Area Type", area_types)

sqft = st.number_input("Enter Total Square Feet", min_value=300.0, max_value=10000.0, value=1200.0)
bath = st.number_input("Enter Number of Bathrooms", min_value=1, max_value=10, value=2)
balcony = st.number_input("Enter Number of Balconies", min_value=0, max_value=5, value=1)
bhk = st.number_input("Enter BHK", min_value=1, max_value=10, value=2)

def predict_price(location, area_type, sqft, bath, balcony, bhk):
    x = np.zeros(len(columns))

    x[columns.index("total_sqft")] = sqft
    x[columns.index("bath")] = bath
    x[columns.index("balcony")] = balcony
    x[columns.index("bhk")] = bhk

    loc_col = "location_" + location
    area_col = "area_type_" + area_type

    if loc_col in columns:
        x[columns.index(loc_col)] = 1

    if area_col in columns:
        x[columns.index(area_col)] = 1

    return model.predict([x])[0]

if st.button("Predict Price"):
    predicted_price = predict_price(location, area_type, sqft, bath, balcony, bhk)

    st.success(f"Estimated House Price: ₹ {predicted_price:.2f} Lakhs")
    st.write(f"Approximate value: ₹ {predicted_price/100:.2f} Crores")

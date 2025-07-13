import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("BMI Calculator")

# Inputs
st.subheader("Enter your details:")
height = st.slider("Height (in cm)", 100, 220, 170)
weight = st.slider("Weight (in kg)", 30, 150, 70)

# BMI Calculation
height_m = height / 100
bmi = round(weight / (height_m ** 2), 2)

st.write(f"**Your BMI is:** `{bmi}`")

# Classification
if bmi < 18.5:
    status = "Underweight"
elif 18.5 <= bmi < 25:
    status = "Normal weight"
elif 25 <= bmi < 30:
    status = "Overweight"
else:
    status = "Obese"

st.success(f"You are categorized as: **{status}**")

# Visualization
st.subheader("BMI Category Ranges")
categories = ["Underweight", "Normal", "Overweight", "Obese"]
bmi_ranges = [18.5, 25, 30, 40]

fig, ax = plt.subplots()
ax.bar(categories, bmi_ranges, color=['blue', 'green', 'orange', 'red'])
ax.axhline(bmi, color='black', linewidth=2, linestyle='--', label="Your BMI")
ax.set_ylabel("BMI Value")
ax.legend()

st.pyplot(fig)

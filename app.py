import streamlit as st

st.title("Nathaniel Salvoro")
st.caption("I am Nathaniel Salvoro, and I'm a fourth-year college student studying Bachelor of Science in Information Technology. After I graduate, I want to become a successful Web Developer.")
st.divider()

st.header("BMI Calculator")
st.caption("a simple app I made")


height = st.slider("Enter your height", 0, 250, 175)
weight = st.slider("Enter your weight", 0, 500, 70)

bmi = weight / ((height/100) ** 2)

st.write(f"BMI: {bmi:.2f}")
st.divider()
st.write("### CLASSIFICATION ###")
st.write("Underweight: less than 18.5")
st.write("Normal: 18.5 - 24.9")
st.write("Overweight: 25 - 29.9")
st.write("Obese: 30+")

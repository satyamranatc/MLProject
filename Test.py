import streamlit as st

st.title("Hello Welcome")


# DropDownList
Choice = st.selectbox("Choose a Purpose:", ["HeartAttack", "Dibatees", "Parkisons", "Other"])


if Choice == "HeartAttack":
    st.subheader("Heart Attack")
    st.write("This is a Heart Attack")
    import pandas as pd
    import joblib

    # Load the trained model
    Model = joblib.load("./HearAttack/MyModel")

    # Title of the app
    st.title("Heart Disease Input Form")

    # Input fields
    age = st.number_input("Enter value for age:", min_value=0, max_value=120, value=25)
    sex = st.radio("Enter value for sex:", options=[1, 0], format_func=lambda x: 'Male' if x == 1 else 'Female')
    cp = st.number_input("Enter value for cp (chest pain type):", min_value=0, max_value=3, value=0)
    trestbps = st.number_input("Enter value for trestbps (resting blood pressure in mm Hg):", min_value=0, value=120)
    chol = st.number_input("Enter value for chol (serum cholesterol in mg/dl):", min_value=0, value=200)
    fbs = st.radio("Enter value for fbs (fasting blood sugar > 120 mg/dl):", options=[1, 0], format_func=lambda x: 'True' if x == 1 else 'False')
    restecg = st.number_input("Enter value for restecg (resting electrocardiographic results):", min_value=0, max_value=2, value=0)
    thalach = st.number_input("Enter value for thalach (maximum heart rate achieved):", min_value=0, value=150)
    exang = st.radio("Enter value for exang (exercise induced angina):", options=[1, 0], format_func=lambda x: 'Yes' if x == 1 else 'No')
    oldpeak = st.number_input("Enter value for oldpeak (ST depression induced by exercise relative to rest):", min_value=0.0, value=1.0, step=0.1, format="%.1f")
    slope = st.number_input("Enter value for slope (the slope of the peak exercise ST segment):", min_value=0, max_value=2, value=0)
    ca = st.number_input("Enter value for ca (number of major vessels (0-3) colored by fluoroscopy):", min_value=0, max_value=3, value=0)
    thal = st.number_input("Enter value for thal (thalassemia):", min_value=0, max_value=3, value=0)


    # Button to submit the form
    if st.button("Submit"):
        Result = Model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

        # Interpret and print the result
        if Result == 0:
            st.write("You Are Safe")
        else:
            st.write("Kabhi Alvida Na Kehna")



elif Choice == "Dibatees":
        st.subheader("Dibatees")
        st.write("This is a Dibatees")


elif Choice == "Parkisons":

    st.subheader("Parkisons")

    st.write("This is a Parkisons")
    

elif Choice == "Other":

    st.subheader("Other")

    st.write("This is a Other")
    

else:

    st.subheader("Other")

    st.write("This is a Other")
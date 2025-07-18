import streamlit as st
import pandas as pd
import numpy as np

# --- App Title and Description ---
st.title("My First Streamlit App")
st.write("This is a simple app to demonstrate the functionalities of streamlit.")
         
# --- Interactive idgets in the Sidebar ---
st.sidebar.header("User Input Features") 

# Text Input
user_name = st.sidebar.text_input("what is your name?","GANDI BHARANIKA")

# slider
age = st.sidebar.slider("Select your age", 0,100,25)

# Selectbox
favorite_color = st.sidebar.selectbox("what is your favourite color?",["Blue", "Red", "Green", "Yellow"])
  
  # --- main page content
st.header(f"welcome, {user_name}!")
st.write(f"you are {age} years old and favorite color is {favorite_color}.")

# --- Displaying DataFrame ---
st.subheader("Here's some random data:")

# create a sample DataFrame
data = pd.DataFrame(
    np.random.randn(10,5),
   columns=('col %d' % i for i in range(5))
  )

st.dataframe(data)

# --- checkbox to show/hide content ---
if st.checkbox("Show raw data"):
     st.subheader("Raw Data")
     st.write(data)
     
    # --- Button to trigger an action ---
if st.button("Say hello"):
       st.write("Hello there")
       
else:
        st.write("Goodbye")
        
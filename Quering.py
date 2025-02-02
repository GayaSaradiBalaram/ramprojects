
import pandas as pd
import streamlit as st


from pandasai import Agent

import os

os.environ["PANDASAI_API_KEY"] = "$2a$10$alGxZdqFpTTQbq9qTDTG8OkrUQ7Fjm4ArYX3FIPDfIe1ctfHUEEgO"

#llm = OpenAI(api_token=os.environ["PANDASAI_API_KEY"])

st.title("Query the data")
def load_data():
    data = pd.read_csv("data_sample/sample.csv")

    return data

# Load the data
df= load_data()

# Select the data frame to analyze
data_choice = st.selectbox('Select the data frame to analyze', ['Original Data', 'Transformed Data'])

# Set the selected data frame
if data_choice == 'Original Data':
    df = df


agent = Agent(df)
st.write(df.head(3))

prompt = st.text_area("Enter the question")

if st.button("Generate"):
    if prompt:
        st.write("Generating the response")
        response = agent.chat(prompt)
        st.write(response)
    else:
        st.warning("Please enter the prompt")

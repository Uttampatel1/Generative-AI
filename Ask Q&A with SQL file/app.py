from dotenv import load_dotenv
load_dotenv() ## load all the environment variables

import streamlit as st
import os
import sqlite3
import pandas as pd

import google.generativeai as genai

## Configure Genai Key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function To Load Google Gemini Model and provide queries as response
def get_gemini_response(question, prompt):
    try:
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content([prompt[0], question])
        return response.text
    except Exception as e:
        st.error(f"Error generating response: {e}")
        return None

def read_sql_query(sql, db):
    try:
        conn = sqlite3.connect(db)
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        conn.commit()
        conn.close()
        return rows
    except Exception as e:
        st.error(f"Error executing SQL query: {e}")
        return None

## Define Your Prompt
prompt = [
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name STUDENT_NEW and has the following columns - NAME, Department, 
    Grade, Marks \n\nFor example,\nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENT_NEW ;
    \nExample 2 - Tell me all the students studying in Data Science class?, 
    the SQL command will be something like this SELECT * FROM STUDENT_NEW 
    where Department="Data Science"; 
    also the SQL code should not have ``` in the beginning or end and SQL word in output
    """
]

## Streamlit App
st.set_page_config(page_title="Gemini SQL App", page_icon="✨")

# Header
st.title("🔮 Gemini App To Retrieve SQL Data")
st.write("Ask any question about the STUDENT_NEW database!")

# Input and Button
question = st.text_input("Input: ", key="input")
submit = st.button("Ask the question 🚀")

# if submit is clicked
if submit:
    response = get_gemini_response(question, prompt)
    if response is not None:
        st.success("Query: " + response)
        # Fetch data from SQLite database
        data = read_sql_query(response, "test.db")

        if data is not None:
            # Display Response
            st.subheader("The Response is:")
            
            # Display response in a DataFrame for better tabular representation
            df = pd.DataFrame(data, columns=[f"Column {i+1}" for i in range(len(data[0]))])
            st.dataframe(df)

            # Optionally, you can add some styling to the DataFrame
            st.markdown(f"Total Rows: {len(data)}")




## Define Your Prompt
# prompt=[
#     """
#     You are an expert in converting English questions to SQL query!
#     The SQL database has the name STUDENT and has the following columns - NAME, CLASS, 
#     SECTION \n\nFor example,\nExample 1 - How many entries of records are present?, 
#     the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;
#     \nExample 2 - Tell me all the students studying in Data Science class?, 
#     the SQL command will be something like this SELECT * FROM STUDENT 
#     where CLASS="Data Science"; 
#     also the sql code should not have ``` in beginning or end and sql word in output
#     """
# ]

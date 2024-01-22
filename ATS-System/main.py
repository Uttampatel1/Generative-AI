import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv
import json

# Load environment variables
load_dotenv()

# Configure generative AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to get Gemini response
def get_gemini_response(input):
    try:
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(input)
        return response.text
    except Exception as e:
        st.error(f"An error occurred while generating content: {str(e)}")
        return None

# Function to extract text from PDF
def input_pdf_text(uploaded_file):
    try:
        reader = pdf.PdfReader(uploaded_file)
        text = ""
        for page in range(len(reader.pages)):
            page = reader.pages[page]
            text += str(page.extract_text())
        return text
    except Exception as e:
        st.error(f"An error occurred while extracting text from PDF: {str(e)}")
        return None

# Prompt Template
input_prompt = """
Hey! Act like a skilled or very experienced ATS (Application Tracking System)
with a deep understanding of the tech field, software engineering, data science, data analysis,
and big data engineering. Your task is to evaluate the resume based on the given job description.
Consider the job market is very competitive and provide the best assistance for improving the resumes.
Assign the percentage matching based on JD and the missing keywords with high accuracy.
Resume: {text}
Description: {jd}

I want the response in one single string having the structure
{{"JD Match": "%", "Missing Keywords": [], "Profile Summary": ""}}
"""
f = '''
/* Style for the title */
.title {
    color: #3498db;
    font-size: 2em;
    margin-bottom: 20px;
}

/* Style for the headers */
.section-header {
    color: #2ecc71;
    font-size: 1.5em;
    margin-top: 20px;
    margin-bottom: 10px;
}

/* Style for the text area */
.st-ae{
    width: 100%;
    height: 150px;
    padding: 10px;
    border: 1px solid #ee2222;
    border-radius: 5px;
    margin-bottom: 20px;
}

/* Style for the file uploader */
.st-emotion-cache-1erivf3 {
    color: #e74c3c;
    background-color: #ecf0f1;
    padding: 10px;
    border: 2px dashed #bdc3c7;
    border-radius: 5px;
    margin-bottom: 20px;
}

/* Style for the submit button */
.st-emotion-cache-19rxjzo.ef3psqc12 {
    background-color: #2ecc71;
    color: #fff;
    padding: 10px 20px;
    font-size: 1.2em;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

/* Style for the success message */
.success-message {
    color: #27ae60;
    font-weight: bold;
    margin-top: 10px;
}

/* Style for the warning message */
.warning-message {
    color: #e67e22;
    font-weight: bold;
    margin-top: 10px;
}

/* Style for the info message */
.info-message {
    color: #3498db;
    font-weight: bold;
    margin-top: 10px;
}

/* Style for the error message */
.error-message {
    color: #e74c3c;
    font-weight: bold;
    margin-top: 10px;
}
'''

st.markdown(f"<style>{f}</style>",unsafe_allow_html=True)

# Streamlit app
st.title("🚀 Smart ATS")
st.markdown("<div class='title'>Improve Your Resume with Smart ATS</div>", unsafe_allow_html=True)

# Job Description input
jd = st.text_area("Paste the Job Description 📄", key='jd')

# Resume upload
uploaded_file = st.file_uploader("Upload Your Resume 📂", type="pdf", help="Please upload the PDF", key='resume')

# Submit button
submit = st.button("Submit 👍", key='submit')

# Display results
if submit:
    # Display success message
    st.markdown("<div class='success-message'>Submission successful!</div>", unsafe_allow_html=True)
    
    if jd and uploaded_file:
        text = input_pdf_text(uploaded_file)
        if text is not None:
            response = get_gemini_response(input_prompt.format(text=text, jd=jd))
            if response is not None:
                response_dict = json.loads(response)

                # Styled result display
                st.markdown("<div class='section-header'>📋 ATS Evaluation Result:</div>", unsafe_allow_html=True)

                # Display JD Match
                st.markdown(f"<div class='success-message'>🔍 <strong>JD Match:</strong> {response_dict.get('JD Match', 'N/A')}</div>", unsafe_allow_html=True)

                # Display Missing Keywords
                missing_keywords = response_dict.get('Missing Keywords', [])
                # st.warning(f"❌ **Missing Keywords:** {', '.join(missing_keywords) if missing_keywords else 'None'}")
                
                st.markdown(f"<div class='warning-message'>❌ <b> Missing Keywords</b> : {', '.join(missing_keywords) if missing_keywords else 'None'}</div>", unsafe_allow_html=True)

                # Display Profile Summary
                profile_summary = response_dict.get('Profile Summary', '')
                st.info(f"📄 **Profile Summary:** {profile_summary if profile_summary else 'Not provided'}")
            

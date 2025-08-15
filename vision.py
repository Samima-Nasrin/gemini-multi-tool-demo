from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

## function to load Gemini Pro Model and get response
model=genai.GenerativeModel('gemini-2.5-flash')
def get_gemini_response(input,image):
    if input!='':
        response=model.generate_content([input,image])
    else:
        response=model.generate_content(image)
    return response.text

## initialize streamlit app
st.set_page_config(page_title='Image Demo')
st.header('Gemini Application')
input=st.text_input('Input Promt: ',key='input')

uploaded_file=st.file_uploader('Upload Image', type=['jpg','jpeg','png'])
image=''
if uploaded_file is not None:
    image=Image.open(uploaded_file)
    st.image(image,caption='Uploaded Image')

submit=st.button('Tell me about the image')

## when submit is called
if submit:
    response=get_gemini_response(input,image)
    st.subheader('The response is')
    st.write(response)

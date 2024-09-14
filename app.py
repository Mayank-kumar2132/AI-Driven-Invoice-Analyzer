from dotenv import load_dotenv

load_dotenv() # this will get everything form the .env file

import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

genai.configure(api_key = os.getenv("API_KEY"))
# print(os.getenv("API_KEY"))

model = genai.GenerativeModel('gemini-pro-vision')

def get_gemini_response(input, image, prompt):
    response = model.generate_content([input, image[0], prompt])
    return response.text

def input_image_details(uploaded_file):
    if uploaded_file is not None :
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                'mime_type': uploaded_file.type,
                'data': bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError('No File Uploaded')

st.set_page_config(page_title = "Multi Lingual Invoice Extractor")

st.header('Gemini Application')
input = st.text_input('Input Promt :', key = 'input')
uploaded_file = st.file_uploader('Choose an Image :', type = ['jpg','jpeg','png',])

image = ''
if uploaded_file is not None :
    image = Image.open(uploaded_file)
    st.image(image, caption = 'Uploaded Image', use_column_width = True)
submit = st.button('Tell me about the invoice')


input_prompt="""
Your are an expert in understanding invoices.
 We will upload a image as invoice and you will have to answer any
 question based onthe uploaded invoice image

"""

if submit :
    image_data = input_image_details(uploaded_file)
    response = get_gemini_response(input_prompt, image_data, input)
    st.subheader("The Response is ")
    st.write(response)
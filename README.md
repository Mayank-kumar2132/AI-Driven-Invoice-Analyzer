# AI-Driven-Invoice-Analyzer
### Project Overview
This project, Multi-Lingual Invoice Extractor, utilizes Google Generative AI (Gemini) to extract and analyze data from invoice images. The project allows users to upload an invoice image in various formats (JPG, JPEG, PNG) and then ask specific questions about the content of the invoice. The system uses Google’s Gemini AI to interpret the invoice data and provide responses in a streamlined manner. The project is built using Streamlit for the frontend interface, enabling a user-friendly and interactive experience.

### Features
Invoice Image Upload: Users can upload invoice images in JPG, JPEG, or PNG formats.
AI-Powered Invoice Interpretation: Leveraging Google Gemini AI to process and extract meaningful insights from the uploaded invoices.
Multi-Lingual Support: Capable of handling invoices in different languages.
Real-Time Interaction: Users can ask questions about the uploaded invoice and receive AI-generated responses in real time.
Streamlit Web App: The project is presented via a simple, interactive web interface.
### Technologies Used
Python: Core language for building the backend.
Streamlit: Used for creating the user interface and handling file uploads.
Google Generative AI (Gemini): The AI model used for processing and generating responses related to invoice content.
Pillow (PIL): For image handling and processing.
Python-dotenv: For securely loading environment variables (such as the API key).
langchain: For integrating language models and processing language-based queries.
PyPDF2: Additional library for potential PDF invoice processing.
chromadb: Used for managing embeddings and document storage in future extensions.
### Installation
Clone the repository:
Navigate to the project directory:

Install the required dependencies:

pip install -r requirements.txt
Create a .env file and add your Google Generative AI API key:
makefile
API_KEY=your_google_api_key_here
Run the Streamlit app:
streamlit run app.py
### How to Use
Upload an invoice image in JPG, JPEG, or PNG format.
Input a question or prompt regarding the invoice (e.g., "What is the total amount due?").
Submit your query and let the AI respond with insights derived from the invoice.
### Suggested Improvements
Add support for PDF invoices using PyPDF2.
Expand the AI model’s capability to handle a wider range of invoice formats and languages.
Enhance the UI for a more intuitive user experience.
Add OCR (Optical Character Recognition) for more accurate text extraction from the images.

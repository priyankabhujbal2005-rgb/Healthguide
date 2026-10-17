# HealthGuide – AI Health Information Agent

## About the Project
HealthGuide is a Python-based web application that provides general health information through a chatbot and a guided symptom checker. It is designed for educational purposes and helps users find basic health information from trusted references.

## Features
- **Health FAQ Chatbot:** Answers common health questions using a local FAQ knowledge base.
- **Trusted References:** Provides links to health information from sources such as WHO and NHS.
- **Guided Symptom Checker:** Collects selected symptoms, duration, and severity to display general guidance.
- **Emergency Alerts:** Recognizes selected emergency-related keywords and advises users to seek immediate help.
- **Interactive Web Interface:** Built with Streamlit.

## Technologies Used
- Python
- Streamlit
- Pandas
- Scikit-learn
- TF-IDF and cosine similarity
- CSV for the health FAQ knowledge base

## Project Structure
```text
HealthGuide/
├── app.py
├── chatbot.py
├── symptom_checker.py
├── requirements.txt
├── README.md
└── data/
    └── health_faq.csv
```

## Installation and Setup
1. Install Python.
2. Open a terminal in the project directory.
3. Create and activate a virtual environment if desired.
4. Install the dependencies:

   `pip install -r requirements.txt`

5. Start the application:

   `streamlit run app.py`

6. Open the local URL displayed in the terminal.

## Safety Disclaimer
HealthGuide provides general health education only. It does not diagnose diseases, prescribe medicines, or replace a qualified healthcare professional. In an emergency, contact local emergency services immediately.

## Project Purpose
This project demonstrates a simple information-retrieval chatbot, a guided symptom checker, and a web interface using Python and Streamlit.
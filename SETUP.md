# Restaurant AI App - Setup Guide

## Prerequisites
- Python 3.13
- GROQ API Key (get one at https://console.groq.com)

## Installation

1. **Install dependencies:**
   ```powershell
   pip install -r requirements.txt
   ```

2. **Set your GROQ API Key:**
   ```powershell
   $env:GROQ_API_KEY='your-actual-groq-api-key-here'
   ```

3. **Run the app:**
   ```powershell
   streamlit run app.py
   ```
   
   Or use the launcher script:
   ```powershell
   .\run.ps1
   ```

## Troubleshooting

### NumPy Warnings on Windows
The warnings about "NumPy built with MINGW-W64" are expected on Windows Python 3.13 and can be safely ignored. The app will work despite these warnings.

### GROQ_API_KEY Error
If you see "GROQ_API_KEY not found", make sure to set your API key in the environment before running the app.

### Exit Code 1
This typically means either:
- GROQ_API_KEY is not set in the environment
- You're using `python app.py` instead of `streamlit run app.py`

Use the correct command: `streamlit run app.py`

# cs217-assignment1

This is a repository for a simple note-taking project:

- **notes.py**: The core note-taking class.
- **api.py**: A FastAPI interface.
- **app.py**: A Flask “mini website.”
- **stream.py**: A Streamlit application.

## Setup

```bash
# Create and activate a virtual environment (optional but recommended)


# Install dependencies
pip install -r requirements.txt

# Run the FastAPI API
uvicorn api:app --reload

# In a separate shell, run the Flask app
python app.py

# In another separate shell, run the Streamlit app
streamlit run stream.py

# COSI-217 Assignment1 - Notebook App
### Galileo Steinberg

This repository contains a simple note-taking application with three different web interfaces:

1. **FastAPI** – Provides an HTTP API for listing, searching, fetching, and adding notes.
2. **Flask** – A mini website to browse, search, and add notes.
3. **Streamlit** – An interactive UI to accomplish the same note-taking tasks.

### Files
- `notes.py` – Core note-taking code (create, list, find, get note content).
- `api.py` – FastAPI server with GET/POST endpoints.
- `app.py` – Flask mini-website with two pages (main + note detail).
- `stream.py` – Streamlit application with tabs to view/add notes.
- `requirements.txt` – Python dependencies.
- `README.md` – This guide.
- `templates/` – HTML templates
- `static/` – A small CSS file
- `data/` – Directory where the notes are stored as `<name>.txt`.

### Dependencies

All required dependencies are listed in `requirements.txt`. They include:

- `fastapi`
- `uvicorn`
- `flask`
- `streamlit`

These can be installed with `pip install -r requirements.txt`.





### Running the app



```bash
# Install dependencies
pip install -r requirements.txt

# Run the FastAPI API
uvicorn api:app --reload

# Run the Flask app
python app.py

# Run the Streamlit app
streamlit run stream.py

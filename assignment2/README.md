# NoteBook Application - Assignment 2

This is a simple note-taking web application built with Flask and SQLAlchemy for COSI-217.

## Features

- Create, view, and delete notes
- Add comments to notes
- Search through notes and comments
- Timestamps for all notes and comments
- SQLite database backend using SQLAlchemy

## Requirements

- Python
- Flask
- Flask-SQLAlchemy

All required dependencies are listed in `requirements.txt`.

## Installation

1. Clone the repository
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

Simply run:
```bash

python run.py
```

This will start the Flask development server, and the application will be accessible at `http://127.0.0.1:5000/`.
Once the application has started, the instance directory containing `db.sqlite` will be created automatically.

## Application Structure

- `notebook/` - Main application package
  - `__init__.py` - Application factory and configuration
  - `models.py` - Database models (Note and Comment)
  - `notes.py` - Core note-taking functionality
  - `routes.py` - Flask routes for web interface
- `static/` - Static files
  - `css/style.css` - Custom styling
  - `js/main.js` - JavaScript for comment form toggle
- `templates/` - HTML templates
  - `base.html` - Base template with common elements
  - `index.html` - Home page with note list and search
  - `note.html` - Note detail page with comments
- `run.py` - Application entry point
- `requirements.txt` - Python dependencies
- `README.md` - README file with project details

## Database Schema

The application uses two main database tables:

1. **Notes**
   - id: Primary key
   - name: Note name (unique)
   - content: Note content
   - date_created: Timestamp when note was created/updated

2. **Comments**
   - id: Primary key
   - content: Comment content
   - date_created: Timestamp when comment was added
   - note_id: Foreign key reference to Notes table
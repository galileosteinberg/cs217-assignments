from flask import Blueprint, render_template, request, redirect, url_for, flash
from .model import db, Note, Comment
from .notes import NoteBook

# Create blueprint
main = Blueprint('main', __name__)

# Initialize notebook
nb = NoteBook()


@main.route('/')
def index():
    """Homepage - shows list of notes and search functionality"""
    search_term = request.args.get('search', '')
    if search_term:
        filtered = nb.find(search_term)
    else:
        filtered = nb.notes()
    return render_template('index.html', notes=filtered,
                           search_term=search_term)


@main.route('/add', methods=['POST'])
def add_note():
    """Add a new note"""
    name = request.form.get('name', '').strip()
    content = request.form.get('content', '').strip()
    if name and content:
        nb.add(name, content)
    return redirect(url_for('main.index'))


@main.route('/note')
def show_note():
    """Display a specific note with its comments"""
    name = request.args.get('name')
    try:
        note = nb[name]
        return render_template('note.html', note=note)
    except KeyError:
        return "No such note.", 404


@main.route('/delete')
def delete_note():
    """Delete a note and all its comments"""
    name = request.args.get('name')
    if name:
        nb.delete(name)
    return redirect(url_for('main.index'))


@main.route('/add_comment', methods=['POST'])
def add_comment():
    """Add a comment to a note"""
    note_name = request.form.get('note_name')
    content = request.form.get('content', '').strip()

    if note_name and content:
        nb.add_comment(note_name, content)

    return redirect(url_for('main.show_note', name=note_name))


#app.py

from flask import Flask, render_template, request, redirect, url_for
from notes import NoteBook

app = Flask(__name__)
nb = NoteBook("data")

@app.route('/')
def index():
    search_term = request.args.get('search', '')
    if search_term:
        filtered = nb.find(search_term)
    else:
        filtered = nb.notes()
    return render_template('index.html', notes=filtered, search_term=search_term)

@app.route('/add', methods=['POST'])
def add_note():
    name = request.form.get('name', '').strip()
    content = request.form.get('content', '').strip()
    if name and content:
        nb.add(name, content)
    return redirect(url_for('index'))

@app.route('/note')
def show_note():
    name = request.args.get('name')
    try:
        note = nb[name]
        return render_template('note.html', note=note)
    except KeyError:
        return "No such note.", 404


if __name__ == "__main__":
    app.run(debug=True)
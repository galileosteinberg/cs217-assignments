from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

# Initialize SQLAlchemy
db = SQLAlchemy()


class Note(db.Model):
    __tablename__ = 'notes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.now())

    # Define relationship with Comment - cascade delete when note is deleted
    comments = db.relationship('Comment', backref='note',
                               cascade='all, delete-orphan', lazy='joined')

    def __repr__(self):
        return f"Note('{self.name}', '{self.date_created}')"

    def text(self):
        """Return the content of the note (for compatibility with previous code)"""
        return self.content


class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.now())
    note_id = db.Column(db.Integer, db.ForeignKey('notes.id'), nullable=False)

    def __repr__(self):
        return f"Comment('{self.content[:20]}...', '{self.date_created}')"
from .model import db, Note, Comment
from datetime import datetime
from sqlalchemy import or_


class NoteBook:
    """
    Core notebook functionality - now using database instead of files
    """

    def __init__(self, directory=None):
        """
        Initialize the notebook
        The directory parameter is kept for backwards compatibility
        but is not used in this database implementation
        """
        pass

    def add(self, name, content):
        """
        Create or update a note with the given name and content.
        Returns True for success.
        """
        # Check if the note already exists
        note = Note.query.filter_by(name=name).first()

        if note:
            # Update existing note
            note.content = content
            note.date_created = datetime.now()
        else:
            # Create new note
            note = Note(name=name, content=content)
            db.session.add(note)

        db.session.commit()
        return True

    def notes(self):
        """
        Return a list of all note names.
        """
        return [note.name for note in
                Note.query.order_by(Note.date_created.desc()).all()]

    def find(self, term):
        """
        Return a list of note names where the name, content,
        or any associated comment contains the search term (case-insensitive).
        """
        if not term:
            return self.notes()

        # Create search pattern
        search_pattern = f"%{term.lower()}%"

        # Find notes by name or content
        notes_query = Note.query.filter(
            or_(
                Note.name.ilike(search_pattern),
                Note.content.ilike(search_pattern)
            )
        )

        # Find notes with matching comments
        notes_with_matching_comments = Note.query.join(Note.comments).filter(
            Comment.content.ilike(search_pattern)
        )

        # Combine results (union eliminates duplicates)
        matching_notes = notes_query.union(notes_with_matching_comments).all()

        return [note.name for note in matching_notes]

    def __getitem__(self, name):
        """
        Return a Note object for the given note name.
        Raise KeyError if no such note exists.
        """
        note = Note.query.filter_by(name=name).first()
        if not note:
            raise KeyError(f"No note named '{name}' found.")
        return note

    def delete(self, name):
        """
        Delete a note and all its comments.
        Returns True if successful, False if note doesn't exist.
        """
        note = Note.query.filter_by(name=name).first()
        if not note:
            return False

        db.session.delete(note)
        db.session.commit()
        return True

    def add_comment(self, note_name, content):
        """
        Add a comment to a note.
        Returns True if successful, False if note doesn't exist.
        """
        note = Note.query.filter_by(name=note_name).first()
        if not note:
            return False

        comment = Comment(content=content, note=note)
        db.session.add(comment)
        db.session.commit()
        return True
import os

class Note:
    def __init__(self, name, content):
        self.name = name
        self.content = content

    def text(self):
        return self.content


class NoteBook:
    def __init__(self, directory='data'):
        self.directory = directory
        os.makedirs(self.directory, exist_ok=True)

    def __getitem__(self, name):
        """
        Return a Note object for the given note name.
        Raise KeyError if no such note file exists.
        """
        filename = os.path.join(self.directory, f"{name}.txt")
        if not os.path.isfile(filename):
            raise KeyError(f"No note named '{name}' found.")
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()
        return Note(name, content)

    def add(self, name, content):
        """
        Create or overwrite a note file with the given name and content.
        Returns True for success (always).
        """
        filename = os.path.join(self.directory, f"{name}.txt")
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        return True

    def notes(self):
        """
        Return a list of all note names found in the data directory.
        """
        all_notes = []
        for filename in os.listdir(self.directory):
            if filename.endswith(".txt"):
                note_name = filename[:-4]  # remove .txt
                all_notes.append(note_name)
        return all_notes

    def find(self, term):
        """
        Return a list of all note names whose name or content
        contains the given search term (case-insensitive).
        """
        matches = []
        for note_name in self.notes():
            if term.lower() in note_name.lower():
                matches.append(note_name)
            else:
                content = self[note_name].text()
                if term.lower() in content.lower():
                    matches.append(note_name)
        return matches
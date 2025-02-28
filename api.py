from fastapi import FastAPI, Request
from notes import NoteBook
import uvicorn

app = FastAPI()
nb = NoteBook("data")

@app.get("/")
def root():
    return {
        "message": (
            "Welcome to the Notes API.\n "
            "GET  /list           -> list all note names\n"
            "GET  /find?term=xyz   -> find notes containing 'xyz'\n"
            "GET  /note/NAME      -> returns text of note 'NAME'\n"
            "POST /add            -> add a note via JSON {name,content}\n"
        )
    }

@app.get("/list")
def list_notes():
    return nb.notes()

@app.get("/find")
def find_notes(term: str):
    result = nb.find(term)
    return {"term": term, "notes": [result]}

@app.get("/note/{name}")
def get_note(name: str):
    try:
        note = nb[name]
        return note.text()
    except KeyError:
        return f"No note named '{name}' found."

@app.post("/add")
async def add_note(request: Request):
    data = await request.json
    name = data["name"]
    content = data["content"]
    if not name or not content:
        return {"success": False, "message": "name and content are required"}
    nb.add(name, content)
    return {"success": True, "message": f"Note '{name}' added successfully."}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)


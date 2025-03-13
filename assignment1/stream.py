#stream.py

import streamlit as st
from notes import NoteBook

nb = NoteBook('data')

# st.title("NoteBook")

st.set_page_config(page_title="NoteBook", layout="wide")
st.markdown(
    """
    <style>
    .reportview-container {
        background-color: #F5F7FA;
    }
    .stButton>button {
        background-color: #3366FF;
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.5em 1em;
    }
    .stButton>button:hover {
        background-color: #254eda;
    }
    </style>
    """,
    unsafe_allow_html=True
)

header = st.title("NoteBook")

tab1, tab2 = st.tabs(["Show note", "Add note"])

with tab1:
    st.subheader("Search & View Notes")
    search_term = st.text_input("Search term", '')
    if search_term:
        filtered = nb.find(search_term)
        st.write(f"Notes matching '{search_term}':")
    else:
        filtered = nb.notes()
        st.write("All notes:")
        # Show list in a small table or as text
    st.dataframe(filtered, use_container_width=True)

    if filtered:
        chosen = st.selectbox("Select a note to view", filtered)
        st.write("**Content**")
        st.write(nb[chosen].text())
    else:
        st.write("No notes found.")

with tab2:
    st.subheader("Add a New Note")
    new_name = st.text_input("Note name")
    new_content = st.text_area("Note content")
    if st.button("Add note"):
        if new_name and new_content:
            nb.add(new_name, new_content)
            st.success(f"Note '{new_name}' added!")
        else:
            st.error("Please enter both a name and some content.")
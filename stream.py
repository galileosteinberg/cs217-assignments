import streamlit as st
from notes import NoteBook

nb = NoteBook('data')

st.title("NoteBook")

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
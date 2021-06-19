import streamlit as st
import awesome_streamlit as ast

import coach
import user

currentUser = ""

PAGES = {
    "Coach": coach,
    "User": user,
}

def main():
    """Main function of the App"""
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))

    page = PAGES[selection]

main()
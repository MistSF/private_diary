import streamlit as st
import awesome_streamlit as ast

from functions.nav import nav
import coach
import user

currentUser = ""

PAGES = {
    "Coach": coach,
    "User": user,
}

def main() :
    """Main function of the App"""
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))
    if selection :
        nav.setCurrentUser(selection)
        page = PAGES[selection]
        nav.goTo(PAGES[selection])
        page.app()

main()
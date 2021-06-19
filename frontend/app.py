import streamlit as st
import awesome_streamlit as ast
import requests

from functions.nav import nav
import coach
import user

currentUser = ""

def main() :
    """Main function of the App"""
    st.sidebar.title("Navigation")
    goCoach = st.sidebar.button("Coach")
    goUser = st.sidebar.button("User")
    if goCoach :
        nav.setCurrentUser("Coach")
        nav.goTo(coach)

    if goUser :
        nav.setCurrentUser("User")
        nav.goTo(user)
    
    if nav.getCurrentUser() == "User" :
        r = requests.get("{}/coach/clients".format(nav.url))
        value = st.sidebar.selectbox("Select Dynamic", options=list(r.json()))
        nav.setCurrentClient(value)

    if nav.getPage() :
        nav.getPage().app()

main()
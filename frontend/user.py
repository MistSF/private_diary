import streamlit as st
from functions.nav import nav

def app() :
    client = nav.getCurrentClient()
    if client != 0 :
        st.write("Hello {} {}".format(client[1], client[2]))
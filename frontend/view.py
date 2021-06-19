from numpy.lib.function_base import iterable
import streamlit  as st
import awesome_streamlit as ast
import requests
from app import currentUser

def app():
    if currentUser != "" :
        st.write("Hello {}". format(currentUser[1]))
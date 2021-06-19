import streamlit  as st
import requests
from functions.nav import nav

def app() :

    st.write("Coach")
    r = requests.get("http://localhost:8000/coach/clients")

    value = st.selectbox("Select Dynamic", options=list(r.json()))
    st.write("{} {}".format(value[1], value[2]))
import streamlit  as st
import requests
from streamlit import proto
from functions.nav import nav

import coach

def app() :

    client = nav.getCurrentClient()

    st.write("New User".format(client[1], client[2]))

    forms = st.form(key="update")
    firstname = forms.text_input(label='new firstname')
    lastname = forms.text_input(label='new lastname')
    submit_button = forms.form_submit_button('Submit')

    if submit_button :
        if firstname != "" and lastname != "" :
            requests.post("{}/coach/add?firstname={}&lastname={}".format(nav.getUrl(), firstname, lastname))
            nav.goTo(coach)
        else :
            st.error("Please fill the form !")
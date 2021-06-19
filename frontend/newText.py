import streamlit  as st
import requests
from streamlit import proto
from functions.nav import nav

import user

def app() :

    client = nav.getCurrentClient()

    st.write("New Text")

    forms = st.form(key="update")
    text = forms.text_input(label='new text')
    submit_button = forms.form_submit_button('Submit')

    if submit_button :
        if text != "" :
            requests.post("{}/client/newText?id_client={}&text={}".format(nav.getUrl(), client[0], text))
        nav.goTo(user)
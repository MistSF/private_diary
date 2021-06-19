import streamlit  as st
import requests
from streamlit import proto
from functions.nav import nav

import coach

def app() :

    client = nav.getCurrentClient()

    st.write("Edit {} {}".format(client[1], client[2]))

    forms = st.form(key="update")
    firstname = forms.text_input(label='new firstname')
    lastname = forms.text_input(label='new lastname')
    submit_button = forms.form_submit_button('Submit')

    if submit_button :
        if firstname == "" :
            firstname = client[1]
        if lastname == "" :
            lastname = client[2]
        requests.put("{}/coach/update?ID={}&firstname={}&lastname={}".format(nav.getUrl(), client[0], firstname, lastname))
        nav.goTo(coach)
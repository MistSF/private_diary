import streamlit  as st
import requests
from streamlit import proto
from functions.nav import nav

import edit
import new

def app() :

    st.write("Coach")
    r = requests.get("{}/coach/clients".format(nav.getUrl()))

    value = st.selectbox("Select Dynamic", options=list(r.json()))
    nav.setCurrentClient(value)
    cols = st.beta_columns((1, .2, .2))
    cols[0].write("{} {}".format(value[1], value[2]))
    editButton = cols[1].button("edit")
    delete = cols[2].button("delete")

    newClient = st.button("New Client")

    if newClient :
        nav.goTo(new)

    if editButton :
        nav.goTo(edit)

    if delete :
        x = requests.delete("{}/coach/delClient?ID={}".format(nav.getUrl(), nav.getCurrentClient()[0]))
    
    rtext = requests.get("{}/client/alltext?id_client={}".format(nav.getUrl(), value[0]))

    st.title("Texte")
    for x in rtext.json() :
        cols = st.beta_columns(3)
        cols[0].write(x[1])
        cols[1].write(x[3])
        cols[2].write(x[2])
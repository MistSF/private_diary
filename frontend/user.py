from numpy import datetime64
import streamlit as st
import requests
from datetime import datetime
from functions.nav import nav

import editText
import newText

def app() :
    client = nav.getCurrentClient()
    if client != 0 :
        st.write("Hello {} {}".format(client[1], client[2]))
        rtext = requests.get("{}/client/alltext?id_client={}".format(nav.getUrl(), nav.getCurrentClient()[0]))

        st.title("Texte")
        for x in rtext.json() :
            cols = st.beta_columns(4)
            cols[0].write(x[1])
            cols[1].write(x[3])
            cols[2].write(x[2])
            if x[2][:10] == str(datetime.now())[:10] :
                editButton = cols[3].button("Edit", key=x[0])
                if editButton :
                    nav.setCurrentText(x)
                    nav.goTo(editText)
        newTextButton = st.button("New Text")
        if newTextButton :
            nav.goTo(newText)
import matplotlib.pyplot as plt
import streamlit  as st
import requests
import pandas as pd
from functions.nav import nav
import plotly.express as px

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

    Emotion = []

    st.title("Texte")
    for x in rtext.json() :
        Emotion.append(x[3])
        cols = st.beta_columns(3)
        cols[0].write(x[1])
        cols[1].write(x[3])
        cols[2].write(x[2])

    Emotion = pd.DataFrame(Emotion)
    data = Emotion.value_counts()
    data.plot.pie()
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()
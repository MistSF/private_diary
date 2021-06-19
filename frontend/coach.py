import streamlit  as st
import awesome_streamlit as ast
import requests

import view

from functions.client import openView

st.write("Coach")
r = requests.get("http://localhost:8000/coach/clients")

for x in r.json() :
    cols = st.beta_columns((1, .25))
    cols[0].write(f'- {x[1]} {x[2]}')
    res_Edit = cols[1].button(f'view', key=x[0])
    if res_Edit :
        print(x)

ast.shared.components.write_page(view)
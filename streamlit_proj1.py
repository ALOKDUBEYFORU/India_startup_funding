import streamlit as st
import numpy as np
import pandas as pd

st.title('Startup Funding Analysis')
st.sidebar.title('Analysis type')
s_option = st.sidebar.selectbox("Choose the category",['investor','startup','Over all Analysis'])
if s_option=='investor':
    s_suboption = st.sidebar.selectbox("Choose the investor",['first','second'])
elif s_option == 'startup':
    pass
else:
    pass


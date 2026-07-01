import eda 
import prediction
import pandas as pd
import streamlit as st

page = st.sidebar.selectbox('Page: ', ('eda', 'prediction'))

if page == 'eda':
    eda.run()
else:
    prediction.run()
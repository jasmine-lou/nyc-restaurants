import requests
from sodapy import Socrata
import pandas as pd
import streamlit as st

st.title("NYC Restaurant Inspection Data")

client = Socrata("data.cityofnewyork.us", None)

results = client.get("43nn-pn8j", limit=2000)

df = pd.DataFrame.from_records(results)

st.dataframe(df, use_container_width=True)
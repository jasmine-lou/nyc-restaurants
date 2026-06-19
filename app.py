import requests
import pandas as pd
import streamlit as st

st.title("NYC Restaurant Inspection Data")

url = "https://data.cityofnewyork.us/api/v3/views/43nn-pn8j/query.json"

payload = {
    "query": """
        SELECT *
        LIMIT 1000
    """
}

response = requests.post(url, json=payload)
response.raise_for_status()

data = response.json()

# Adjust this if the API returns metadata differently
df = pd.DataFrame(
    data["data"],
    columns=["Restaurant", "Grade", "Cuisine"]
)

st.dataframe(df, use_container_width=True)
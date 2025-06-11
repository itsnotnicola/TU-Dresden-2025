import streamlit as st
from google.cloud import storage
import json
import pandas as pd
from awesome_table import AwesomeTable
from awesome_table.column import Column


BUCKET_NAME = 'hackathon-team2-bucket'
FILE_NAME = 'all_customer_support_analysis.json'

st.title('Welcome to Ottomatic Reply')
st.write('''#### Here’s where great service starts.

This internal support space is designed to help our team assist customers quickly, confidently, and in true Otto style.

We keep it efficient, empathetic, and always on-brand — just like the service our customers expect.

Let’s make support smarter, together.''')

if st.button('Load data', type='primary' ):
    client = storage.Client(project= 'ogcs-av8t-ailaboratory')
    bucket = client.bucket(BUCKET_NAME)
    blob = bucket.blob(FILE_NAME)

    data = blob.download_as_text()
    # JSON data to Python dictionary
    data_dict = json.loads(data)
    st.write(data_dict)
    for key, value in data_dict.items():
        print(f"{key}: {value}")


import streamlit as st

# Using "with" notation
with st.sidebar:
    st.metric(label='Number of unanswered tickets:', value=10)
    add_selectbox = st.selectbox(
    "Support Team",
    ("All","Shipping and Delivery Updates (Aftersales)", "Returns and Exchanges Management (Aftersales)",
        "Claims and Product Defects (Aftersales)", "Payment and Billing Support (Aftersales)", "Product Consultation (Presales)", 
        "Order Support (Presales)", "Technical Assistance (Presales/Aftersales)", "Customer Account Support (Aftersales)", 
        "Loyalty Programs and Discounts (Presales/Aftersales)", "Customer Feedback and Complaints (Aftersales)")
    )
    field = st.radio(
        "Sort by field:",
        ("Time", "Urgency", "Sentiment")
    )

    options = ['Ascending', 'Descending']
    selection = st.pills(f"Sort {field} by:", options, selection_mode="single")
    st.markdown(f"Your selected options: {selection}.")

    options = ['All','Unanswered', 'Answered']
    selection = st.pills(f"Sort status by:", options, selection_mode="single")
    st.markdown(f"Your selected options: {selection}.")

st.logo('Otto_Group_Logo_2022.svg.png')

sample_data = {}

AwesomeTable(pd.json_normalize(sample_data), columns=[
    Column(name='id', label='ID'),
    Column(name='name', label='Name'),
    Column(name='job_title', label='Job Title'),
    Column(name='avatar', label='Avatar'),
    Column(name='_url.social_media', label='Social Media'),
    Column(name='_url.document', label='Document'),
])
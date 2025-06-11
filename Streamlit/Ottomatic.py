import streamlit as st

st.title('Welcome to Ottomatic Reply')
st.write('''#### Here’s where great service starts.

This internal support space is designed to help our team assist customers quickly, confidently, and in true Otto style.

We keep it efficient, empathetic, and always on-brand — just like the service our customers expect.

Let’s make support smarter, together.''')

st.button('Load data', type='primary' )

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

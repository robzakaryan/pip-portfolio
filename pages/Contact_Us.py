import streamlit as st
from send_email import email

st.set_page_config(layout='centered')
st.header('Contact us')

with st.form(key='send_email'):
    user_email = st.text_input('Enter your email', placeholder='Enter email')
    raw_message = st.text_area('Your message')
    message = f"""\
Subject: New email from {user_email}

From: {user_email}
{raw_message}
"""
    submit_btn = st.form_submit_button('Send email')
    if submit_btn:
        email(message)
        st.success('Email was sent')


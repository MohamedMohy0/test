import streamlit as st

st.set_page_config(page_title="Secure App")

# Simulate locked state
locked = st.checkbox("🔒 Lock the page manually")

if locked:
    st.error("🔐 This page is locked. You cannot continue.")
    st.stop()

st.success("✅ Welcome! The page is active.")

# Main content
st.write("This is your secure Streamlit app.")

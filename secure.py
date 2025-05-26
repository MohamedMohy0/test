import streamlit as st
import time

st.title("Refresh Page Button Demo")

# Display current time to see effect of refresh
st.write("Page loaded at:", time.strftime("%H:%M:%S"))

# Button to refresh (rerun) the app
if st.button("Refresh Page"):
    st.experimental_rerun()

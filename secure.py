import streamlit as st
import time

st.set_page_config(page_title="🔁 Refresh Page")

st.title("🔁 Refresh Button Demo")

# Show current time (proves refresh happened)
st.write("This page was last loaded at:")
st.code(time.strftime("%H:%M:%S"))

# Add refresh button
if st.button("🔄 Refresh Page"):
    st.experimental_rerun()

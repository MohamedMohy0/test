import streamlit as st

st.set_page_config(page_title="🔄 Refresh Demo")

st.title("🔁 Refresh Button Example")

if st.button("🔄 Refresh Page"):
    st.experimental_rerun()

st.write("This page was last loaded at:")
st.code(st.session_state.get("last_load_time", "First load"))

import time
st.session_state["last_load_time"] = time.strftime("%H:%M:%S")

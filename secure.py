import streamlit as st
import streamlit.components.v1 as components

st.title("Test Right Click Block")

right_click_blocker = """
<script>
document.addEventListener('contextmenu', event => event.preventDefault());
</script>
"""

components.html(right_click_blocker, height=0)
st.write("Try right-clicking anywhere inside this app area.")

import streamlit as st
import streamlit.components.v1 as components

st.title("Right-click to refresh the page")

js = """
<script>
document.addEventListener('contextmenu', function(e) {
    e.preventDefault();
    location.reload();
});
</script>
"""

components.html(js, height=0)
st.write("Try right-clicking anywhere inside this app area to refresh the page.")

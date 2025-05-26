import streamlit as st
import streamlit.components.v1 as components

st.title("Disable right-click inside app area")

js = """
<script>
document.addEventListener('contextmenu', function(e) {
    e.preventDefault();
    alert("Right-click is disabled inside this app.");
});
</script>
"""

components.html(js)
st.write("Try right-clicking anywhere inside this app area.")

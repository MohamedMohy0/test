import streamlit as st
import streamlit.components.v1 as components

st.title("Protected Streamlit App")

js = """
<script>
document.addEventListener('contextmenu', function(e) {
    e.preventDefault();
    alert('Right-click is disabled on this site.');
});
</script>
"""

components.html(js)
st.write("Right-click is disabled. This helps deter casual inspection.")

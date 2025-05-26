import streamlit as st
import streamlit.components.v1 as components

st.title("Right-click Disabled on Full Page")

js_code = """
<style>
#warning {
    position: fixed;
    bottom: 20px;
    right: 20px;
    background: #f44336;
    color: white;
    padding: 12px 20px;
    border-radius: 5px;
    font-family: Arial, sans-serif;
    display: none;
    z-index: 9999999; /* super high to be on top */
    box-shadow: 0 0 10px rgba(0,0,0,0.5);
}
</style>

<div id="warning">Right-click is disabled on this site.</div>

<script>
document.addEventListener('contextmenu', function(e) {
    e.preventDefault();
    var warning = document.getElementById('warning');
    warning.style.display = 'block';
    setTimeout(() => {
        warning.style.display = 'none';
    }, 3000);
});
</script>
"""

components.html(js_code, height=0)

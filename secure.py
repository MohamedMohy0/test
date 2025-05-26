import streamlit as st
import streamlit.components.v1 as components

st.title("Detect DevTools inside Streamlit app")

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
    z-index: 9999999;
    box-shadow: 0 0 10px rgba(0,0,0,0.5);
}
</style>

<div id="warning">DevTools detected! Please close it.</div>

<script>
(function() {
    var warning = document.getElementById('warning');
    var devtoolsOpen = false;
    
    function checkDevTools() {
        const threshold = 160;
        const widthThreshold = window.outerWidth - window.innerWidth > threshold;
        const heightThreshold = window.outerHeight - window.innerHeight > threshold;
        if (widthThreshold || heightThreshold) {
            if (!devtoolsOpen) {
                devtoolsOpen = true;
                warning.style.display = 'block';
                // Optionally reload page:
                // location.reload();
            }
        } else {
            if (devtoolsOpen) {
                devtoolsOpen = false;
                warning.style.display = 'none';
            }
        }
    }
    
    // Check every 500ms
    setInterval(checkDevTools, 500);
})();
</script>
"""

components.html(js_code, height=0)

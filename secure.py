import streamlit as st
import streamlit.components.v1 as components

st.title("Block Right-Click & Detect DevTools inside Streamlit")

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
    user-select: none;
    pointer-events: none;
}
</style>

<div id="warning">Warning: Right-click or DevTools are disabled.</div>

<script>
(function() {
    var warning = document.getElementById('warning');
    var devtoolsOpen = false;

    // Block right-click anywhere inside document
    document.addEventListener('contextmenu', function(e) {
        e.preventDefault();
        warning.style.display = 'block';
        setTimeout(() => {
            warning.style.display = 'none';
        }, 3000);
    });

    // DevTools detection - check every 500ms
    function checkDevTools() {
        const threshold = 160;
        const widthDiff = window.outerWidth - window.innerWidth;
        const heightDiff = window.outerHeight - window.innerHeight;

        if (widthDiff > threshold || heightDiff > threshold) {
            if (!devtoolsOpen) {
                devtoolsOpen = true;
                warning.style.display = 'block';
                // Optional: uncomment to reload on devtools open
                // location.reload();
            }
        } else {
            if (devtoolsOpen) {
                devtoolsOpen = false;
                warning.style.display = 'none';
            }
        }
    }

    setInterval(checkDevTools, 500);
})();
</script>
"""

components.html(js_code, height=0)

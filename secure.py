import streamlit as st
import streamlit.components.v1 as components

st.title("Right-click disabled on entire Streamlit page")

js_code = """
<style>
#overlay {
    position: fixed;
    top: 0; left: 0; right: 0; bottom: 0;
    width: 100vw;import streamlit as st
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

    height: 100vh;
    z-index: 9999999;
    /* Make overlay invisible but catch mouse events */
    background: transparent;
}

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
    z-index: 10000000;
    box-shadow: 0 0 10px rgba(0,0,0,0.5);
}
</style>

<div id="overlay"></div>
<div id="warning">Right-click is disabled on this site.</div>

<script>
const overlay = document.getElementById('overlay');
const warning = document.getElementById('warning');

overlay.addEventListener('contextmenu', function(e) {
    e.preventDefault();
    warning.style.display = 'block';
    setTimeout(() => {
        warning.style.display = 'none';
    }, 3000);
});
</script>
"""

components.html(js_code, height=0)

import streamlit as st
import streamlit.components.v1 as components

st.title("Right-click anywhere to refresh the page")

html_code = """
<style>
  /* Fullscreen transparent overlay */
  #overlay {
    position: fixed;
    top: 0; left: 0; right: 0; bottom: 0;
    width: 100vw;
    height: 100vh;
    z-index: 9999;
    background: transparent;
  }
</style>

<div id="overlay"></div>

<script>
  const overlay = document.getElementById('overlay');
  overlay.addEventListener('contextmenu', function(e) {
    e.preventDefault();
    window.location.reload();
  });
</script>
"""

components.html(html_code, height=0)

st.write("Try right-clicking anywhere inside this app area to refresh the page.")

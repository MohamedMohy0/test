import streamlit as st
import streamlit.components.v1 as components

st.write("Try right-click inside this app area — it should be blocked.")

# Inject JS to disable right-click inside the iframe area
components.html(
    """
    <script>
    document.addEventListener('contextmenu', event => {
        event.preventDefault();
        alert('Right-click is disabled inside the app.');
    });
    </script>
    """,
    height=0,
)

st.write("Try right-clicking anywhere inside this app area.")

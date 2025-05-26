import streamlit as st
import streamlit.components.v1 as components

st.title("Full Browser Refresh Button")

if st.button("Refresh (F5)"):
    components.html(
        """
        <script>
        window.location.reload();
        </script>
        """,
        height=0,
    )

st.write("Click the button above to reload the entire page (like F5).")

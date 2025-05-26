import streamlit as st

st.title("Right-click to refresh the page")

# Inject JS into the main page DOM using st.markdown
st.markdown(
    """
    <script>
    document.addEventListener('contextmenu', function(e) {
        e.preventDefault();
        window.location.reload();
    });
    </script>
    """,
    unsafe_allow_html=True,
)

st.write("Try right-clicking anywhere inside this app area to refresh the page.")

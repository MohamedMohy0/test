import streamlit as st

st.markdown("""
    <script>
    document.addEventListener('contextmenu', function(event) {
        event.preventDefault();
        alert("Right-click is disabled inside this app.");
    });
    </script>
    """, unsafe_allow_html=True)

st.write("Try right-clicking inside the app area now.")

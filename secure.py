import streamlit as st

st.set_page_config(page_title="Secure Page", layout="centered")

# Page Content
st.title("🔐 Secure Streamlit Page")
st.write("Basic JavaScript protections are active.")

# Inject JavaScript
st.markdown("""
    <script>
        // Disable right-click
        document.addEventListener('contextmenu', event => event.preventDefault());

        // Block some DevTools shortcuts
        document.onkeydown = function(e) {
            if (e.keyCode === 123 || // F12
                (e.ctrlKey && e.shiftKey && e.keyCode === 73) || // Ctrl+Shift+I
                (e.ctrlKey && e.shiftKey && e.keyCode === 74) || // Ctrl+Shift+J
                (e.ctrlKey && e.keyCode === 85)) { // Ctrl+U
                return false;
            }
        };

        // Reload if user switches back to tab
        document.addEventListener("visibilitychange", function () {
            if (!document.hidden) {
                location.reload();
            }
        });
    </script>
""", unsafe_allow_html=True)

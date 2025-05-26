import streamlit as st

st.set_page_config(page_title="🔐 Secure Page", layout="centered")

st.title("Secure Streamlit Page")

st.write("This page has protections against DevTools, right-click, and tab-switching.")

# Inject custom JavaScript
st.markdown("""
    <script>
        // ✅ Disable right-click
        document.addEventListener('contextmenu', function(e) {
            e.preventDefault();
        }, false);

        // ✅ Block devtools keyboard shortcuts
        document.onkeydown = function(e) {
            if (
                e.keyCode == 123 || // F12
                (e.ctrlKey && e.shiftKey && e.keyCode == 73) || // Ctrl+Shift+I
                (e.ctrlKey && e.shiftKey && e.keyCode == 74) || // Ctrl+Shift+J
                (e.ctrlKey && e.keyCode == 85) // Ctrl+U
            ) {
                return false;
            }
        };

        // ✅ Detect if DevTools is open (basic trick)
        var element = new Image();
        Object.defineProperty(element, 'id', {
            get: function() {
                alert("🚨 DevTools detected! Reloading...");
                location.reload();
            }
        });
        console.log(element);

        // ✅ Reload page when user switches tabs
        document.addEventListener("visibilitychange", function () {
            if (!document.hidden) {
                location.reload();
            }
        });
    </script>
""", unsafe_allow_html=True)

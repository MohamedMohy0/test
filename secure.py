import streamlit as st

st.set_page_config(page_title="Secure Page", layout="centered")

# Page Content
st.title("🔐 Secure Streamlit Page")
st.write("Basic JavaScript protections are active.")

# Inject JavaScript
st.markdown("""
    <script>
        // Block right-click
        document.addEventListener('contextmenu', function(e) {
            e.preventDefault();
        }, false);

        // Block key combinations
        document.onkeydown = function(e) {
            if (e.keyCode == 123) { return false; } // F12
            if (e.ctrlKey && e.shiftKey && e.keyCode == 73) { return false; } // Ctrl+Shift+I
            if (e.ctrlKey && e.shiftKey && e.keyCode == 74) { return false; } // Ctrl+Shift+J
            if (e.ctrlKey && e.keyCode == 85) { return false; } // Ctrl+U
        };

        // Detect DevTools open (basic)
        let devtoolsOpen = false;
        const element = new Image();
        Object.defineProperty(element, 'id', {
            get: function () {
                devtoolsOpen = true;
                alert("DevTools is open! Action blocked.");
                location.reload();
            }
        });
        console.log(element);

        // Reload when tab returns to focus
        document.addEventListener("visibilitychange", function () {
            if (!document.hidden) {
                location.reload();
            }
        });
    </script>
""", unsafe_allow_html=True)


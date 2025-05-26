import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="🔐 Secure Test")

st.title("🔐 Streamlit + JavaScript Event Detection")

st.write("Try switching tabs, right-clicking, or opening DevTools.")

# A placeholder to display messages from JS
message_area = st.empty()

# JavaScript to send messages to Streamlit via iframe
components.html("""
<!DOCTYPE html>
<html>
<head>
    <script>
        function notifyStreamlit(msg) {
            const streamlitReceiver = window.parent;
            streamlitReceiver.postMessage({ type: "js-event", message: msg }, "*");
        }

        // Right-click detection
        document.addEventListener('contextmenu', function(e) {
            e.preventDefault();
            notifyStreamlit("🖱️ Right-click detected");
        });

        // DevTools detection (basic)
        const element = new Image();
        Object.defineProperty(element, 'id', {
            get: function () {
                notifyStreamlit("🚨 DevTools detected");
            }
        });
        console.log(element);

        // Tab visibility detection
        document.addEventListener("visibilitychange", function () {
            if (!document.hidden) {
                notifyStreamlit("↩️ Tab was switched and returned");
            }
        });

        // Listen for messages (for testing)
        window.addEventListener("message", (event) => {
            if (event.data.type === "ping") {
                notifyStreamlit("✅ JS Connected");
            }
        });
    </script>
</head>
<body>
    <h3>This is the embedded JS listener.</h3>
</body>
</html>
""", height=150)

# Receive JS messages using Streamlit's JS event system
st.markdown("""
<script>
    const streamlitWindow = window;
    window.addEventListener("message", (event) => {
        if (event.data.type === "js-event") {
            const msg = event.data.message;
            // Pass message into Streamlit via form input
            const input = window.parent.document.querySelector('iframe[srcdoc] + div input');
            if (input) {
                input.value = msg;
                input.dispatchEvent(new Event('input', { bubbles: true }));
            }
        }
    });

    // Trigger connection test
    window.onload = () => {
        window.parent.postMessage({ type: "ping" }, "*");
    };
</script>
""", unsafe_allow_html=True)

# Invisible input to catch JS messages
event = st.text_input("JS Event", "", label_visibility="collapsed")
if event:
    message_area.warning(f"🧠 JS Event: {event}")

import streamlit as st
import time
import streamlit.components.v1 as components

if "reload_count" not in st.session_state:
    st.session_state.reload_count = 0
st.session_state.reload_count += 1

st.title("Auto-refresh demo with timestamp")

load_time = time.strftime("%Y-%m-%d %H:%M:%S")
st.write(f"Page loaded at: {load_time}")
st.write(f"Reload count: {st.session_state.reload_count}")

js_code = """
<script>
// Reload on right-click or devtools open (same as before)
function reloadPage() {
    window.location.reload();
}

document.addEventListener('contextmenu', function(e) {
    e.preventDefault();
    reloadPage();
});

let devtoolsOpen = false;
const threshold = 160;
setInterval(() => {
    const widthThreshold = window.outerWidth - window.innerWidth > threshold;
    const heightThreshold = window.outerHeight - window.innerHeight > threshold;
    if (widthThreshold || heightThreshold) {
        if (!devtoolsOpen) {
            devtoolsOpen = true;
            reloadPage();
        }
    } else {
        devtoolsOpen = false;
    }
}, 1000);
</script>
"""

components.html(js_code)

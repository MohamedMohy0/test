import streamlit as st
import time
import streamlit.components.v1 as components

st.title("Auto-refresh on right-click or devtools open")

load_time = time.strftime("%Y-%m-%d %H:%M:%S")
st.write(f"Page loaded at: {load_time}")

js_code = """
<script>
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

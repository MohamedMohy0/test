import streamlit as st
import streamlit.components.v1 as components

st.title("Auto-refresh on Right-click or DevTools")

js_code = """
<script>
// Reload page function
function reloadPage() {
    window.location.reload();
}

// Right-click detection
document.addEventListener('contextmenu', function(e) {
    e.preventDefault();   // optionally block right-click menu
    reloadPage();
});

// DevTools detection - simple trick
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
st.write("Try right-clicking or opening DevTools — the page will refresh automatically.")

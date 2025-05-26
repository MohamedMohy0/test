import streamlit as st

st.set_page_config(page_title="🔒 Secure App", layout="centered")

st.title("🔐 Protected Streamlit Page")
st.write("JavaScript protections are now enabled:")

# HTML + JS protections
custom_js = """
<script>
// Disable right-click
document.addEventListener('contextmenu', function(e) {
    e.preventDefault();
});

// Disable devtools shortcuts
document.onkeydown = function(e) {
    if (
        e.keyCode === 123 || // F12
        (e.ctrlKey && e.shiftKey && e.keyCode === 73) || // Ctrl+Shift+I
        (e.ctrlKey && e.shiftKey && e.keyCode === 74) || // Ctrl+Shift+J
        (e.ctrlKey && e.keyCode === 85) // Ctrl+U
    ) {
        e.preventDefault();
        return false;
    }
};

// Detect DevTools (basic trick)
let devtoolsOpen = false;
const element = new Image();
Object.defineProperty(element, 'id', {
    get: function () {
        devtoolsOpen = true;
        alert("🚨 DevTools detected!");
        location.reload();
    }
});
console.log(element);

// Reload on tab return
document.addEventListener("visibilitychange", function () {
    if (!document.hidden) {
        location.reload();
    }
});
</script>
"""

# Inject into page
st.components.v1.html(custom_js, height=0)

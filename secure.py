import streamlit as st
import streamlit.components.v1 as components

st.title("Auto-reload on right-click or tab focus")

js_code = """
<script>
function reloadPage() {
    console.log("Reloading page now!");
    window.location.reload();
}

document.addEventListener('contextmenu', function(e) {
    console.log("Right-click detected");
    e.preventDefault();
    reloadPage();
});

window.addEventListener('focus', function() {
    console.log("Window gained focus - reloading");
    reloadPage();
});
</script>
"""

components.html(js_code, height=0)
st.write("Try right-click or switching tabs to trigger reload.")

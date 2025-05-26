import streamlit as st
import streamlit.components.v1 as components

st.title("Streamlit App with Right-click Disabled")

js = """
<script>
document.addEventListener('contextmenu', function(e) {
    e.preventDefault();
    // You can add a console message instead of alert
    console.log('Right-click disabled');
});
</script>
"""

components.html(js)
st.write("Right-click is disabled quietly without annoying popups.")

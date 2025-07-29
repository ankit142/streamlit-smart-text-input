import streamlit as st
from streamlit_smarttext_input import st_smart_text_input

st.set_page_config(page_title="SmartText Input Demo", layout="centered")
st.title("Streamlit SmartText Input Test")

# Options to test with
options = ["Toyota", "BMW", "Tesla", "Ford", "Audi", "Mercedes", "Honda"]


# Call the custom component
value = st_smart_text_input(
    label="Choose or Type a Fruit or Greeting",
    options=options,
    index=None,
    placeholder="Start typing and press Enter...",
    delay=200,
    disabled=False,
    label_visibility="visible",
)

# Display what was selected or typed
if value:
    if value.lower() in [o.lower() for o in options]:
        st.info(f"🍓 '{value}' is a known car brand from the list.")
    elif value.lower() in ["hi", "hey", "hello"]:
        st.info("Hello, I am a Python package crafted by [Ankit Guria](https://github.com/ankitguria).")
    else:
        st.warning(f"'{value}' is a new input. You can add this to the list!")

# UI Divider
st.markdown("---")
st.caption("Press ⏎ Enter after typing to trigger input capture.")

import streamlit as st
from emoji_converter import text_to_custom_emojis, get_random_emojis

st.title("Text to Emoji Translator")

# Create a form
with st.form(key='emoji_form'):
    user_text = st.text_input("Enter text to translate")
    submit_button = st.form_submit_button(label='Submit')

if submit_button:
    if not user_text.strip():
        st.warning("Please enter some text before submitting.")
    else:
        emoji_text = text_to_custom_emojis(user_text)
        st.markdown(f"### Emoji Translation:\n\n{emoji_text}")

        # Optionally, show some random emojis from emoji-helper API
        r_emojis = get_random_emojis(5)
        st.write("Random Emojis from API:", " ".join(r_emojis))

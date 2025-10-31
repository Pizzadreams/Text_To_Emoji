import streamlit as st
import emoji

def text_to_custom_emojis(text):
    # Custom word-to-emoji mapping
    emoji_map = {
        'happy': '😊',
        'sad': '😢',
        'love': '❤️',
        'cowboy': '🤠',
        'dog': ':dog:',  # Emoji shortcode example
        'cat': ':cat:'
    }
    words = text.split()
    result = []
    for w in words:
        lw = w.lower()
        if lw in emoji_map:
            result.append(emoji_map[lw])
        else:
            result.append(w)
    # Join back to a sentence
    sentence = ' '.join(result)
    # Convert any emoji shortcodes to actual emojis
    return emoji.emojize(sentence, language='alias')

st.title("Text to Emoji Translator")

with st.form("emoji_form"):
    user_text = st.text_input("Enter text to translate")
    submitted = st.form_submit_button("Submit")

if submitted:
    if not user_text.strip():
        st.warning("Please enter some text before submitting.")
    else:
        emoji_text = text_to_custom_emojis(user_text)
        st.markdown(f"### Emoji Translation:\n\n{emoji_text}")



with st.form("emoji_form"):
    user_text = st.text_input("Enter text to translate (try using emoji shortcodes like ':rocket:' or ':smile:')")
    submitted = st.form_submit_button("Submit")

if submitted:
    if not user_text.strip():
        st.warning("Please enter some text before submitting.")
    else:
        # Convert all emoji shortcodes in the sentence to emojis
        emoji_text = emoji.emojize(user_text, language='alias')
        st.markdown(f"### Emoji Translation:\n\n{emoji_text}")
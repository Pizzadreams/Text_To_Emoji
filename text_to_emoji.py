import streamlit as st
import emoji
import requests
import json

# def get_random_emojis(n=5):
#     url = f"https://emojihelper-1-v4897410.deta.app/random?n={n}&skintones=False&nogroup=Symbols,Flags"
#     response = requests.get(url)
#     return json.loads(response.text)

def text_to_custom_emojis(text):
    # Example static dictionary for demo (expand as needed)
    emoji_map = {
        "red": "🟥",
        "bull": "🐂",
        "wings": "🪽",
        "you": "👉",
        "gives": "🤲"  # example custom emoji
    }
    words = text.lower().split()
    return " ".join([emoji_map.get(word, word) for word in words])

st.title("Text to Emoji Translator")

user_text = st.text_input("Enter text to translate")

if user_text:
    emoji_text = text_to_custom_emojis(user_text)
    st.markdown(f"### Emoji Translation:\n\n{emoji_text}")

    # # Optionally, show some random emojis from emoji-helper API
    # r_emojis = get_random_emojis(5)
    # st.write("Random Emojis from API:", " ".join(r_emojis))

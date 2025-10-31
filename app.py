import streamlit as st
from emoji_converter import text_to_custom_emojis, get_random_emojis

def main():
    st.title("Text to Emoji Translator")

    user_text = st.text_input("Enter text to translate", placeholder="Type a phrase here...")

    if user_text:
        emoji_text = text_to_custom_emojis(user_text)
        st.markdown(f"### Emoji Translation:\n\n{emoji_text}")

        r_emojis = get_random_emojis(5)
        st.write("Random Emojis from API:", " ".join(r_emojis))

if __name__ == "__main__":
    main()

import streamlit as st
import emoji
from thefuzz import process

st.title("Text to Emoji Translator")

# Dictionary of emoji aliases from emoji library (e.g., ':rocket:', ':smile:')
emoji_dict = emoji.EMOJI_ALIAS_UNICODE_ENGLISH
emoji_aliases = list(emoji_dict.keys())  # List of all emoji shortcodes

with st.form("emoji_form"):
    # Text input for user to type an emoji name or approximate shortcode
    user_text = st.text_input("Enter emoji name or approximate shortcode (e.g., 'rock', 'smil')")
    submitted = st.form_submit_button("Submit")

if submitted:
    if not user_text.strip():
        st.warning("Please enter some text before submitting.")
    else:
        # Perform fuzzy matching of user input against known emoji aliases
        matched_aliases = fuzzy_emoji_search(user_text, emoji_aliases, limit=5, threshold=60)

        if matched_aliases:
            # Convert matched shortcodes to actual emojis using emoji.emojize
            emoji_translations = [emoji.emojize(alias, language='alias') for alias in matched_aliases]
            st.markdown(f"### Emoji Suggestions for '{user_text}':\n\n{' '.join(emoji_translations)}")
        else:
            st.write("No close emoji matches found. Try a different keyword.")

def fuzzy_emoji_search(query, aliases, limit=5, threshold=70):
    # Get the closest matching emoji aliases with fuzzy matching above the threshold
    results = process.extract(query, aliases, limit=limit)
    filtered = [item for item in results if item[1] >= threshold]
    return [alias for alias, score in filtered]
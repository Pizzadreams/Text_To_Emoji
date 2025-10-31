import streamlit as st
import emoji
from thefuzz import process


# Testing with emoji 2.x, emoji.EMOJI_DATA contains emoji characters as keys
# Each value is a dict with metadata, including 'alias' field which is a list of shortcodes without colons
def get_all_aliases():
    aliases = []
    for data in emoji.EMOJI_DATA.values():
        # 'alias' is a list like ['grinning_face']
        for a in data.get('alias', []):
            # Add colons to the alias shortcode format
            aliases.append(f":{a}:")
    return aliases


emoji_aliases = get_all_aliases()

st.title("Text to Emoji Translator")

with st.form("emoji_form"):
    user_text = st.text_input("Enter emoji name or approximate shortcode (e.g., 'rock', 'smil')")
    submitted = st.form_submit_button("Submit")

if submitted:
    if not user_text.strip():
        st.warning("Please enter some text before submitting.")
    else:
        matched_aliases = fuzzy_emoji_search(user_text, emoji_aliases, limit=5, threshold=60)

        if matched_aliases:
            emoji_translations = [emoji.emojize(alias, language='alias') for alias in matched_aliases]
            st.markdown(f"### Emoji Suggestions for '{user_text}':\n\n{' '.join(emoji_translations)}")
        else:
            st.write("No close emoji matches found. Try a different keyword.")


def fuzzy_emoji_search(query, aliases, limit=5, threshold=70):
    results = process.extract(query, aliases, limit=limit)
    filtered = [item for item in results if item[1] >= threshold]
    return [alias for alias, score in filtered]

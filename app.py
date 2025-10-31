import streamlit as st
import emoji
import components 


def main():
    st.set_page_config(
        page_icon=":robot_face:",
        layout="wide",
        page_title="Text to Emoji Translator",
        initial_sidebar_state="auto"
    )
    
    components.render_content()

if __name__ == "__main__":
    main()
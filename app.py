import streamlit as st

st.title("Behavioral Science Based Advocate Assistant")
st.write("This tool helps improve social media comments for better persuasiveness using behavioral science.")

user_input = st.text_area("Enter your draft reply to improve or a comment that you want to reply to:")
if st.button("Rewrite it"):
    # For now, we just mock the output
    st.success("Your persuasive version would go here.")
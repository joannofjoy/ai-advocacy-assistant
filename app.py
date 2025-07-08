import streamlit as st

st.title("Behavioral Advocate")
st.write("This tool helps improve social media replies using behavioral science.")

user_input = st.text_area("Enter your reply or comment:")
if st.button("Rewrite it"):
    # For now, we just mock the output
    st.success("Your persuasive version would go here.")
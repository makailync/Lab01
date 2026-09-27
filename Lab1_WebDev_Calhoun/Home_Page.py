import streamlit as st
st.markdown("""
<style>
.stApp {
    background: linear-gradient(to bottom, #FFF3A3, #E78587)
}
section[data-testid="stSidebar"] {
    background-color: #FFF8CC !important;
}
header[data-testid="stHeader"]{
    background-color: #FFF8CC !important;
}
</style>
""", unsafe_allow_html=True)
# Title of App
st.title("Web Development Lab01")

# Assignment Data 
# TODO: Fill out your team number, section, and team members

st.header("CS 1301")
st.subheader("Web Development - Section A")
st.subheader("Makailyn Calhoun")


# Introduction
# TODO: Write a quick description for all of your pages in this lab below, in the form:
#       1. **Page Name**: Description
#       2. **Page Name**: Description
#       3. **Page Name**: Description
#       4. **Page Name**: Description

st.write("""
Welcome to our Streamlit Web Development Lab01 app! You can navigate between the pages using the sidebar to the left. The following pages are:

1. Portfolio: Learn more about the achievements and experience of Scott Pilgrim. 
2. Quiz: Test your Scott Pilgrim knowledge with an interactive quiz!


""")


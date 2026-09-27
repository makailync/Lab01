import streamlit as st
st.markdown("""
<style>
.stApp {
    background: linear-gradient(to bottom, #FFF3A3, #FFCCCB);
    font-family: "Arial Black", sans-serif !important;
}
.stApp h1 {
    font-family: "Arial Black", sans-serif !important;
    letter-spacing: 0.5px;
}
.stApp h2, h3 {
    font-family: "Arial Black", sans-serif !important;
    letter-spacing: 0.5px;
}
</style>
""", unsafe_allow_html=True)
st.title("How Much Do You Know About Scott Pilgrim?")
st.write("Test your knowledge of Scott Pilgrim vs. the World!")

st.header("Question 1")
st.image("Lab1_WebDev_Calhoun/Images/evilexes.jpg")
exes = st.slider( #NEW
    "how many of Ramona's evil exes did Scott Pilgrim defeat?",
    min_value=0,
    max_value=10,
    value=5
)

st.header("Question 2")
st.image("Lab1_WebDev_Calhoun/Images/PilgrimRamonaKnives.jpg")
love = st.selectbox( #NEW
    "Who was Scott Pilgrim's true love?",
    ["Knives", "Ramona"]
)

st.header("Question 3")
st.image("Lab1_WebDev_Calhoun/Images/ramona.jpg")
hair = st.multiselect( #NEW
    "What were all of Ramona's hair colors throughout the movie?",
    ["Pink","Blue", "Green", "Purple","Red"]
)

st.header("Question 4")
band = st.radio( #NEW
    "What band does Scott Pilgrim play for?",
    ["Sex Bob-Omb", "The Clash at Demonhead", "Crash and the Boys", "Sex Omb-Bob"]
)

st.header("Question 5")
instrument = st.selectbox(
    "What instrument does Scott Pilgrim play?",
    ["Guitar", "Bass", "Drums", "Keyboard"]
)

if st.button("Submit Quiz"): #NEW
    score = 0
    if exes == 7:
        score += 1
    if love == "Ramona":
        score += 1
    if set(hair) == {"Pink","Blue","Green"}:
        score += 1
    if band == "Sex Bob-Omb":
        score += 1
    if instrument == "Bass":
        score += 1
    st.write("### Your Results")
    st.write("You got", score,"out of 5 questions correct!")

    if score >= 5:
        st.success("Scott Pilgrim expert!!!")
    else:
        st.info("Scott Pilgrim fan...maybe it's time for another watch!")
    


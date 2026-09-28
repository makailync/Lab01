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

st.title("How Much Do You Know About Scott Pilgrim?")
st.caption("Test your knowledge of Scott Pilgrim vs. the World!")

quiz_tab, info_tab=st.tabs(["🎸Quiz","🎬About Scott Pilgrim"])

with quiz_tab:
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
    st.divider() 
    
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
with info_tab:
    st.header("🎬About Scott Pilgrim vs. the World")
    st.write(
        "Scott Pilgrim vs. the World follows Scott Pilgrim as he battles"
        "Ramona Flowers' seven evil exes.")

    st.write("Learn more about some of the characters below.")


    with st.expander("Learn More About Scott Pilgrim!"):
        st.subheader("Scott Pilgrim")
        st.write("Scott Pilgrim is the main character. In the comics,"
                 "Scott Pilgrim was actually 23, but his age was changed to 22"
                 "for the movie. He's also the bass player for Sex Bob-Omb.")
        st.subheader("Ramona Flowers")
        st.write("Ramona Flowers is Scott's love interest. She always keeps"
                 "Scott at arm's length.")
        st.subheader("Knives Chau")
        st.write("Knives is Scott's former girlfriend. She was 17 in the movie"
                 "and the comics. Scott's age change from 23 to 22 was actually to"
                 "make this age gap seem less jarring. Knives finds herself trying"
                 "to appear more like Ramona after Scott falls for her.")
        


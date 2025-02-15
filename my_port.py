import streamlit as st

st.sidebar.title("Navigation")
page = st.sidebar.radio("GO to", ["Home", "Projects", "Contact"])

if page == "Home":
    st.title("Welcome to my Portfolio!")
    # st.image
    st.write("Hi i am Ahnaf Abdullah Sahir, a data Science Student at UIU.")
    st.write("This portfolio showcases my works")

elif page == "Projects":
    st.title("🤯 My Projects!")

    st.subheader("Monkey Pox detector")
    st.write("this project is an ml pproject to detect monkey pox!")
    st.markdown("[GitHubLink](https://github.com/Ahnaf-Abdullah-Sahir?tab=repositories)")
    st.write("---")


elif page== "Contact":
    st.title("MY contact")
    st.write("Email: bazlur.sohag@gmail.com")
    st.write("[GitHub](https://github.com/Ahnaf-Abdullah-Sahir?tab=repositories)")
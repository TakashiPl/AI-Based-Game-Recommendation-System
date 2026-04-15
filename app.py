import streamlit as st
from utils import get_non_empty_string, get_number
from logic import get_recommendations

st.title("My game recommendation engine")
st.write("Welcome in my AI game recommendation system!")
st.write("It works by using the age and tags you enter to search for games that should be to your liking")

user_age = st.number_input(
    label="Please enter your age:",
    min_value=0,
    max_value=120,
    value=25,
    step=1
)

user_tags = st.text_input("Which tags are you looking for? (e.g. rpg, shooter)")


if st.button("Find games"):
    st.write("Looking for games with tags:", user_tags)
    st.write("Games found:")
    for i,d in enumerate(get_recommendations(user_age,user_tags)):
        st.write(i+1,":", d["name"])
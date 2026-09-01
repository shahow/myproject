import streamlit as st

st.title("Yure Streamlit App")


with st.sidebar:
    st.title("Sidebar")
    st.write("You can add more elements here.")
    st.button("Click me!")

st.bottom.header("關於我")
st.bottom.text("聯絡資訊: email: shahow11@gmail.com")
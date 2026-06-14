import streamlit as st


st.set_page_config(page_title="Multi-Page App", layout="centered")

st.title("Research Projects")
st.sidebar.success("Welcome to the Research Projects page!")

if "my_input" not in st.session_state:
    st.session_state.my_input = ""

my_input = st.text_input("Enter some text", value=st.session_state.my_input)
submit_button = st.button("Submit")
if submit_button:
    st.session_state.my_input = my_input
    st.write("You entered:", st.session_state.my_input)

st.markdown("""
<style>
div[data-testid="stExpander"] {
    border: 2px solid #000;
    border-radius: 0px;
}

div[data-testid="stExpander"] details summary {
    background-color: #f5f5f5;
    font-size: 18px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

with st.expander("Form Section", expanded=False):

    c1, c2, c3 = st.columns(3)

    with c1:
        st.text_input("Field 1")
        st.text_input("Field 2")

    with c2:
        st.text_input("Field 3")
        st.text_input("Field 4")

    with c3:
        st.text_input("Field 5")
        st.text_area("Field 6", height=100)

    st.text_area("Large Content Area", height=150)



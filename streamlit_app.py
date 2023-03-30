import streamlit as st
from st_functions import st_button, load_css
from PIL import Image

st.set_page_config(
    page_title="Streamlit Linktree App",
    page_icon="🧊",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

load_css()


col1, col2, col3 = st.columns(3)
# col2.image(Image.open("images/dp.png"))


st.header("Sergio Vega, Data Analyst | Data Scientist.")

st.info(
    "Developer Advocate, Content Creator and ex-Professor with an interest in Data Science and Bioinformatics"
)

ICON_SIZE = 20

st_button("medium", "https://medium.com/@stbnlen", "Read my Blogs", ICON_SIZE)
st_button(
    "newsletter",
    "https://dataprofessor.org/newsletter/",
    "Follow me on Kaggle",
    ICON_SIZE,
)
st_button(
    "twitter", "https://twitter.com/Hella_Shin3", "Follow me on Twitter", ICON_SIZE
)
st_button(
    "linkedin",
    "https://www.linkedin.com/in/sergiovega96/",
    "Follow me on LinkedIn",
    ICON_SIZE,
)
st_button("github", "https://github.com/stbnlen", "Follow me on GitHub", ICON_SIZE)
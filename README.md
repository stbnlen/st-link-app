# Welcome to Streamlit `links page`

<!-- <img src="images/streamlit-links-page.png" width="350"> -->


> A Streamlit app that you can build for free to store all your personal links that is similar in functionality to that of [Linktr.ee](https://linktr.ee/).

<!-- <img src="images/23F54497-245E-413F-99C7-F3E295E4EA13.png" width="350"> -->

# Demo app

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://chanin.streamlitapp.com/)

# Setting up

Getting your own Streamlit `links page` up and running is really easy, just follow the following 3 steps:

**Step 1**. [Click here](https://github.com/dataprofessor/links/generate) to generate a copy of this repository. Next, name your new repository to anything you'd like except for `your username`.github.io

**Step 2**. Customize the contents of the newly generated `links page` by editing the `streamlit_app.py` file:

```python
import streamlit as st
from st_functions import st_button, load_css
from PIL import Image

load_css()

col1, col2, col3 = st.columns(3)
col2.image(Image.open('images/dp.png'))

st.header('Chanin Nantasenamat, Ph.D.')

st.info('Developer Advocate, Content Creator and ex-Professor with an interest in Data Science and Bioinformatics')

ICONS_SIZE = 20

st_button('youtube', '{your_social}', 'Data Professor YouTube channel', ICONS_SIZE)
st_button('youtube', '{your_social}', 'Coding Professor YouTube channel', ICONS_SIZE)
st_button('medium', '{your_social}', 'Read my Blogs', ICONS_SIZE)
st_button('twitter', '{your_social}', 'Follow me on Twitter', ICONS_SIZE)
st_button('linkedin', '{your_social}', 'Follow me on LinkedIn', ICONS_SIZE)
st_button('newsletter', '{your_social}', 'Sign up for my Newsletter', ICONS_SIZE)
st_button('cup', '{your_social}', 'Buy me a Coffee', ICONS_SIZE)
```

There are 3 key information that you can modify:
1. `st.header(A)` is used for specifying your name in place of **A**.
Example:
```python
st.header('Chanin Nantasenamat, Ph.D.')
```

2. `st.info(B)` is used for speciying a quick description about who you are, what you do, etc. in place of **B**.
Example:
```python
st.info('Developer Advocate, Content Creator and ex-Professor with an interest in Data Science and Bioinformatics')
```

3. `st.button(D, E, F, G)` is a custom function for creating link buttons where **D** represents the icon to display (use `youtube` if the play button is to be displayed), **E** represents the URL, **F** represents the message to display on the clickable button and **G** represents the icon size.
Example:
```python
st_button('youtube', 'https://youtube.com/dataprofessor', 'Data Professor YouTube channel', icon_size)
```

**Step 3**. Deploy to [Streamlit Cloud](https://streamlit.io/cloud). Log-in and click on the **New app** button. Choose the newly generated repo from Steps 1-2. Finally click on the **Deploy!** button. 

After a few moments your new `links page` should be accessible at `https://share.streamlit.io/{your-username}/{newly-created-repo}`

In an upcoming release of Streamlit Cloud, you will be able to customize the URL address to `https://{custom-name--here}.streamlitapp.com/` such as the one that I've created at https://chanin.streamlitapp.com/
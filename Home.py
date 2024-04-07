import streamlit as st
import pandas


def render_app_card(current_row, col):
    with col:
        st.title(current_row['title'])
        st.write(current_row['description'])
        st.image(f"images/{current_row['image']}")
        st.write(f"[Source Code]({current_row['url']})")


st.set_page_config(layout="wide")
col1, col2 = st.columns(2)
with col1:
    st.image("images/photo.png")
with col2:
    st.title("Ardit Sulce")
    content = """Hi, I am Robert! I am a Python programmer. I graduated in 2019 with a Master of Science in 
    Geospatial Technologies from the University of Muenster in Germany with a focus on using Python for remote 
    sensing. I have worked with companies from various countries, such as the Center for Conservation Geography, 
    to map and understand Australian ecosystems, image processing with the Swiss in-Terra, and performing data mining 
    to gain business insights with the Australian Rapid Intelligence. """
    st.info(content)

st.subheader('Below you can find some of the apps I have built in Python. Feel free to contact me!')

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

data = pandas.read_csv('data.csv', sep=';')
for index, row in data.iterrows():
    if int(index) < len(data) / 2:
        render_app_card(row, col3)
    else:
        render_app_card(row, col4)

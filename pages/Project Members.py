import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image

st.set_page_config(
    page_title="Project Members",
    page_icon="👨‍💻",
    layout="wide"
)

st.title(':rainbow[Our Team]')
st.header(':red[Here is our team for this project:]')
st.text('Mikhail Belkin, Helper A, Helper B')
image = Image.open('photo1.jpeg')
image = image.resize((600, 400))
st.image(image)

if st.button('Party Button'):
    st.balloons()
    st.write('🥳🎉 Yeaaaaaaaaaaah :) 🥳🎉')
    
st.subheader('About Us')
st.write('A team of Data Enthusiasts from emlyon business school.')
st.write('Always looking for new opportunities and insights, and an end-of-studies internship starting from July 2024.')
st.write('If you need more information, feel free to contact us !')

st.subheader('Experiences')
experiences = pd.DataFrame({
    'Date': ['2018 - 2020', '2018 - 2020', '2018 - 2020'],
    'Company': ['Apple', 'Meta', 'Google'],
    'Job': ['Data Scientist', 'Data Analyst', 'Business Analyst'],
    'Description': ['A loooooooooooooooooooong description 🚀', 
                    'A looooooooooooooooooooooooooonger description 🚀 🚀', 
                    'Even loooooooooooooooooooooooooooooooooooooonger description 🚀 🚀 🚀']
})
st.dataframe(experiences, hide_index = True)

st.subheader('Our Combined Hardskills')
# Generate a matrix with skills for example
skills = pd.DataFrame({
    'Skills': ['Python', 'SQL', 'Machine Learning', 'Data Visualization', 'Data Engineering', 'Business Intelligence'],
    'Level': [80, 80, 65, 60, 40, 55]
})
fig = px.bar(skills, x='Skills', y='Level', color = 'Level')
st.plotly_chart(fig, use_container_width=True)

st.subheader('Our Hobbies')
st.write('Take a look at the list of our Hobbies')
hobbies = pd.DataFrame({
    'Hobbies': ['Table Tennis', 'Hiking', 'Traveling'],
    'Description': ['Participated in the European Cup - places 50-75th', 
                    'Hiked Mount Everest - Now that is a high place !', 
                    'Visited 50+ countries - Yes, we enjoy traveling and discovering new cultures and people']
})
st.dataframe(hobbies, hide_index = True)

st.subheader('Contact Us')
st.write('Here is our contact information, in case you want to hire us :)')
contact = pd.DataFrame({
    'Email': ['mikhailbelkin00@gmail.com'],
    'LinkedIn': ['https://www.linkedin.com/in/belkinmikhail/'],
    'Address':['1 Famous Place, Paris, 75008 France']
})
st.dataframe(contact, hide_index = True)

st.write(':blue[Please, proceed to next page - "NLP Analysis" to continue.]')





import streamlit as st
from streamlit_lottie import st_lottie
import requests
from PIL import Image

st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#---CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")

#---Assets Loading
lottie_coding = load_lottieurl("https://assets8.lottiefiles.com/private_files/lf30_ajzyv37m.json")
img_contact_form = Image.open("1.jpg")
img_lottie_animation = Image.open("2.png")


#---Header
with st.container():
    st.subheader("Hi, I am Ray :wave:")
    st.title("A Data Scientist")
    st.write("""
    I have 3 years of experience in Retail and 
    highly skilled in Python and SQL, for Data Manipulation, Analysis, and Machine Learning.
    I am a Data-driven Retail Professional with a strong background in building recommendation systems, optimizing pricing,
    and improving supply chain efficiency amongst others.
    Results-driven Data Scientist with a track record of great technical abilities along with great communication and presentation.
    """)
    st.write("[Linkedin >](https://www.linkedin.com/in/raymq)")


#---What I Do
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I Do")
        st.write("##")
        st.write(
            """
            As a data Scientist, This is what I spexialize in
            - Collecting and cleaning data from a variety of sources, such as databases, web scraping, and APIs.
            - Analyzing and exploring data using statistical techniques and visualization tools.
            - Building predictive models and machine learning algorithms to gain insights and make data-driven decisions.
            - Communicating findings and insights to stakeholders through reports, dashboards, and presentations.
            - Collaborating with cross-functional teams, such as product, engineering, and business, to solve problems and drive business outcomes.
            """
        )
    with right_column:
        st_lottie(lottie_coding, height=500, key="coding")

#--- Projects
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        #---Insert Image
        st.image(img_lottie_animation)    
    with text_column:
        st.subheader("Intergrate lottiw in yo apps")
        st.write(
            """
            Learn more do this do that wara wara u know how it goes!
            Also dont forget to do some more of that
            Oh and also, some more.
            """
        )
        #st.markdown("[View Full Project Here >](link)")
with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        #---Insert Image 
        st.image(img_contact_form)  
    with text_column:
        st.subheader("Intergrate lottiw in yo apps")
        st.write(
            """
            Learn more do this do that wara wara u know how it goes!
            Also dont forget to do some more of that
            Oh and also, some more.
            """
        )
        #st.markdown("[View Full Project Here >](link)")

#--- Contact Form
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    contact_form =  """
            <form action="https://formsubmit.co/mrau6x@email.com" method="POST">
            <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your Name" required>
     <input type="email" name="email" placeholder="Your Email" required>
     <textarea name="Message" placeholder="Write To Me Here" required></textarea>
     <button type="submit">Send</button>
            </form>
            """
    left_column,right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
    


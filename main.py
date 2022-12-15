import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image

st.set_page_config(page_title="Lab Project", page_icon=":grin:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style.css")

# Load Assets
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/private_files/lf30_wqypnpu5.json")
img_contact_form = Image.open("images/img1.png")
img_2 = Image.open("images/img2.png")

# Header section
with st.container():
    st.subheader("Hi there, This is Rohit :wave: ")
    st.title("Student at Sreenidhi Institute of Science and Technology")
    st.write("Passionate about building sustainable solutions that impact lives and communities")
    st.write("[I share my technical learnings here >](https://rohitlogs.com)")
    st.write("[Get to know my experiences better here >](https://www.linkedin.com/in/rohit-t-0124a4242/)")

# What I do
with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Work Experience: ")
        st.write("###")
        st.write(
            """
            
            
            Currently Interning at Dr. Reddy's as Junior Software Engineer.

            Previously interned at Sectr Consol Pvt ltd where I worked on developing Smart Helmets for different use cases

            Prior to that I interned at a Company called Numeric HR Solutions as a Web Development Intern 
            
            All along have been an active freelancer which allowed me to work on different projects and sharpen my skills

            """
        )
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")
        # st_lottie(lottie_coding, height=200,key="")

# Projects section 
with st.container():
    st.subheader("Few of my Projects:")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        # To insert a image 
        st.image(img_contact_form)
    with text_column:
        st.subheader("BlogIT - A blogging Website")
        st.write("""
                A Community Driven Blogging website where the user drives the website and content. where you can write blogs
                It can be private or public. It has an authentication, where user cannot write or edit or delete blog unless user signs in.
                We can filter the blogs and watch the blogs of a particular user.
                The user who has written the blog can only edit or delete their blog.
        """)
        st.markdown("[Link to Project Repository](https://github.com/TRohit20/Blogs-Website)")

with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        # To insert a image 
        st.image(img_2)
    with text_column:
        st.subheader("Soldier Fit Factory - A website for commercial Business")
        st.write("""
                this is website I have developed from scratch for the gym I personally workout at.
                The website is intended to serve the gym as a marketing place to showcase what they offer and how it is a better choice and also to get fit.
        """)
        st.markdown("[Link to Project Repository](https://github.com/TRohit20/Soldier-Fit-Factory-Website)")

# Contact Form
with st.container():
    st.write("---")
    st.header("You can get in touch with me here:")
    
    # Documentation
    contact_form = """
            <form action="https://formsubmit.co/vadlamudirohit@gmail.com" method="POST">
            <input type = "hidden" name="_captcha" value ="false">
                <input type="text" name="name" placeholder="Your Name" required>
                <input type="email" name="email" placeholder="Your email" required>
                <textarea name = "message" placeholder = "Your message here" required> </textarea>
                <button type="submit">Send</button>
        </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
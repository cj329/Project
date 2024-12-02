import json
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)
lottie_coding = load_lottiefile("lottiefile.json")    

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("not.txt")

with st.container():
    st.title("MY WEBPAGE")
    st.write(
        """
        Hi, Im am CJ serino BSCpE 1B1
        - Studied at Surigao Del Norte State University
        
        """
    )

with st.container():
    st.write("----")
    left_column, right_column = st.columns(2)    
    with left_column:
       st.write("Get In Touch With Me?")
       st.write("##")
       contact_form = """
      <!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body {font-family: Arial, Helvetica, sans-serif;}
* {box-sizing: border-box;}

input[type=text], select, textarea {
  width: 100%;
  padding: 12px;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
  margin-top: 6px;
  margin-bottom: 16px;
  resize: vertical;
}
input[type=email], select, textarea {
  width: 100%;
  padding: 12px;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
  margin-top: 6px;
  margin-bottom: 16px;
  resize: vertical;
}
 

</style>
</head>
<body>

<h3>Contact Form</h3>

<form action="https://formsubmit.co/cserino@ssct.edu.ph" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
       </form>
    
  </form>
</div>

</body>
</html>

       
        """
       st.markdown(contact_form, unsafe_allow_html=True)
       
       
       
       st.write("Tutorial How To Create a Website Using Python and treamlit:")
       st.write("[YouTube Channel >](https://youtu.be/VqgUkExPvLY?si=fAq6vD_NPI89UXBa)")
    with right_column:
       st.lottie(lottie_coding, height=400, key="coding")

       
     





 
    
import streamlit as st
import requests
from PIL import Image
from io import BytesIO

st.set_page_config(page_title="QR Code Generator", page_icon=":white_medium_square:", layout="centered")

st.title("QR Code Generator")
user_input = st.text_input("Enter the link to generate its QR code:")

if user_input:
    response = requests.get(f"https://us-central1-test-da9ec.cloudfunctions.net/qrcode-python?link={user_input}")

    # Check if the request was successful
    if response.status_code == 200:
        img = Image.open(BytesIO(response.content))        
        st.image(img, caption="Generated QR Code")

        buffer = BytesIO()
        img.save(buffer, format="PNG")
        buffer.seek(0)

        st.download_button(
            label="Download QR Code",
            data=buffer,
            file_name="qr_code.png",
            mime="image/png"
        )
    else:
        st.error("Failed to generate QR Code. Please try again.")

st.markdown("Built by [Gaurav Rasane](https://www.linkedin.com/in/gauravrasane14) | [Sushil Rankhamb](https://www.linkedin.com/in/sushilrankhamb18) | [Vikas Prajapati](https://www.linkedin.com/in/vikas-prajapati-b98ba6256) | [Jagdish Rasal](https://www.linkedin.com/in/) | [Aditya ](https://www.linkedin.com/in/aditya-raskar380a34249) | [Source Code](https://github.com/gauravrasane14/QRGeneratorPBL2)")

import qrcode
import streamlit as st
from PIL import Image

# 1. Generate the QR code
url = "https://www.pib.gov.in/indexd.aspx?reg=3&lang=2"
qr_img = qrcode.make(url)

# 2. Convert the 'qrcode' object into a standard PIL image
# This ensures Streamlit can read the pixel data correctly
standard_img = qr_img.get_image()

# 3. Display it
st.title("PIB News QR Code")
st.image(standard_img, caption="Scan this to visit PIB News")

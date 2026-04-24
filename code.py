import qrcode
import streamlit as st
from PIL import Image

# Title for your web app
st.title("QR Code Generator")

# Variable assigning
url = "https://www.pib.gov.in/indexd.aspx?reg=3&lang=2"

# Process of making QR Code
img = qrcode.make(url)

# Output: Displaying on Streamlit
# We use st.image to render the PIL object directly
st.image(img, caption="Scan this to visit PIB News", use_container_width=True)

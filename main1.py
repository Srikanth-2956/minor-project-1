import streamlit as st
import cv2
import numpy as np
from PIL import Image

def enhance_low_light_image(image):
    # Convert the image from BGR to YCrCb color space
    ycrcb_image = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)

    # Split the image into Y, Cr, and Cb components
    y, cr, cb = cv2.split(ycrcb_image)

    # Equalize the histogram of the Y channel (luminance)
    equalized_y = cv2.equalizeHist(y)

    # Merge the equalized Y channel back with Cr and Cb
    merged_ycrcb = cv2.merge((equalized_y, cr, cb))

    # Convert the image back to BGR color space
    enhanced_image = cv2.cvtColor(merged_ycrcb, cv2.COLOR_YCrCb2BGR)

    return enhanced_image

# Streamlit webpage layout
st.title('Low Light Image Enhancement')
st.write('This tool enhances low light images using histogram equalization.')

# File uploader allows user to add their own image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Convert the file to an opencv image.
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    opencv_image = cv2.imdecode(file_bytes, 1)

    # Display the uploaded image
    st.image(opencv_image, channels="BGR", caption='Uploaded Image', use_column_width=True)
    
    # Enhance the uploaded image
    enhanced_image = enhance_low_light_image(opencv_image)
    
    # Convert back to PIL image to display in Streamlit
    enhanced_image_pil = Image.fromarray(enhanced_image)
    
    # Display the enhanced image
    st.image(enhanced_image_pil, caption='Enhanced Image', use_column_width=True)
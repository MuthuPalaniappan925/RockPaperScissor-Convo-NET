##Importing Packages
import numpy as np
from tensorflow.keras.models import load_model
import streamlit as st
from PIL import Image
import random

##Pre-Processing
def load_preprocessing_image(img: str) -> np.array:
    w,h = 300,300
    img = np.array(Image.open(img).resize((w,h)))
    #Normalize pixel values
    img = img / 255
    img = np.expand_dims(img,axis=0)
    img = np.vstack([img])
    return img

@st.cache_resource
def get_model():
    return load_model('RPS_CNN_vgg_16.h5')

@st.cache_data
def save_image(file) -> None:
    with open(file.name,"wb") as f:
        f.write(file.getbuffer())
    return file.name




st.markdown("<h1 style='text-align: center; color: White;'>Rock-Paper-Scissors Convo-NET</h1>", unsafe_allow_html=True)

page_bg_img = '''
<style>
body {
background-image: url("https://images.unsplash.com/photo-1519681393784-d120267933ba");
background-size: cover;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)

model = get_model()
preds = ['Paper','Rocks','Scissors']
preds_emoji = ['📰','⛰','✂']

##Getting the Pictures
st.info("Indulge in the discreet pleasure of engaging with the DL model of the classic game of Rock Paper Scissors")
cam = st.camera_input('')

if cam:
    st.info("A Code by Muthu Palaniappan M")
    filename = save_image(cam)
    prediction = model.predict(load_preprocessing_image(filename),batch_size = 1)
    if prediction.max() >= 0.8:
        ind = np.argmax(prediction)
        val_pred = preds[ind]
        val_emo_pred = preds_emoji[ind]
        machine_output = random.choice(preds)
        st.info(f"Your Output is {val_emo_pred}")
        st.info(f"Machine Choice: {machine_output}")

        if val_pred == machine_output:
            st.info("Tie")
        elif val_pred == 'Paper' and machine_output == 'Rocks':
            st.success("You Won")
            st.balloons()
        elif val_pred == 'Rocks' and machine_output == 'Scissors':
            st.success("You Won")
            st.balloons()
        elif val_pred == 'Scissors' and machine_output == 'Paper':
            st.success("You Won")
            st.balloons()
        else:
            st.warning("Machine Won Sad Life!!!")

    
    else:
        st.error("Can you please adjust your camera or change your background as it is currently difficult to see clearly?")
        st.info("A Code by Muthu Palaniappan M")
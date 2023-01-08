from models.garbage_model import *
import streamlit as st
import cv2 #veebikaamera lisamiseks

st.title("Garbage identification ")

text_input = st.text_input(
    "Insert iamge URL address",
    )
if text_input:
    answer= predictURL(text_input)
    st.write(f"Item on the picture is: {answer}")

run = st.checkbox('Run webcam')
FRAME_WINDOW = st.image([])
camera = cv2.VideoCapture(0)


if run:
    if st.button('Tuvasta'):
        ret, frame = camera.read()
        FRAME_WINDOW.image(frame)
        cv2.imwrite("photo.png", frame)
        answer = predict()
        st.write(f"Item on the picture is: {answer}")
    while run:
        ret, frame = camera.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        FRAME_WINDOW.image(frame)

    
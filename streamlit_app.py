import altair as alt
import pandas as pd
import numpy as np
import streamlit as st

def process_video(video_path):
    cap = cv2.VideoCapture(video_path)
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    
    output_path = tempfile.mktemp(suffix='.mp4')
    out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        # Dummy prediction: draw a rectangle and put text
        cv2.rectangle(frame, (50, 50), (200, 200), (0, 255, 0), 2)
        cv2.putText(frame, 'Prediction', (60, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
        
        out.write(frame)
    
    cap.release()
    out.release()
    
    return output_path

st.title("Video Upload and Processing")

uploaded_file = st.file_uploader("Upload a video file (mp4 or mov)", type=["mp4", "mov"])

if uploaded_file is not None:
    tfile = tempfile.NamedTemporaryFile(delete=False)
    tfile.write(uploaded_file.read())
    
    st.video(tfile.name)
    
    if st.button("Process Video"):
        output_path = process_video(tfile.name)
        st.video(output_path)
        st.success("Video processed successfully!")

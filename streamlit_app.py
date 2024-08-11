import streamlit as st
import cv2
import tempfile
import os

def process_video(video_path):
    video = cv2.VideoCapture(video_path)
    frames = []
    while video.isOpened():
        success, frame = video.read()
        if not success:
            break
        frames.append(frame)
    video.release()
    return frames

st.title("YouTube Video and Local Video Processor")

# Input YouTube URL
youtube_url = st.text_input("Enter YouTube video URL")

# Upload local video file
uploaded_file = st.file_uploader("Upload a video file (mp4 or mov)", type=["mp4", "mov"])

if uploaded_file is not None:
    # Save uploaded file to a temporary location
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_file_path = tmp_file.name

    # Process the video
    frames = process_video(tmp_file_path)
    st.write(f"Processed {len(frames)} frames from the uploaded video.")

    # Display the first frame as an example
    if frames:
        st.image(frames[0], channels="BGR", caption="First frame of the video")

    # Clean up temporary file
    os.remove(tmp_file_path)

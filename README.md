# Movie and TV Show Search & Video Tools

This is a Streamlit application that provides tools for searching movie and TV show information and utilities for video manipulation.

## Features

### 1. Search Movie or TV Show Titles
- Allows users to search for titles within a dataset.
- Displays matching results.

### 2. Search Subtitles with AI Transcripts
- Enables searching through video subtitles or AI-generated transcripts.
- Shows results based on query matches in the transcript data.

### 3. Extend Video Length (AI-Powered - Placeholder)
This feature allows users to upload a video and specify a duration by which to extend it. Currently, it uses a placeholder function that simulates the extension process.

**How to use:**
1.  Navigate to the "Extend Video Length" section in the application.
2.  Click on "Upload a video" to select a video file from your computer (supported formats: .mp4, .mov, .avi, .mkv).
3.  Set the number of seconds you wish to extend the video by using the "Seconds to extend by" input field.
4.  Click the "Extend Video" button.
5.  The application will process the video (currently simulating this) and display the "extended" version.

## Running the Application
This is a Streamlit application. To run it, you typically use:
```bash
streamlit run streamlit_app.py
```
Ensure you have Streamlit and other dependencies (like pandas, opencv-python) installed.

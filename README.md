# Movie and TV Show Search & Video Tools

This is a Streamlit application that provides tools for searching movie and TV show information and utilities for video manipulation.

## Features

### 1. Search Movie or TV Show Titles
- Allows users to search for titles within a dataset.
- Displays matching results.

### 2. Search Subtitles with AI Transcripts
- Enables searching through video subtitles or AI-generated transcripts.
- Shows results based on query matches in the transcript data.

### 3. Extend Video Length (Command-Line Tool)
This feature allows users to extend a video by a specified duration using a command-line tool. Currently, it uses a placeholder function that simulates the extension process by copying the video.

**How to use:**
The tool is run from the command line using `python extend_video_cli.py`.

**Arguments:**
*   `--input_path PATH`: (Required) The full path to the source video file you want to extend.
*   `--duration SECONDS`: (Required) The number of seconds by which to extend the video.
*   `--output_path PATH`: (Optional) The full path where the extended video file should be saved. If not provided, the extended video will be saved in a temporary directory, and its path will be printed to the console.

**Example Usage:**
```bash
python extend_video_cli.py --input_path /path/to/your/video.mp4 --duration 10
```
To specify an output location:
```bash
python extend_video_cli.py --input_path /path/to/your/video.mp4 --duration 10 --output_path /path/to/save/extended_video.mp4
```

## Running the Application
This is a Streamlit application. To run it, you typically use:
```bash
streamlit run streamlit_app.py
```
Ensure you have Streamlit and other dependencies (like pandas, opencv-python) installed.

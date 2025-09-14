#!/bin/bash

# Check for FFmpeg
echo "Attempting to check FFmpeg version..."
if ffmpeg -version 2>/dev/null; then
    echo "FFmpeg is already installed."
else
    echo "FFmpeg not found. Attempting to install..."
    # Attempt to install FFmpeg - this might vary based on the OS
    # Trying common package managers
    if sudo apt-get update && sudo apt-get install -y ffmpeg; then
        echo "FFmpeg installed successfully via apt-get."
    elif sudo yum install -y ffmpeg; then
        echo "FFmpeg installed successfully via yum."
    else
        echo "Could not install FFmpeg. Manual installation might be required."
        # exit 1 # Optionally exit if FFmpeg is critical and cannot be installed
    fi
fi

# Check for OpenCV
echo "Attempting to check OpenCV version..."
if python -c "import cv2; print(cv2.__version__)"; then
    echo "OpenCV (cv2) is already installed."
else
    echo "OpenCV (cv2) not found. Attempting to install..."
    pip install opencv-python
    if python -c "import cv2; print(cv2.__version__)"; then
        echo "OpenCV (cv2) installed successfully via pip."
    else
        echo "Could not install OpenCV (cv2). Manual installation might be required."
        # exit 1 # Optionally exit if OpenCV is critical
    fi
fi

echo "Environment setup check complete."

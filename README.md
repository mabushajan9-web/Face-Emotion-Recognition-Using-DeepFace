Live Emotion Recognition 🎭

This project uses DeepFace and OpenCV to perform real-time emotion recognition through a webcam.
It captures frames from the webcam, detects faces, analyzes emotions, and displays the dominant emotion on screen.

Features

Real-time emotion recognition using DeepFace

Supports multiple emotions such as happy, sad, angry, fear, surprise, neutral, and disgust

Draws bounding boxes around detected faces

Displays dominant emotion above each face

Press 'q' or 'Esc' to quit the application

Requirements

Python 3.7+

OpenCV

DeepFace

TensorFlow / Keras (installed automatically with DeepFace)

Installation

Clone this repository:
git clone https://github.com/yourusername/live-emotion-recognition.git

Navigate to the project folder:
cd live-emotion-recognition

Install dependencies:
pip install opencv-python deepface

Usage

Run the script:
python emotion_recognition.py

The webcam window will open.

Detected faces will be highlighted with a green rectangle.

The predicted dominant emotion will appear above the face.

Press 'q' or 'Esc' to exit.

Code Flow

Capture video frames using OpenCV

Use DeepFace to analyze each frame for emotions

Handle cases where no face is detected

Overlay bounding box and emotion text on each detected face

Display results in real-time

Author

Name: DANCY MABUSHA D
Email: mabushajan9@gmail.com

License

This project is licensed under the MIT License – feel free to use and modify.

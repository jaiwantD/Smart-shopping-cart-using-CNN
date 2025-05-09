# Intelligent Shopping Cart System Using Convolutional Neural Networks

## Project Overview
The Smart Shopping Cart System is designed to automate the billing process by utilizing object detection to identify products placed inside a cart. The system uses a camera to detect items, classifies them using TensorFlow, and handles backend communication through Flask. This version of the project includes image capture using a camera, product classification, and a web-based billing system integrated with Firebase for data storage.

## Features
- **Object Detection**: TensorFlow is used to detect and classify products placed in the shopping cart.
- **Automated Billing**: Products are automatically billed when detected in the cart.
- **Image Storage**: Firebase is used to store images and retrieve classification results.
- **Web Interface**: A simple interface allows users to upload images and view billing information.

## Tech Stack

<img src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" alt="Python" width="100" height="100"><img src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Tensorflow_logo.svg" alt="TensorFlow" width="100" height="100">
<img src="https://upload.wikimedia.org/wikipedia/commons/3/3c/Flask_logo.svg" alt="Flask" width="200" height="100">
<img src="https://firebase.google.com/images/brand-guidelines/logo-vertical.png" alt="Firebase" width="100" height="100">

- **Backend**: Built with Flask to handle image uploads and process them using TensorFlow for product classification.
- **Image Upload**: A web page (`index.html`) allows users to upload product images to Firebase.
- **Billing**: A separate page (`billing.html`) retrieves images from Firebase, classifies them, and displays billing details.
- **Firebase Integration**: Images are stored in Firebase, and classification data is fetched for billing.
- **New User Handling**: Clicking 'New User' on the billing page deletes all stored data from Firebase to prepare for a new session.

## Future Work
- **ESP32 Camera Integration**: The system will soon be integrated with an ESP32 camera for real-time image capture.
- **Flutter Mobile App**: A Flutter app will be developed to allow direct image capture and automatic billing via a mobile interface.

## Prerequisites
- Python 3.x
- TensorFlow
- Flask
- Firebase

## How to Run the Project

1. **Clone the repository**:
   ```bash
   git clone https://github.com/jaiwantD/autonomous-billing-system--ccp

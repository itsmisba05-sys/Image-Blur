Image Blurring Automation
This Python project automatically fetches images from a specified GitHub subdirectory, applies various blurring techniques (Gaussian, Average, Median, and Bilateral), and saves the processed images locally.

Features
Automatically downloads images directly from a GitHub repository subfolder
Supports multiple blur filters:
Gaussian Blur
Average Blur
Median Blur
Bilateral Filter
Saves all processed images in a separate folder for easy access

Requirements
Python 3.x
OpenCV (cv2)
Requests

Install dependencies:
pip install opencv-python requests

Usage
Edit the script with your GitHub username, repository name, and subdirectory path.
Run the script and choose your preferred blur type (1–4).
Blurred images will be saved in the blurred/ folder.

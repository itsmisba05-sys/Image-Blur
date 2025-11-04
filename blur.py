import os
import cv2
import requests

# 🔹 Step 1: Your GitHub repo details
# Example: "https://github.com/username/repo-name"
GITHUB_USER = "your-username"
REPO_NAME = "your-repo"
SUBDIR_PATH = "images"   # folder inside the repo containing your images

# 🔹 Step 2: GitHub API endpoint for the folder
API_URL = f"https://api.github.com/repos/{GITHUB_USER}/{REPO_NAME}/contents/{SUBDIR_PATH}"

# 🔹 Step 3: Local folders
input_folder = "images"
output_folder = "blurred"
os.makedirs(input_folder, exist_ok=True)
os.makedirs(output_folder, exist_ok=True)

# 🔹 Step 4: Fetch file list from GitHub API
response = requests.get(API_URL)
if response.status_code != 200:
    raise Exception(f"Failed to fetch directory listing: {response.status_code}")

files = response.json()

# Filter only image files
supported_formats = ('.jpg', '.jpeg', '.png')
image_files = [file for file in files if file["name"].lower().endswith(supported_formats)]

print(f"📂 Found {len(image_files)} image(s) in GitHub subdirectory '{SUBDIR_PATH}'")

# 🔹 Step 5: Download all images
for file in image_files:
    image_url = file["download_url"]
    image_name = file["name"]
    image_path = os.path.join(input_folder, image_name)

    img_data = requests.get(image_url).content
    with open(image_path, "wb") as handler:
        handler.write(img_data)
    print(f"✅ Downloaded: {image_name}")

# 🔹 Step 6: Ask user for blur type
print("\nSelect blur type:")
print("1. Gaussian Blur")
print("2. Average Blur")
print("3. Median Blur")
print("4. Bilateral Filter")

choice = int(input("Enter your choice (1–4): "))

# 🔹 Step 7: Process and blur all images
for image_name in os.listdir(input_folder):
    if not image_name.lower().endswith(supported_formats):
        continue

    image_path = os.path.join(input_folder, image_name)
    image = cv2.imread(image_path)

    if image is None:
        print(f"⚠️ Skipping {image_name} (unreadable)")
        continue

    if choice == 1:
        blurred = cv2.GaussianBlur(image, (15, 15), 0)
    elif choice == 2:
        blurred = cv2.blur(image, (15, 15))
    elif choice == 3:
        blurred = cv2.medianBlur(image, 15)
    elif choice == 4:
        blurred = cv2.bilateralFilter(image, 15, 75, 75)
    else:
        print("❌ Invalid choice — skipping.")
        continue

    output_path = os.path.join(output_folder, f"blurred_{image_name}")
    cv2.imwrite(output_path, blurred)
    print(f"💾 Saved: {output_path}")

print("\n✅ Done! All blurred images are saved in the 'blurred' folder.")

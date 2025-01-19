# Necessary imports for the project
import os
import time
import shutil
import subprocess

# Define paths
camera_folder = "./camera_captured_images"  # Path where the camera saves pictures
uploaded_folder = "./uploaded_images"      # Path to move uploaded pictures
upload_url = "https://projects.benax.rw/f/o/r/e/a/c/h/p/r/o/j/e/c/t/s/4e8d42b66f70fa9d39741a93ed0356c/iot_testing_202501/upload.php"

# Ensure the 'uploaded' folder exists
os.makedirs(uploaded_folder, exist_ok=True)

def monitor_and_upload():
    while True:
        # List all files in the camera folder
        files = [f for f in os.listdir(camera_folder) if os.path.isfile(os.path.join(camera_folder, f))]
        
        for file in files:
            file_path = os.path.join(camera_folder, file)
            
            # Upload the file using curl
            try:
                print(f"Uploading {file}...")
                result = subprocess.run([
                    "curl", "-X", "POST", "-F", f"imageFile=@{file_path}", upload_url
                ], capture_output=True, text=True)

                if result.returncode == 0:
                    print(f"Successfully uploaded {file}.")
                    # Move the file to the uploaded folder
                    shutil.move(file_path, os.path.join(uploaded_folder, file))
                else:
                    print(f"Failed to upload {file}: {result.stderr}")
            except Exception as e:
                print(f"Error uploading {file}: {e}")

        # Wait for 30 seconds before checking again
        time.sleep(30)

if __name__ == "__main__":
    print("Starting the folder monitoring script...")
    monitor_and_upload()

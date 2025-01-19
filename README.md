# Folder Monitor and Image Uploader

## Overview
This project is a Python script designed to automate the process of monitoring a folder for newly captured images, uploading them to a specified URL, and organizing the files post-upload. The script ensures that all captured images are uploaded automatically and prevents redundancy by moving uploaded files to a designated folder.

## Features
- Monitors a specified folder for new images.
- Uploads images to a server using the `curl` command.
- Moves successfully uploaded images to an "uploaded" folder for organization.
- Runs continuously, checking for new files every 30 seconds.

## Requirements
- Python 3.x
- `curl` command-line tool

## Setup
1. Clone this repository:
   ```bash
   git clone <repository_url>
   cd <repository_name>
   ```
2. Ensure the required folders exist:
   - A folder where the camera saves pictures (e.g., `./camera_folder`).
   - A folder to store uploaded pictures (e.g., `./uploaded`).

   If these folders do not exist, the script will attempt to create them.

3. Update the script with the correct folder paths:
   - `camera_folder`: Path where images are saved.
   - `uploaded_folder`: Path to move uploaded images.
   - `upload_url`: The server URL for uploading images.

## Usage
1. Run the script:
   ```bash
   python3 upload_script.py
   ```
2. The script will:
   - Continuously monitor the specified folder for new images.
   - Automatically upload each image to the server using the `curl` command.
   - Move successfully uploaded images to the `uploaded` folder.

## Example `curl` Command
The script uses the following `curl` command format for uploading images:
```bash
curl -X POST -F imageFile=@/path/to/your/image.jpg <upload_url>
```

## Deliverables
- The Python script should be pushed to a GitHub repository.
- Submit the GitHub repository link using the provided Google Form.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author
- **Your Name**  
  Add your details here, such as your GitHub profile or email.

## Acknowledgments
- Special thanks to the team for the assignment.

## Notes
- Ensure `curl` is installed and accessible from your system's command line.
- The script is configured to check for new files every 30 seconds; you can modify this interval in the script if needed.
- Handle errors appropriately if images fail to upload.

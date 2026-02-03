import os
import shutil
from pathlib import Path
from tkinter import Tk
from tkinter.filedialog import askdirectory

# Choosing the directory path
source_dir = Path(askdirectory(title="Select a Folder"))

# Listing out all the files
files = [f for f in os.listdir(source_dir) if os.path.isfile(os.path.join(source_dir, f))]
print("\n".join(files))

# Printing the extension of the file
for file in files:
    filename, file_extension = os.path.splitext(file)
    print(f"File extension: {file_extension}")

# Creating new folders for file sorting.
folders = ["Images", "PDFs", "Documents", "Videos", "Music", "Audio", "Books", "Other"]
for folder in folders:
    folder_path = source_dir / folder
    if folder_path.exists():
        print(f"{folder} folder already exists.")
    else:
        folder_path.mkdir(parents=True, exist_ok=True)
        print(f"{folder} folder created successfully!")        

# Moving files to respective folders
extension_folder_map = {
    '.jpg': 'Images',
    '.png': 'Images',
    '.pdf': 'PDFs',
    '.txt': 'Documents',
    '.docx': 'Documents',
    '.mp4': 'Videos',
    '.mkv': 'Videos',
    '.epub': 'Books',
    '.azw3': 'Books',
    '.mp3': 'Audio',
    '.zip': 'Other',
    '.ipynb': 'Other',
    '.csv': 'Other'
}

for file_path in source_dir.iterdir():
    if file_path.is_file():
        ext = file_path.suffix.lower() 
        if ext in extension_folder_map:
            target_dir = Path(f"{source_dir}/{extension_folder_map[ext]}")
            try:
                shutil.move(str(file_path), target_dir / file_path.name)
                print(f"Moved: {file_path.name} to {target_dir}")
            except Exception as e:
                print(f"Error moving {file_path.name: {e}}")

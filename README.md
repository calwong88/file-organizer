# File Organizer v1.0

A simple and intuitive Python tool that automatically organizes files in a directory by sorting them into categorized folders based on their file extensions.

## 📋 Description

File Organizer helps you declutter directories by automatically moving files into organized folders. It features a user-friendly GUI for folder selection and supports common file types including images, documents, videos, audio files, PDFs, and books.

## ✨ Features

- **GUI Folder Selection**: Easy-to-use dialog for selecting the directory to organize
- **Automatic Categorization**: Sorts files into predefined categories
- **Multiple File Type Support**: Handles images, PDFs, documents, videos, audio, books, and more
- **Smart Folder Creation**: Automatically creates category folders if they don't exist
- **Safe File Handling**: Includes error handling to prevent data loss

## 📁 Supported File Categories

| Category | Extensions |
|----------|-----------|
| **Images** | `.jpg`, `.png` |
| **PDFs** | `.pdf` |
| **Documents** | `.txt`, `.docx` |
| **Videos** | `.mp4`, `.mkv` |
| **Audio** | `.mp3` |
| **Books** | `.epub`, `.azw3` |
| **Other** | `.zip`, `.ipynb`, `.csv` |

## 🚀 Installation

### Prerequisites

- Python 3.6 or higher
- tkinter (usually comes with Python)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/file-organizer.git
cd file-organizer
```

2. No additional dependencies required! The script uses only Python standard library modules.

## 💻 Usage

Simply run the script:

```bash
python file_organizer_1_0.py
```

A dialog window will appear asking you to select the folder you want to organize. Once selected, the script will:

1. List all files in the directory
2. Display file extensions
3. Create necessary category folders
4. Move files to their respective folders
5. Display progress and any errors

### Example

```bash
python file_organizer_1_0.py
```

Then select your Downloads folder or any other directory you want to organize.

## 🛠️ How It Works

1. **Folder Selection**: Uses tkinter's file dialog to select target directory
2. **File Discovery**: Lists all files in the selected directory
3. **Folder Creation**: Creates category folders (Images, PDFs, Documents, Videos, Music, Audio, Books, Other)
4. **File Movement**: Moves each file to its appropriate folder based on extension mapping
5. **Error Handling**: Catches and reports any errors during file operations

## 📝 Customization

You can easily customize the file categories by modifying the `extension_folder_map` dictionary in the script:

```python
extension_folder_map = {
    '.jpg': 'Images',
    '.png': 'Images',
    '.pdf': 'PDFs',
    # Add your own mappings here
}
```

You can also add more folder categories by editing the `folders` list:

```python
folders = ["Images", "PDFs", "Documents", "Videos", "Music", "Audio", "Books", "Other"]
```

## ⚠️ Important Notes

- **Backup Your Files**: Always backup important files before running the organizer
- **Existing Folders**: If category folders already exist, the script will use them
- **File Conflicts**: If a file with the same name exists in the destination folder, an error will be reported
- **Subfolders**: The script only processes files in the root of the selected directory, not subfolders

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🐛 Known Issues

- Does not handle duplicate filenames in destination folders
- Does not process files in subdirectories
- Limited file extension support (easily expandable)

## 🔮 Future Enhancements

- [ ] Add duplicate file handling
- [ ] Recursive directory processing option
- [ ] Undo functionality
- [ ] More file type support
- [ ] Command-line interface option
- [ ] Configuration file for custom mappings
- [ ] Dry-run mode to preview changes

## 👤 Author

Calvin Wong - [@calwong88](https://github.com/calwong88)

## 🙏 Acknowledgments

- Built with Python's standard library
- Uses tkinter for GUI components

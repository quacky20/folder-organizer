# 📁 Folder Organizer

A modern desktop application built with Python and CustomTkinter that automatically organizes files into categorized folders based on their file types.

## ✨ Features

- **Automatic File Categorization**: Organizes files into Images, Videos, Documents, and Others folders
- **Exception List**: Select files to exclude from organization
- **Custom Directory Selection**: Choose both source and destination folders
- **Undo Functionality**: Revert changes with a single click
- **Modern UI**: Built with CustomTkinter for a sleek, modern interface
- **Real-time Updates**: Refresh file list to see current directory contents
- **Status Feedback**: Visual indicators for successful operations and errors

## 📋 Supported File Types

### Images
`jpg`, `jpeg`, `png`, `gif`, `psd`, `svg`

### Videos
`mp4`, `mov`, `avi`, `wmv`, `mkv`, `webm`, `flv`, `mpg`, `mpeg`

### Documents
`pdf`, `doc`, `docx`, `txt`, `ppt`, `pptx`, `xls`, `xlsx`

### Others
All other file types (excluding `.lnk` shortcuts which are ignored)

## 🚀 Installation

### Prerequisites
- Python 3.10 or higher (for `match` statement support)
- Windows OS (due to `.ico` icon file)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/quacky20/folder-organizer.git
cd Folder-Organizer
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python main.py
```

## 📖 Usage

1. **Choose Source Directory**: Click "Choose directory" to select the folder you want to organize
2. **Choose Destination Directory**: Click "Choose save directory" to select where organized files should be saved
3. **Select Exceptions** (Optional): Select files from the list that you want to exclude from organization
4. **Clean**: Click "Clean" to organize your files
5. **Undo** (Optional): If needed, click "Undo" to revert the organization
6. **Refresh**: Click the refresh button (↻) to update the file list

## 🗂️ Project Structure

```
Folder-Organizer/
│
├── main.py              # Application entry point
├── window.py            # GUI implementation (CustomTkinter)
├── utils.py             # Core file organization logic
├── requirements.txt     # Python dependencies
├── icon.ico            # Application icon
└── README.md           # Documentation
```

## 🛠️ Technical Details

### Architecture
- **Frontend**: CustomTkinter for modern GUI
- **Backend**: Python standard library (`os`, `shutil`)
- **Pattern**: Separation of concerns (GUI logic in `window.py`, file operations in `utils.py`)

### Color Scheme
- Background: `#061E29`
- Primary: `#1D546D`
- Hover: `#387997`
- Secondary: `#5F9598`
- Text: `#F3F4F4`

### Key Components
- `Window`: Main application class inheriting from `ctk.CTk`
- `createFolders()`: Creates category folders in destination
- `moveFiles()`: Moves files based on extension matching
- `undo()`: Reverts file organization
- `organize()`: Main orchestration function

## ⚠️ Important Notes

- **Backup Your Files**: Always backup important files before organizing
- **Duplicate Names**: If files with the same name exist in destination, operation may fail
- **Permissions**: Ensure you have read/write permissions for both source and destination directories
- **`.lnk` Files**: Shortcut files are automatically ignored

## 🐛 Known Issues

- No validation for empty directories
- No support for nested folder organization

## 🔮 Future Enhancements

- [ ] Logging system for detailed error tracking
- [ ] Configuration file for custom file categories
- [ ] Support for custom file type rules
- [ ] Batch file (.bat) for easy execution
- [ ] Logs viewer in GUI
- [ ] Progress bar for large file operations
- [ ] Cross-platform support (Linux, macOS)
- [ ] Drag-and-drop file support
- [ ] Settings persistence
- [ ] Duplicate file handling

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

**Note**: This application is designed for personal use. Always review files before organizing and keep backups of important data.

Created with ❤️
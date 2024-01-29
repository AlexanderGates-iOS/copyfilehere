import tkinter as tk
from tkinter import filedialog
import shutil
import os


def copy_file():
    # Specify the file path or use a file dialog to select a file
    file_path = filedialog.askopenfilename()
    # Specify the destination directory
    destination = "."
    # Copy the file to the destination
    shutil.copy(file_path, destination)


def copy_folder():
    # Specify the folder path or use a file dialog to select a folder
    folder_path = filedialog.askdirectory()
    if folder_path:
        # Extract the folder name from the selected path
        folder_name = os.path.basename(folder_path)
        # Specify the destination directory (same location as the script)
        destination = os.path.join(".", folder_name)
        # Copy the folder to the destination
        shutil.copytree(folder_path, destination, dirs_exist_ok=True)


# Create the main window
root = tk.Tk()
root.title("File and Folder Copier")
root.geometry("300x150")

# Create a frame to hold the buttons
frame = tk.Frame(root)
frame.pack(expand=True, fill=tk.BOTH)

# Create a button and assign the extract_file function
extract_button = tk.Button(frame, text="Copy File", command=copy_file)
extract_button.pack(expand=True)

# Create a button and assign the copy_folder function
copy_folder_button = tk.Button(frame, text="Copy Folder", command=copy_folder)
copy_folder_button.pack(expand=True)

# Run the application
root.mainloop()

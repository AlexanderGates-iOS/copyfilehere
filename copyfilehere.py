import tkinter as tk
from tkinter import filedialog
import shutil


def copy_file():
    # Specify the file path or use a file dialog to select a file
    file_path = filedialog.askopenfilename()

    # Specify the destination directory
    destination = "."

    # Copy the file to the destination
    shutil.copy(file_path, destination)


# Create the main window
root = tk.Tk()
root.title("Copy File Here")

# Set the window size (width x height)
root.geometry("250x100")

# Create a frame to hold the button
frame = tk.Frame(root)
frame.pack(expand=True, fill=tk.BOTH)

# Create a button and assign the extract_file function
extract_button = tk.Button(frame, text="Copy File", command=copy_file)
extract_button.pack(expand=True)

# Run the application
root.mainloop()

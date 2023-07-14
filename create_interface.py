# Import necessary modules
import tkinter as tk
from tkinter import filedialog

# Create the main window
root = tk.Tk()
root.title('Pokemon TCG Decklist Importer')

# Create the file dialog
file_dialog = filedialog.askopenfilename(title='Select Decklist File', filetypes=[('Text Files', '*.txt')])

# Create the label for the file path
file_path_label = tk.Label(root, text='Selected File: ' + file_dialog)
file_path_label.pack()

# Run the main loop
root.mainloop()

import os
from tkinter import filedialog, ttk
import tkinter as tk

# Modern color scheme
COLORS = {
    'bg': '#2E3440',  # Dark background
    'secondary': '#3B4252',  # Slightly lighter background
    'accent': '#88C0D0',  # Blue accent
    'text': '#ECEFF4',  # Light text
    'input_bg': '#4C566A'  # Input background
}

# Updated font configurations
FONTS = {
    'main': ('Helvetica', 13),
    'header': ('Helvetica', 15, 'bold'),
    'input': ('Helvetica', 16)
}

def close_window(root, e):
    root.destroy()

# set the diminsions of the app and center it on the screen
def setup_window(root):

    # Set window size
    root_width = 800
    root_height = 600
    root.geometry(f'{root_width}x{root_height}')
    root.minsize(root_width, root_height)

    # Get screen dimensions
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calculate center position
    x = (screen_width - root_width) // 2
    y = (screen_height - root_height) // 2

    # Set window position to center of screen
    root.geometry(f'+{x}+{y}')
    root.title("Testing Test")

root = tk.Tk()
setup_window(root)

# Create and configure the custom frame style
style = ttk.Style()
style.configure(
    'Border.TFrame',
    background='#2E3440',
    padding=20,
    borderwidth=20,
    relief='solid'
)

# Main outer frame
frame = ttk.Frame(root, style='Border.TFrame')
frame.grid(row=0, column=0, sticky='nsew')

# Inner frame
style.configure('Inner.Border.TFrame', background='#FFFFFF')
inner_frame = ttk.Frame(frame, style='Inner.Border.TFrame')
inner_frame.grid(row=0, column=0, sticky='nsew', padx=20, pady=20)

# Configure grid weights for both frames
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
frame.grid_rowconfigure(0, weight=1)
frame.grid_columnconfigure(0, weight=1)

# Closes the application window when the 'q' key is pressed
root.bind('<q>', lambda e: close_window(root, e))
root.mainloop()

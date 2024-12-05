import os
from tkinter import filedialog, ttk
import tkinter as tk

# Modern color scheme
COLORS = {
    'bg': 'gray',  # Dark background
    # 'bg': '#2E3440',  # Dark background
    'secondary': '#3B4252',  # Slightly lighter background
    'accent': '#88C0D0',  # Blue accent
    'text': '#ECEFF4',  # Light text
    'input_bg': '#4C566A',  # Input background
    'button_text': '#2E3440',  # Input background

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

    # Set the background color of the root window
    root.configure(bg=COLORS['bg'])

# Handles the style for the <choose file> button
def create_styled_button(parent, text, command):
    return tk.Button(
        parent,
        text=text,
        command=command,
        bg=COLORS['accent'],
        fg=COLORS['button_text'],
        font=FONTS['main'],
        relief='flat',
        cursor='hand2'
    )

# TODO: this is a placeholder for the browse button
def setup_browse_button():
    print("browse_button called")

# Controls styling for the label of the currently selected file and the browse file button
def setup_browse_file_frame():

    browse_file_frame = ttk.Frame(main_frame, style='Border.TFrame')
    browse_file_frame.grid(row=0, column=0, sticky='nsew')
    browse_file_frame.rowconfigure(0, weight=1)
    browse_file_frame.columnconfigure(0, weight=1)
    browse_file_frame.columnconfigure(1, weight=1)

    current_selected_file_frame = ttk.Frame(browse_file_frame, style='Border.TFrame')
    current_selected_file_frame.grid(row=0, column=0, sticky='nsew')
    current_selected_file_label = tk.Label(
        current_selected_file_frame,
        text="Label 0",
        bg=COLORS['bg'],
        fg=COLORS['text'],
        font=FONTS['header']
    )
    current_selected_file_label.pack(expand=True)

    browse_button_frame = ttk.Frame(browse_file_frame, style='Border.TFrame')
    browse_button_frame.grid(row=0, column=1, sticky='nsew')
    browse_button = create_styled_button(browse_button_frame, "Choose File", setup_browse_button)
    browse_button.pack(expand=True, side='right')

# Controls styling for the input area
def setup_user_input_frame():

    user_input_frame = ttk.Frame(main_frame, style='Border.TFrame')
    user_input_frame.grid(row=1, column=0, sticky='nsew')

    user_input_label = tk.Label(
        user_input_frame,
        text="Enter Chinese Text",
        bg=COLORS['bg'],
        fg=COLORS['text'],
        font=FONTS['header']
    )
    user_input_label.pack(expand=True)

    # TODO this label should be changed to a palce for user input
    user_input_area = tk.Label(
        user_input_frame,
        text="This is the placeholder for the input area",
        bg=COLORS['bg'],
        fg=COLORS['text'],
        font=FONTS['header']
    )
    user_input_area.pack(expand=True)

def setup_chinese_sentence_frame():

    chinese_sentence_frame = ttk.Frame(main_frame, style='Border.TFrame')
    chinese_sentence_frame.grid(row=2, column=0, sticky='nsew')

    chinese_sentence_label = tk.Label(
        chinese_sentence_frame,
        text="Chinese",
        bg=COLORS['bg'],
        fg=COLORS['text'],
        font=FONTS['header']
    )
    chinese_sentence_label.pack(expand=True)

    original_chinese_sentence = tk.Label(
        chinese_sentence_frame,
        text="This is the placeholder for the input area",
        bg=COLORS['bg'],
        fg=COLORS['text'],
        font=FONTS['header']
    )
    original_chinese_sentence.pack(expand=True)

def setup_pinyin_sentence_frame():
    pinyin_sentence_frame = ttk.Frame(main_frame, style='Border.TFrame')
    pinyin_sentence_frame.grid(row=3, column=0, sticky='nsew')

    pinyin_sentence_label = tk.Label(
        pinyin_sentence_frame,
        text="Pinyin",
        bg=COLORS['bg'],
        fg=COLORS['text'],
        font=FONTS['header']
    )
    pinyin_sentence_label.pack(expand=True)

    translated_pinyin_sentence = tk.Label(
        pinyin_sentence_frame,
        text="This is the placeholder for the input area",
        bg=COLORS['bg'],
        fg=COLORS['text'],
        font=FONTS['header']
    )
    translated_pinyin_sentence.pack(expand=True)

root = tk.Tk()
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
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
main_frame = ttk.Frame(root, style='Border.TFrame')
main_frame.grid(row=0, column=0, sticky='nsew', padx=20, pady=20)

main_frame.rowconfigure(0, weight=1)
main_frame.rowconfigure(1, weight=1)
main_frame.rowconfigure(2, weight=1)
main_frame.rowconfigure(3, weight=1)
main_frame.columnconfigure(0, weight=1)
main_frame.columnconfigure(1, weight=1)

setup_browse_file_frame()
setup_user_input_frame()
setup_chinese_sentence_frame()
setup_pinyin_sentence_frame()

# TODO finish set up of recently_opened_files_frame
# recently_opened_files_frame = ttk.Frame(main_frame, style='Border.TFrame')
# recently_opened_files_frame.rowconfigure(0, weight=1)
# recently_opened_files_frame.columnconfigure(0, weight=1)

# Closes the application window when the 'q' key is pressed
root.bind('<q>', lambda e: close_window(root, e))
root.mainloop()

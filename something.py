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

def browse_button():
    print("browse_button called")

def setup_browse_file_frame():

    browse_file_frame = ttk.Frame(main_frame, style='Border.TFrame')
    browse_file_frame.grid(row=0, column=0, sticky='nsew')
    browse_file_frame.rowconfigure(0, weight=1)
    browse_file_frame.columnconfigure(0, weight=1)
    browse_file_frame.columnconfigure(1, weight=1)

    test_frame_0 = ttk.Frame(browse_file_frame, style='Border.TFrame')
    test_frame_0.grid(row=0, column=0, sticky='nsew')
    test_label_0 = tk.Label(
        test_frame_0,
        text="Label 0",
        bg=COLORS['bg'],
        fg=COLORS['text'],
        font=FONTS['header']
    )
    test_label_0.pack(expand=True)

    test_frame_4 = ttk.Frame(browse_file_frame, style='Border.TFrame')
    test_frame_4.grid(row=0, column=1, sticky='nsew')
    test_label_4 = tk.Label(
        test_frame_4,
        text="Label 4",
        bg=COLORS['bg'],
        fg=COLORS['text'],
        font=FONTS['header']
    )
    browse_btn = create_styled_button(test_frame_4, "Choose File", browse_button)
    browse_btn.pack(expand=True, side='right')

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
main_frame = ttk.Frame(root, style='Border.TFrame')
main_frame.grid(row=0, column=0, sticky='nsew', padx=20, pady=20)


# test_frame_0 = ttk.Frame(main_frame, style='Border.TFrame')
# test_frame_0.grid(row=0, column=0, sticky='nsew')
# test_label_0 = tk.Label(
#     test_frame_0,
#     text="Label 0",
#     bg=COLORS['bg'],
#     fg=COLORS['text'],
#     font=FONTS['header']
# )
# test_label_0.pack(expand=True, side='left')

# test_frame_1 = ttk.Frame(main_frame, style='Border.TFrame')
# test_frame_1.grid(row=1, column=0, sticky='nsew')
# test_label_1 = tk.Label(
#     test_frame_1,
#     text="Label 1",
#     bg=COLORS['bg'],
#     fg=COLORS['text'],
#     font=FONTS['header']
# )
# test_label_1.pack(expand=True)

# test_frame_2 = ttk.Frame(main_frame, style='Border.TFrame')
# test_frame_2.grid(row=2, column=0, sticky='nsew')
# test_label_2 = tk.Label(
#     test_frame_2,
#     text="Label 2",
#     bg=COLORS['bg'],
#     fg=COLORS['text'],
#     font=FONTS['header']
# )
# test_label_2.pack(expand=True)

# test_frame_3 = ttk.Frame(main_frame, style='Border.TFrame')
# test_frame_3.grid(row=3, column=0, sticky='nsew')
# test_label_3 = tk.Label(
#     test_frame_3,
#     text="Label 3",
#     bg=COLORS['bg'],
#     fg=COLORS['text'],
#     font=FONTS['header']
# )
# test_label_3.pack(expand=True)


# test_frame_5 = ttk.Frame(main_frame, style='Border.TFrame')
# test_frame_5.grid(row=1, column=1, sticky='nsew')
# test_label_5 = tk.Label(
#     test_frame_5,
#     text="Label 5",
#     bg=COLORS['bg'],
#     fg=COLORS['text'],
#     font=FONTS['header']
# )
# test_label_5.pack(expand=True)

# test_frame_6 = ttk.Frame(main_frame, style='Border.TFrame')
# test_frame_6.grid(row=2, column=1, sticky='nsew')
# test_label_6 = tk.Label(
#     test_frame_6,
#     text="Label 6",
#     bg=COLORS['bg'],
#     fg=COLORS['text'],
#     font=FONTS['header']
# )
# test_label_6.pack(expand=True)

# test_frame_7 = ttk.Frame(main_frame, style='Border.TFrame')
# test_frame_7.grid(row=3, column=1, sticky='nsew')
# test_label_7 = tk.Label(
#     test_frame_7,
#     text="Label 7",
#     bg=COLORS['bg'],
#     fg=COLORS['text'],
#     font=FONTS['header']
# )
# test_label_7.pack(expand=True)

# test_frame_8 = ttk.Frame(main_frame, style='Border.TFrame')
# test_frame_8.grid(row=0, column=2, sticky='nsew')
# test_label_8 = tk.Label(
#     test_frame_8,
#     text="Label 8",
#     bg=COLORS['bg'],
#     fg=COLORS['text'],
#     font=FONTS['header']
# )
# test_label_8.pack(expand=True)

# test_frame_9 = ttk.Frame(main_frame, style='Border.TFrame')
# test_frame_9.grid(row=1, column=2, sticky='nsew')
# test_label_9 = tk.Label(
#     test_frame_9,
#     text="Label 9",
#     bg=COLORS['bg'],
#     fg=COLORS['text'],
#     font=FONTS['header']
# )
# test_label_9.pack(expand=True)

# test_frame_10 = ttk.Frame(main_frame, style='Border.TFrame')
# test_frame_10.grid(row=2, column=2, sticky='nsew')
# test_label_10 = tk.Label(
#     test_frame_10,
#     text="Label 10",
#     bg=COLORS['bg'],
#     fg=COLORS['text'],
#     font=FONTS['header']
# )
# test_label_10.pack(expand=True)

# test_frame_11 = ttk.Frame(main_frame, style='Border.TFrame')
# test_frame_11.grid(row=3, column=2, sticky='nsew')
# test_label_11 = tk.Label(
#     test_frame_11,
#     text="Label 11",
#     bg=COLORS['bg'],
#     fg=COLORS['text'],
#     font=FONTS['header']
# )
# test_label_11.pack(expand=True)

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

main_frame.rowconfigure(0, weight=1)
main_frame.rowconfigure(1, weight=1)
main_frame.rowconfigure(2, weight=1)
main_frame.rowconfigure(3, weight=1)
main_frame.columnconfigure(0, weight=1)
main_frame.columnconfigure(1, weight=1)

setup_browse_file_frame()
# Controls styling for the label of the currently selected file and the browse file button

# user_input_frame = ttk.Frame(main_frame, style='Border.TFrame')
# user_input_frame.rowconfigure(0, weight=1)
# user_input_frame.columnconfigure(0, weight=1)

# chinese_sentence_frame = ttk.Frame(main_frame, style='Border.TFrame')
# chinese_sentence_frame.rowconfigure(0, weight=1)
# chinese_sentence_frame.columnconfigure(0, weight=1)

# pinyin_sentence_frame = ttk.Frame(main_frame, style='Border.TFrame')
# pinyin_sentence_frame.rowconfigure(0, weight=1)
# pinyin_sentence_frame.columnconfigure(0, weight=1)

# recently_opened_files_frame = ttk.Frame(main_frame, style='Border.TFrame')
# recently_opened_files_frame.rowconfigure(0, weight=1)
# recently_opened_files_frame.columnconfigure(0, weight=1)


# Closes the application window when the 'q' key is pressed
root.bind('<q>', lambda e: close_window(root, e))
root.mainloop()

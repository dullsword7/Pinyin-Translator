import os
from tkinter import filedialog, ttk
import tkinter as tk
from pinyin_jyutping_sentence import pinyin

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

# the obsidian file to open and edit
global current_file_path

# appends the user input to the current file when the Enter key is pressed
def printResult(self):
    userInput = sentence_entry.get().strip()
    if len(userInput) < 1:
        return
    # print(f'Appending [{userInput}] to [{os.path.basename(current_file_path)}]')
    addChinesePinyinSentenceToNotes(userInput)

# @input - the sentence to be translated to pinyin
# translates the sentence to pinyin and appends it to an obsidian note
def addChinesePinyinSentenceToNotes(input):

    # converts the input string to pinyin
    sentence_pinyin = pinyin(input)

    table_entry_chinese = input
    table_entry_pinyin = sentence_pinyin
    table_entry_english = "this is the english translation"
    table_entry = f'\n{table_entry_chinese} <br> {table_entry_pinyin} | {table_entry_english}'

    original_sentence.set(input)
    pinyin_sentence.set(sentence_pinyin)
    sentence_entry.delete(0, 'end')

    try:
        # opens the obsidian note to edit
        with open(current_file_path, 'a', encoding="utf-8") as f:
            f.write(table_entry)
    except:
        print("Select a file")

def browse_button():
    # Allow user to select a directory and store it in global var
    # called folder_path
    global current_file_path
    current_file_path = filedialog.askopenfilename()
    current_file_name = folder_path.set(os.path.basename(current_file_path))
    print(current_file_path)

def create_styled_button(parent, text, command):
    return tk.Button(
        parent,
        text=text,
        command=command,
        bg=COLORS['accent'],
        fg=COLORS['bg'],
        font=FONTS['main'],
        relief='flat',
        padx=15,
        cursor='hand2'
    )

root = tk.Tk()
root.configure(bg=COLORS['bg'])
# Get screen dimensions
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set window size
root_width = 800
root_height = 600
root.geometry(f'{root_width}x{root_height}')
root.minsize(root_width, root_height)

# Calculate center position
x = (screen_width - root_width) // 2
y = (screen_height - root_height) // 2

# Set window position to center of screen
root.geometry(f'+{x}+{y}')
root.title("Chinese to Pinyin Translator")

folder_path = tk.StringVar()
original_sentence = tk.StringVar()
pinyin_sentence = tk.StringVar()

# Style configuration
style = ttk.Style()
style.configure('Custom.TFrame', background=COLORS['bg'])

# Main container
main_frame = ttk.Frame(root, style='Custom.TFrame', padding="20")
main_frame.grid(row=0, column=0, sticky="nsew")

# File selection area
file_frame = ttk.Frame(main_frame, style='Custom.TFrame')
file_frame.grid(row=0, column=0, columnspan=3, sticky="ew", pady=(0, 20))

current_file_label = tk.Label(
    file_frame,
    textvariable=folder_path,
    bg=COLORS['secondary'],
    fg=COLORS['text'],
    font=FONTS['main'],
    padx=10,
    pady=8
)
browse_btn = create_styled_button(file_frame, "Choose File", browse_button)

# Input area
input_frame = ttk.Frame(main_frame, style='Custom.TFrame')
input_frame.grid(row=1, column=0, columnspan=3, sticky="ew", pady=20)

input_label = tk.Label(
    input_frame,
    text="Enter Chinese Text",
    bg=COLORS['bg'],
    fg=COLORS['accent'],
    font=FONTS['header'],
    anchor='w'
)
input_label.pack(fill='x', pady=(0, 5))

sentence_entry = tk.Entry(
    input_frame,
    font=FONTS['input'],
    bg=COLORS['input_bg'],
    fg=COLORS['text'],
    insertbackground=COLORS['text'],
    relief='flat',
    bd=10
)
# Result display area
result_frame = ttk.Frame(main_frame, style='Custom.TFrame')
result_frame.grid(row=2, column=0, columnspan=3, sticky="ew", pady=20)

# Chinese sentence label and text
chinese_label = tk.Label(
    result_frame,
    text="Chinese",
    bg=COLORS['bg'],
    fg=COLORS['accent'],
    font=FONTS['header'],
    anchor='w'
)
chinese_label.pack(fill='x', pady=(0, 5))

original_sentence_label = tk.Label(
    result_frame,
    textvariable=original_sentence,
    bg=COLORS['secondary'],
    fg=COLORS['text'],
    font=FONTS['main'],
    pady=15,
    wraplength=700
    )
original_sentence_label.pack(fill='x', pady=(0, 20))

# Pinyin sentence label and text
pinyin_label = tk.Label(
    result_frame,
    text="Pinyin",
    bg=COLORS['bg'],
    fg=COLORS['accent'],
    font=FONTS['header'],
    anchor='w'
)
pinyin_label.pack(fill='x', pady=(0, 5))

pinyin_sentence_label = tk.Label(
    result_frame,
    textvariable=pinyin_sentence,
    bg=COLORS['secondary'],
    fg=COLORS['accent'],
    font=FONTS['main'],
    pady=15,
    wraplength=700
)
pinyin_sentence_label.pack(fill='x')
# Recent files area
recent_frame = ttk.Frame(main_frame, style='Custom.TFrame')
recent_frame.grid(row=3, column=0, columnspan=3, sticky="ew", pady=20)

recently_opened_label = tk.Label(
    recent_frame,
    text="Recently Opened Files",
    bg=COLORS['bg'],
    fg=COLORS['text'],
    font=FONTS['header']
)

recently_opened_files = tk.Listbox(
    recent_frame,
    bg=COLORS['secondary'],
    fg=COLORS['text'],
    font=FONTS['main'],
    height=4,
    selectmode='single',
    activestyle='none',
    relief='flat',
    selectbackground=COLORS['accent']
)

# Grid configurations
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
main_frame.grid_columnconfigure(1, weight=1)

# Widget placements
current_file_label.pack(side='left', fill='x', expand=True, padx=(0, 10))
browse_btn.pack(side='right')

sentence_entry.pack(fill='x', expand=True)
sentence_entry.bind('<Return>', printResult)
sentence_entry.focus_set()

original_sentence_label.pack(fill='x', pady=(0, 5))
pinyin_sentence_label.pack(fill='x')

recently_opened_label.pack(anchor='w', pady=(0, 10))
recently_opened_files.pack(fill='x')

main_frame.mainloop()

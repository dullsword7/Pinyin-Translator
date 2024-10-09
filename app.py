import os
from tkinter import filedialog
import tkinter as tk
from pinyin_jyutping_sentence import pinyin

default_bg_color = '#40434e'
default_text_color = 'white'

# the obsidian file to open and edit
global current_file_path

# appends the user input to the current file when the Enter key is pressed
def printResult(self):
    userInput = entry.get()
    if len(userInput) < 1:
        return
    print(f'Appending [{userInput}] to [{os.path.basename(current_file_path)}]')
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

    # opens the obsidian note to edit
    with open(current_file_path, 'a', encoding="utf-8") as f:
        f.write(table_entry)

def browse_button():
    # Allow user to select a directory and store it in global var
    # called folder_path
    global current_file_path
    current_file_path = filedialog.askopenfilename()
    current_file_name = folder_path.set(os.path.basename(current_file_path))
    print(current_file_path)

window = tk.Tk()

folder_path = tk.StringVar()

greeting = tk.Label(text="This is my app", fg=default_text_color, bg="blue")
# lbl1 = tk.Label(master=window, text="asdf;lkjjjjjjjjjjjjjasdf", textvariable=folder_path, bg="red")
lbl1 = tk.Label(master=window, text="nahnahnahnahnahnahnahnahnahnahnahnah", bg="red")
button2 = tk.Button(text="Browse", command=browse_button, bg="green")

# handles the user input
entry = tk.Entry(bg="pink")
entry.focus_set()
entry.bind('<Return>', printResult)

greeting.grid(row=0, column=0, padx=2, pady=2)
lbl1.grid(row=0, column=1, padx=2, pady=2)
button2.grid(row=1, column=1, padx=2, pady=2)
entry.grid(row=1, column=0, padx=2, pady=2)

# sets the background color of the window
window.configure(bg=default_bg_color)

# sets the width and height of the window
window.geometry("1080x720")
window.title("Quickly Translate Sentences In Chinese To Pinyin")
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=1)





window.mainloop()


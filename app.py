import os
from tkinter import filedialog
import tkinter as tk
from pinyin_jyutping_sentence import pinyin

default_bg_color = '#40434e'
default_text_color = 'white'
default_font_size = 20

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

root = tk.Tk()

folder_path = tk.StringVar()
original_sentence = tk.StringVar()
pinyin_sentence = tk.StringVar()

root_width = 600
root_height = 400
root_min_width = 600
root_min_height = 400

root.configure(bg="gray")
root.geometry(str(root_width) + 'x' + str(root_height))
root.minsize(root_min_width, root_min_height)
root.title("Quickly Translate Sentences In Chinese To Pinyin")

current_file_label = tk.Label(master=root, textvariable=folder_path, bg="purple", font=("Times New Roman", 15), anchor="center", width=15)
browse_button = tk.Button(text="Browse", command=browse_button, bg="green")
recently_opened_files = tk.Label(master=root, text="recent files", bg="teal", font=("Times New Roman", 15), anchor="center", width=5, height=8)
original_sentence_label = tk.Label(master=root, textvariable=original_sentence, bg="red", font=("Times New Roman", 15), anchor="center", width=40, height=2)
pinyin_sentence_label = tk.Label(master=root, textvariable=pinyin_sentence, bg="pink", font=("Times New Roman", 15), anchor="center", width=40, height=2)

# handles the user input
sentence_entry = tk.Entry(bg="light blue", font=("Times New Roman", 15))
sentence_entry.focus_set()
sentence_entry.bind('<Return>', printResult)

root.grid_columnconfigure(1,weight=1)
root.grid_columnconfigure(5, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(7, weight=1)


recently_opened_files.grid(row=2, column=2, padx=10, pady=10, sticky="news", rowspan=2)
current_file_label.grid(row=2, column=3, padx=10, pady=10, sticky="news")
browse_button.grid(row=2, column=4, padx=10, pady=10, sticky="ews")
sentence_entry.grid(row=3, column=3, padx=10, pady=(50, 10), sticky="news", columnspan=2)
original_sentence_label.grid(row=5, column=2, padx=10, pady=(20, 0), sticky="news", columnspan=3)
pinyin_sentence_label.grid(row=6, column=2, padx=10, pady=(0, 10), sticky="news", columnspan=3)

root.mainloop()


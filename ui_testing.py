import os
from tkinter import filedialog
import tkinter as tk
from pinyin_jyutping_sentence import pinyin

def printResult(self):
    print(f'Window Size - Width: {root.winfo_width()} , Height: {root.winfo_height()}')
    print(f'Widget Size - Width: {original_sentence_label.winfo_width()} , Height: {original_sentence_label.winfo_height()}')

root_width = 600
root_height = 400
root_min_width = 600
root_min_height = 400

root = tk.Tk()
root.configure(bg="gray")
root.geometry(str(root_width) + 'x' + str(root_height))
root.minsize(root_min_width, root_min_height)
root.title("Quickly Translate Sentences In Chinese To Pinyin")

current_file_label = tk.Label(master=root, text="current file", bg="purple")
browse_button = tk.Button(text="Browse", command="", bg="green")
recently_opened_files = tk.Label(master=root, text="recent files", bg="teal", height=10)
original_sentence_label = tk.Label(master=root, text="original sentence", bg="red", width=50)
pinyin_sentence_label = tk.Label(master=root, text="pinyin sentence", bg="pink", width=50)

# handles the user input
sentence_entry = tk.Entry(bg="light blue")
sentence_entry.focus_set()
sentence_entry.bind('<Return>', printResult)

root.grid_columnconfigure(1,weight=1)
root.grid_columnconfigure(5,weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(7, weight=1)


recently_opened_files.grid(row=2, column=2, padx=10, pady=10, sticky="news", rowspan=2)
current_file_label.grid(row=2, column=3, padx=10, pady=10, sticky="news")
browse_button.grid(row=2, column=4, padx=10, pady=10, sticky="ews")
sentence_entry.grid(row=3, column=3, padx=10, pady=(50, 10), sticky="news", columnspan=2)
original_sentence_label.grid(row=5, column=2, padx=10, pady=(10, 0), sticky="news", columnspan=3)
pinyin_sentence_label.grid(row=6, column=2, padx=10, pady=(0, 10), sticky="news", columnspan=3)

root.mainloop()

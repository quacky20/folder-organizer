import tkinter as tk
from tkinter import ttk
from utils import *

class Window(tk.Tk):
    def __init__(self, basePath):
        super().__init__()
        self.title('Folder Organizer')
        self.geometry('400x500')
        
        self.basePath = basePath
        
        self.files = getFiles(basePath)
        self.exception_list = []
        self.files_to_move = []
        self.history = []

        self.create_widgets()

    def create_widgets(self):
        self.title_label = ttk.Label(master = self, text = 'Folder Organizer', font = 'Calibri 24 bold')
        self.title_label.pack()
        
        # input field
        self.input_frame = ttk.Frame(master = self)
        self.selection_label = ttk.Label(master = self.input_frame, text = 'Select files to ignore', font = 'Calibri 16')
        self.title_label.pack()
        self.files_list = tk.Listbox(self.input_frame, selectmode = 'multiple')
        for item in self.files:
            self.files_list.insert(tk.END, item)
        self.button = ttk.Button(master = self.input_frame, text = 'Clean', command = self.move)
        self.undo_button = ttk.Button(master = self.input_frame, text = 'Undo', command = self.undo)
        self.files_list.pack(side = 'left', padx = 10)
        self.button.pack(side = 'left')
        self.selection_label.pack()
        self.input_frame.pack(pady = 10)

        # output
        self.output_label = ttk.Label(master = self, text = 'Finished', font = 'Calibri 24 bold')
        
    def refreshFiles(self):
        self.files_list.delete(0, tk.END)
        self.files = getFiles(self.basePath)
        for item in self.files:
            self.files_list.insert(tk.END, item)
        
    def move(self):
        self.exception_list = [self.files_list.get(i) for i in self.files_list.curselection()]
        self.files_to_move = [file for file in self.files if file not in self.exception_list]
        organize(path = self.basePath,files = self.files_to_move)
        self.output_label.config(text='Finished')
        self.output_label.pack()
        self.refreshFiles()
        self.undo_button.pack(side = 'left')
        self.button.pack_forget()
            
    def undo(self):
        undo(self.basePath, self.files_to_move)
        self.output_label.config(text='Undid')
        self.button.pack(side = 'left')
        self.refreshFiles()
        self.undo_button.pack_forget()
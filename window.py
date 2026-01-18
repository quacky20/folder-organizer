import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from CTkListbox import *
from utils import *

# class Window(tk.Tk):
#     def __init__(self, basePath):
#         super().__init__()
#         self.title('Folder Organizer')
#         self.geometry('400x500')
        
#         self.basePath = basePath
        
#         self.files = getFiles(basePath)
#         self.exception_list = []
#         self.files_to_move = []
#         self.history = []

#         self.create_widgets()

#     def create_widgets(self):
#         self.title_label = ttk.Label(master = self, text = 'Folder Organizer', font = 'Calibri 24 bold')
#         self.title_label.pack()
        
#         # input field
#         self.input_frame = ttk.Frame(master = self)
#         self.selection_label = ttk.Label(master = self.input_frame, text = 'Select files to ignore', font = 'Calibri 16')
#         self.title_label.pack()
#         self.files_list = tk.Listbox(self.input_frame, selectmode = 'multiple')
#         for item in self.files:
#             self.files_list.insert(tk.END, item)
#         self.button = ttk.Button(master = self.input_frame, text = 'Clean', command = self.move)
#         self.undo_button = ttk.Button(master = self.input_frame, text = 'Undo', command = self.undo)
#         self.files_list.pack(side = 'left', padx = 10)
#         self.button.pack(side = 'left')
#         self.selection_label.pack()
#         self.input_frame.pack(pady = 10)

#         # output
#         self.output_label = ttk.Label(master = self, text = 'Finished', font = 'Calibri 24 bold')
        
#     def refreshFiles(self):
#         self.files_list.delete(0, tk.END)
#         self.files = getFiles(self.basePath)
#         for item in self.files:
#             self.files_list.insert(tk.END, item)
        
#     def move(self):
#         self.exception_list = [self.files_list.get(i) for i in self.files_list.curselection()]
#         self.files_to_move = [file for file in self.files if file not in self.exception_list]
#         organize(path = self.basePath,files = self.files_to_move)
#         self.output_label.config(text='Finished')
#         self.output_label.pack()
#         self.refreshFiles()
#         self.undo_button.pack(side = 'left')
#         self.button.pack_forget()
            
#     def undo(self):
#         undo(self.basePath, self.files_to_move)
#         self.output_label.config(text='Undid')
#         self.button.pack(side = 'left')
#         self.refreshFiles()
#         self.undo_button.pack_forget()
        
class Window(ctk.CTk):
    def __init__(self, basePath):
        super().__init__()
        
        self.bg = '#061E29'
        self.primary = '#1D546D'
        self.hover = '#387997'
        self.secondary = '#5F9598'
        self.text = '#F3F4F4'
        
        self.configure(fg_color = self.bg)
        self.resizable(False, False)
        self.title('Folder Organizer')
        self.geometry('600x400')
        self.iconbitmap('./icon.ico')
        
        self.basePath = basePath
        
        self.files = getFiles(basePath)
        self.exception_list = []
        self.files_to_move = []
        self.history = []


        self.create_widgets()

    def create_widgets(self):
        self.columnconfigure((0, 1, 2, 3), weight = 1)
        self.rowconfigure((0, 1, 2, 3, 4), weight = 1, uniform='row')
        
        self.title_label = ctk.CTkLabel(
            master = self, 
            text = 'Folder Organizer', 
            text_color = 'white',
            font=('Pixelify Sans', 26, 'bold'))
        self.title_label.grid(row = 0, column = 0, sticky = '', ipadx = 20, ipady = 20)
        
        # button and label
        self.selection_label = ctk.CTkLabel(
            master = self, 
            text = 'Select files to ignore',
            text_color = self.text,
            font=('Pixelify Sans', 20))
        self.selection_label.grid(row = 1, column = 0, sticky = 'n', ipadx = 20, ipady = 10)
        
            
        self.button = ctk.CTkButton(
            master = self, 
            text = 'Clean', 
            fg_color = self.primary,
            hover_color = self.hover,
            text_color = self.text,
            border_color = self.secondary,
            border_width = 2,
            font=('Pixelify Sans', 16),
            command = self.move)
        self.button.grid(row = 2, column = 0, sticky = 'news', padx = 30, pady = 10)
        
        # file list
        self.files_list = CTkListbox(
            self, 
            multiple_selection=True,
            font = ('Pixelify Sans', 16),
            border_color = self.secondary,
            border_width = 2,
            hover_color = self.hover)
        for item in self.files:
            self.files_list.insert(tk.END, item)
        self.files_list.grid(row = 0, column = 1, rowspan = 5, columnspan = 3, sticky = 'news', padx = 10, pady = 20)
        
        # output label
        self.output_label = ctk.CTkLabel(
            master = self, 
            text = '',
            font=('Pixelify Sans', 24, 'bold'))
        self.output_label.grid(row = 4, column = 0, sticky = '', pady = 10)
        
    def refreshFiles(self):
        self.files_list.delete(0, tk.END)
        self.files = getFiles(self.basePath)
        for item in self.files:
            self.files_list.insert(tk.END, item)
        
    def move(self):
        self.exception_list = [self.files_list.get(i) for i in self.files_list.curselection()]
        self.files_to_move = [file for file in self.files if file not in self.exception_list]
        organize(path = self.basePath,files = self.files_to_move)
        self.output_label.configure(text='Finished', text_color="#4fff95")
        self.refreshFiles()
        self.button.configure(text = 'Undo', command = self.undo)
            
    def undo(self):
        undo(self.basePath, self.files_to_move)
        self.output_label.configure(text='Undid', text_color="#ff8080")
        self.button.configure(text = 'Clean', command = self.move)
        self.refreshFiles()
  
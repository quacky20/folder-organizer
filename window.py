import tkinter as tk
import customtkinter as ctk
from CTkListbox import *
from utils import *
from tkinter import filedialog

class Window(ctk.CTk):
    def __init__(self):
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
        
        self.basePath = ''
        self.savePath = ''

        self.files = []
        self.exception_list = []
        self.files_to_move = []
        self.history = []


        self.create_widgets()

    def create_widgets(self):
        self.columnconfigure((0, 1, 2, 3), weight = 1)
        self.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7), weight = 1, uniform='row')
        
        self.title_label = ctk.CTkLabel(
            master = self, 
            text = 'Folder Organizer', 
            text_color = 'white',
            font=('Pixelify Sans', 26, 'bold'))
        self.title_label.grid(row = 0, column = 0, sticky = '', ipadx = 20, ipady = 20)
        
        # label
        self.selection_label = ctk.CTkLabel(
            master = self, 
            text = 'Select files to ignore',
            text_color = self.text,
            font=('Pixelify Sans', 20))
        self.selection_label.grid(row = 1, column = 0, sticky = 'n', ipadx = 20, ipady = 10)
        
        # buttons
        self.button = ctk.CTkButton(
            master = self, 
            text = 'Clean', 
            fg_color = self.primary,
            hover_color = self.hover,
            text_color = self.text,
            border_color = self.secondary,
            border_width = 2,
            font=('Pixelify Sans', 16),
            command = self.move,
        )
        self.button.grid(row = 2, column = 0, sticky = 'news', padx = 30, pady = 10)
        
        if not self.files:
            self.button.configure(state = 'disabled')
        
        self.choose_directory = ctk.CTkButton(
            master = self,
            text = 'Choose directory',
            fg_color = self.primary,
            hover_color = self.hover,
            text_color = self.text,
            border_color = self.secondary,
            border_width = 2,
            font=('Pixelify Sans', 16),
            command = self.directory_choose
        )
        self.choose_directory.grid(row = 3, column = 0, sticky = 'news', padx = 30, pady = 10)
        
        self.choose_save_directory = ctk.CTkButton(
            master = self,
            text = 'Choose save directory',
            fg_color = self.primary,
            hover_color = self.hover,
            text_color = self.text,
            border_color = self.secondary,
            border_width = 2,
            font=('Pixelify Sans', 16),
            command = self.directory_save_choose
        )
        self.choose_save_directory.grid(row = 4, column = 0, sticky = 'news', padx = 30, pady = 10)
        
        # file list
        self.files_list = CTkListbox(
            self, 
            multiple_selection=True,
            font = ('Pixelify Sans', 16),
            border_color = self.secondary,
            border_width = 2,
            hover_color = self.hover)
        if self.files:
            for item in self.files:
                self.files_list.insert(tk.END, item)
        self.files_list.grid(row = 0, column = 1, rowspan = 5, columnspan = 3, sticky = 'news', padx = 10, pady = (20, 0))
        
        # chosen directory label
        self.directory_label = ctk.CTkLabel(
            master = self,
            wraplength = 200,
            text = '',
            font=('Pixelify Sans', 16, 'bold'),
            justify = 'left'
        )
        self.directory_label.grid(row = 5, column = 0, rowspan = 2, sticky = 'n', pady = 10)
        
        save_to_label = ctk.CTkLabel(
            master = self,
            text = 'Save to: ',
            font=('Pixelify Sans', 16, 'bold')
        )
        
        self.save_directory_label = ctk.CTkLabel(
            master = self,
            wraplength = 150,
            text = '',
            font=('Pixelify Sans', 16, 'bold'),
            justify = 'left'
        )
        self.save_directory_label.grid(row = 5, column = 2, rowspan = 2, sticky = 'n', pady = (20, 10))
        save_to_label.grid(row = 5, column = 1, rowspan = 2, sticky = 'n', pady = (20, 10))
        
        # output label
        status_label = ctk.CTkLabel(
            master = self,
            text = 'Status: ',
            font=('Pixelify Sans', 16, 'bold')
        )
        status_label.grid(row = 7, column = 0, sticky = 'e', pady = (0, 10), padx = (5,5))
        self.status = ctk.CTkLabel(
            master = self, 
            text = '',
            font=('Pixelify Sans', 16, 'bold'))
        self.status.grid(row = 7, column = 1, sticky = 'w', pady = (0, 10))
        
        # refresh button
        self.refresh_button = ctk.CTkButton(
            master = self, 
            text = 'Refresh \u27f3', 
            fg_color = self.primary,
            hover_color = self.hover,
            text_color = self.text,
            border_color = self.secondary,
            border_width = 2,
            font=('Pixelify Sans', 16),
            command = self.refreshFiles,
        )
        
        if not self.files:
            self.refresh_button.configure(state = 'disabled')
            
        self.refresh_button.grid(row = 7, column = 0, sticky = 'w', pady = (0, 10), padx = 10)
        
    def refreshFiles(self):
        self.files_list.delete(0, tk.END)
        self.files = getFiles(self.basePath)
        for item in self.files:
            self.files_list.insert(tk.END, item)
        
    def move(self):
        self.exception_list = [self.files_list.get(i) for i in self.files_list.curselection()]
        self.files_to_move = [file for file in self.files if file not in self.exception_list]
        try:
            organize(
                path = self.basePath,
                savePath = self.savePath,
                files = self.files_to_move
                )
        except Exception:
            self.status.configure(text='Error', text_color="#ff8080")
            
        self.status.configure(text='Finished', text_color="#4fff95")
        self.refreshFiles()
        self.button.configure(text = 'Undo', command = self.undo)
            
    def undo(self):
        try:
            undo(
                path = self.basePath,
                save_path = self.savePath,
                files_to_move = self.files_to_move
                )
        except Exception:
            self.status.configure(text='Error', text_color="#ff8080")
        self.status.configure(text='Reverted changes', text_color="#ff8080")
        self.button.configure(text = 'Clean', command = self.move)
        self.refreshFiles()
  
    def directory_choose(self):
        self.basePath = filedialog.askdirectory(
            initialdir='/',
            title='Select folder to clean',
        )
        self.directory_label.configure(text = self.basePath)
        self.refreshFiles()
        if self.basePath:
            self.refresh_button.configure(state = 'normal')
            if self.savePath:
                self.button.configure(state = 'normal')
        
    def directory_save_choose(self):
        self.savePath = filedialog.askdirectory(
            initialdir='/',
            title='Select folder to save to',
        )
        self.save_directory_label.configure(text = self.savePath)
        if self.basePath and self.savePath:
            self.button.configure(state = 'normal')

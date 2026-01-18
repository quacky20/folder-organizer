import pathlib
from window import Window

if __name__ == '__main__':
    mypath = pathlib.Path.home() / 'Desktop'
    app = Window()
    app.mainloop()
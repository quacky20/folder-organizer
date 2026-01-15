import os
import shutil

def createFolder(base_path, name):
    try:
        os.mkdir(os.path.join(base_path, name))
        print(f'Created directory: {name}')
    except FileExistsError:
        print(f'{name} already exists')
    except PermissionError:
        print('Permission denied')
    except Exception as e:
        print(f'Error: {e}')
        
def createFolders(base_path):
    directories = ['Images', 'Videos', 'Documents', 'Others']
    for name in directories:
        createFolder(base_path, os.path.join('Desktop', name))

def moveFiles(path):
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

    for file in files:
        if '.' not in file:
            try:
                shutil.move(os.path.join(path, file), os.path.join(path, 'Desktop', 'Others', file))
            except Exception as e:
                print(f'Error moving {file}: {e}')
            finally:
                continue
        
        extension = file.split('.')[-1].lower()
        
        try:
            match extension:
                case 'jpg' | 'jpeg' | 'png' | 'gif' | 'psd' | 'svg':
                    shutil.move(os.path.join(path, file), os.path.join(path, 'Desktop', 'Images', file))
                case 'mp4' | 'mov' | 'avi' | 'wmv' | 'mkv' | 'webm' | 'flv' | 'mpg' | 'mpeg':
                    shutil.move(os.path.join(path, file), os.path.join(path, 'Desktop', 'Videos', file))
                case 'pdf' | 'doc' | 'docx' | 'txt' | 'ppt' | 'pptx' | 'xls' | 'xlsx':
                    shutil.move(os.path.join(path, file), os.path.join(path, 'Desktop', 'Documents', file))
                case 'lnk':
                    pass
                case _:
                    shutil.move(os.path.join(path, file), os.path.join(path, 'Desktop', 'Others', file))
        except Exception as e:
            print(f'Error moving {file}: {e}')
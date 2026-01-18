import os
import shutil

def createFolder(save_path, name):
    try:
        os.mkdir(os.path.join(save_path, name))
    except FileExistsError:
        return
    except PermissionError:
        print('Permission denied')
    except Exception as e:
        print(f'Error: {e}')
        raise
        
def createFolders(save_path):
    directories = ['Images', 'Videos', 'Documents', 'Others']
    for name in directories:
        createFolder(save_path, name)
        
def getFiles(basePath):
    return [f for f in os.listdir(basePath) if os.path.isfile(os.path.join(basePath, f))]

def moveFiles(path, savePath, files):
    for file in files:
        if '.' not in file:
            try:
                shutil.move(os.path.join(path, file), os.path.join(savePath, 'Others', file))
            except Exception as e:
                print(f'Error moving {file}: {e}')
                raise
            finally:
                continue
        
        extension = file.split('.')[-1].lower()
        
        try:
            match extension:
                case 'jpg' | 'jpeg' | 'png' | 'gif' | 'psd' | 'svg':
                    shutil.move(os.path.join(path, file), os.path.join(savePath, 'Images', file))
                case 'mp4' | 'mov' | 'avi' | 'wmv' | 'mkv' | 'webm' | 'flv' | 'mpg' | 'mpeg':
                    shutil.move(os.path.join(path, file), os.path.join(savePath, 'Videos', file))
                case 'pdf' | 'doc' | 'docx' | 'txt' | 'ppt' | 'pptx' | 'xls' | 'xlsx':
                    shutil.move(os.path.join(path, file), os.path.join(savePath, 'Documents', file))
                case 'lnk':
                    pass
                case _:
                    shutil.move(os.path.join(path, file), os.path.join(savePath, 'Others', file))
        except Exception as e:
            print(f'Error moving {file}: {e}')
            raise
                
def undo(path, save_path, files_to_move):
    directories = ['Images', 'Videos', 'Documents', 'Others']
    for folder in directories:
        directory = os.path.join(save_path, folder)
        files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
        
        for file in files:
            if file in files_to_move:
                try:
                    shutil.move(os.path.join(directory, file), os.path.join(path, file))
                except Exception as e:
                    print(f'Error moving {file}: {e}')  
                    raise     

def organize(path, savePath, files):
    createFolders(savePath)
    moveFiles(path, savePath, files)
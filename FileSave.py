from pathlib import Path
import json
import os

savePath = Path(os.getcwd() + '/saves/')
saveFile = Path('students.txt')

def CreatePath() -> None:
    # creates saves directory for datasheets 
    if not(os.path.isdir(savePath)) == True: # checks if the directory exists
        print('true')
        os.mkdir(savePath)
        _prevdir = ConnectPath()
        _stream = open(saveFile, 'w+') # creates new text file for student grades
        CloseSave(_stream, _prevdir)

def ConnectPath() -> None:
    prevdir = os.getcwd() #
    '''
    previous directory saved as variable so to return to after closing function
    without it, imports will not work in Prog
    '''
    os.chdir(savePath)
    return prevdir # previous directory returned

def OpenSave():
    prevdir = ConnectPath()
    if saveFile.is_file() == True:
        return open(saveFile, 'r+'), prevdir
    else:
        return open(saveFile, 'w+'), prevdir
def CloseSave(stream, dir) -> None:
    stream.close()
    os.chdir(dir) #changes directory to pass Path, this case the previous directory

def LoadData(students) -> None:
    save, prevdir = OpenSave()
    students.clear() # deletes all previous dictionaries to remove chance of duplicates
    for line in save.readlines():
        students.append(json.loads(line)) # json.loads() converts line from text file to python dictionary
    CloseSave(save, prevdir)

def SaveData(students) -> None:
    save, prevdir = OpenSave()
    for student in students:
        save.write(json.dumps(student)+'\n') # json.dumps() converts python dictionary to text file
    CloseSave(save, prevdir)
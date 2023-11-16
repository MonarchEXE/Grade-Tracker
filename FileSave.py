from pathlib import Path
import json
import os

savePath = Path(os.getcwd() + '/saves/')
saveFile = Path('students.txt')

def CreatePath() -> None:
    if not(os.path.isdir(savePath)) == True:
        print('true')
        os.mkdir(savePath)
        _prevdir = ConnectPath()
        _stream = open(saveFile, 'w+')
        CloseSave(_stream, _prevdir)
    print(os.getcwd())

def ConnectPath() -> None:
    prevdir = os.getcwd()
    os.chdir(savePath)
    return prevdir

def OpenSave():
    prevdir = ConnectPath()
    if saveFile.is_file() == True:
        return open(saveFile, 'r+'), prevdir
    else:
        return open(saveFile, 'w+'), prevdir
def CloseSave(stream, dir) -> None:
    stream.close()
    os.chdir(dir)

def LoadData(students) -> None:
    save, prevdir = OpenSave()
    students.clear()
    for line in save.readlines():
        students.append(json.loads(line))
    CloseSave(save, prevdir)

def SaveData(students) -> None:
    save, prevdir = OpenSave()
    for student in students:
        save.write(json.dumps(student)+'\n')
    CloseSave(save, prevdir)
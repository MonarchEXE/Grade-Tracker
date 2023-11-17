import GradeTracker as gtDict
import GradeAvgs as gtAvgs
import TblDisplay as gtDisplay
import FileSave as gtFile

# list to locally hold all current students
# listed with a nested dict that has nested dicts
currentStudents = [
    {'name': 'Claude',
     'grades': {
        'Maths': 7,
        'English': 5    
     }
     },
     {'name': 'Jerma',
     'grades': {
        'Maths': 6,
        'English': 9    
     }
     }
    ]

def CreateBarrier() -> None:
    # basic function that prints a barrier made of 100 dashes
    # used for dividing new menu options.
    barrier = ''
    for i in range (0,100):
        barrier += '-'
    print(barrier)
    return

def NewStudentMenu() -> None:
    CreateBarrier()
    stdName = input('Enter student\'s name (leave empty to exit): ')
    if(stdName != ''):        
        subjects = []
        print('Enter subject title: ')
        while(True):
            subject = input('')
            if(subject == ''):
                break
            subjects.append(subject)
        currentStudents.append(gtDict.CreateStudent(stdName, subjects))    
        print('Student datasheet created')
    MainMenu()

def AverageGradesMenu() -> None:
    CreateBarrier()
    print('Grade Averages Menu.')
    print('Select an option:')
    print('    1. Find average grades per student.')
    print('    2. Find average grades per subject.')
    print('    0. Exit to main menu.')
    print()
    choice = -1
    while(choice < 0 or choice > 2):
        try:
            choice = int(input('Enter Option: '))
        except:
            print('Invalid input')
            continue
        if(choice < 0 or choice > 2):
            print('Enter a valid choice')
            continue
    match choice:
        case 1:
            title = 'Grade Averages per Student'
            gtDisplay.DisplayGrades(currentStudents,title,gtAvgs.StudentGrades)
        case 2:
            title = 'Grade Averages per Subject'
            gtDisplay.DisplayGrades(currentStudents,title,gtAvgs.SubjectGrades)
        case 0:
            pass
    MainMenu()

def AccessGradesMenu():
    CreateBarrier()
    print('Student Grades Menu.')
    print('Select an option:')
    print('    1. Alter a student\'s subject grade.')
    print('    2. Display all student\'s grades.')
    print('    0. Exit to main menu.')
    print()
    choice = -1
    while(choice < 0 or choice > 2):
        try:
            choice = int(input('Enter Option: '))
        except:
            print('Invalid input')
            continue
        if(choice < 0 or choice > 2):
            print('Enter a valid choice')
            continue
    match choice:
        case 1:
            gtDict.AlterStudentGrade(currentStudents)
        case 2:
            gtDict.GetStudentGrades(currentStudents)
        case 0:
            pass
    MainMenu()

def SaveData():
    CreateBarrier()
    print('Save/Load Data Menu.')
    print('Select an option:')
    print('    1. Save current changes to student datasheets.')
    print('    2. Load previous student datasheets.')
    print('    0. Exit to main menu.')
    print()
    choice = -1
    while(choice < 0 or choice > 2):
        try:
            choice = int(input('Enter Option: '))
        except:
            print('Invalid input')
            continue
        if(choice < 0 or choice > 2):
            print('Enter a valid choice')
            continue
    match choice:
        case 1:
            gtFile.SaveData(currentStudents)
        case 2:
            gtFile.LoadData(currentStudents)
        case 0:
            pass
    MainMenu()

def StartMenu():
    CreateBarrier()
    print('Welcome to Student Grade Tracker!')
    gtFile.CreatePath()
def MainMenu():
    CreateBarrier()
    print('Main Menu.')
    print('Select an option: ')
    print('    1. Create a new student datasheet.')
    print('    2. Access a student\'s datasheet.')
    print('    3. Find grade averages.')
    print('    4. Save/Load student datasheets.')
    print('    0. Exit Program.')
    print()

    choice = -1
    while(choice < 0 or choice > 4):
        try:
            choice = int(input('Enter Option: '))
        except:
            print('Invalid input')
            continue
        if(choice < 0 or choice > 4):
            print('Enter a valid choice')
            continue
    match choice:
        case 1:
            NewStudentMenu()
        case 2:
            AccessGradesMenu()
        case 3:
            AverageGradesMenu()
        case 4:
            SaveData()
        case 0:
            return

StartMenu()
MainMenu()
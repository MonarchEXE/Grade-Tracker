import GradeTracker as gtDict
import InputValidation as gtValid
import GradeAvgs as gtAvgs
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
            title = 'Grade Averages per Subject'
            print("Work in progess...")
        case 2:
            title = 'Grade Averages per Subject'
            gtAvgs.TblDisplay.DisplayGrades(currentStudents,title,gtAvgs.CollSubjectGrades)
        case 0:
            pass
    MainMenu()

def AccessGradesMenu():
    CreateBarrier()
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

def MainMenu() -> None:
    CreateBarrier()
    print('Welcome to Student Grade Tracker!')
    print('Select an option: ')
    print('    1. Create a new student datasheet.')
    print('    2. Access a student\'s datasheet.')
    print('    3. Find grade averages.')
    print('    4. Save current changes.')
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
            print('Not Available at the moment.')
        case 0:
            return

MainMenu()
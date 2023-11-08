import InputValidation as inValid

def StudentAvgs(students) -> dict:
    for student in students:
        StudentAvg(student)
    return
def StudentAvg(student) -> int:
    # function that tallies all grades of a given student and calculates average
    # no return, just prints the name of student and their grade average
    totalGrade = 0
    i = 0
    for grade in student['grades']:
        try:
            totalGrade += int(student['grades'][grade])
        except:
            print('Error')
        i += 1
    print('Average grade of %s: %s' % (student.get('name'), (totalGrade/i)))
    return

def SubjectAvg(subject, students) -> int:
    # function to collect avg subject grade per student
    # 'students' parameters are all student dicts w/ corresponding 'subject'
    # e.g., all students have 'Physics' as a tracked subject   
    totalGrade = 0
    i = 0
    for grade in students:
        totalGrade += students[grade][subject]
        i = i + 1
    return (totalGrade/i)

def CreateStudent(name, subjects) -> dict:
    newDict = {
        'name' : name,
        'grades': {}
        }
    if(len(subjects) != 0):
        # if 'subject' param has a one arg, then it calls AddSubjects
        # grades dict is overwritten w/ return value of AddSubjects
        newDict['grades'] = AddSubjects(subjects)
    return newDict
def AddSubjects(subjects) -> dict:
    # function that creates a dictionary of subjects
    # key-value is { subject : grade }
    gradesDict = {}
    for subject in subjects:
        gradesDict[subject] = None
    print(gradesDict) # test code, remember to delete
    return gradesDict

def AlterStudentGrade(students) -> dict:
    student = GetStudent(students)
    stdSubject = input('Enter subject: ')
    grade = inValid.GradeInput.ValidInput()
    # finds index of selected student, and overwrites the index with the student dict
    # with updated grade
    students[students.index(student)] = UpdateGrade(student, stdSubject,grade)
    # returning it updates currentStudents without 
    return students
def UpdateGrade(student, subject, grade) -> None: 
    student['grades'][subject] = grade
    return student

def GetStudentGrades(students):
    student = GetStudent(students) 
    if(student == None):
        print('Student not found.')
        return
    print(student['grades'])
def GetStudent(students) -> dict:
    # locates the student of given name from list 'students' 
    # students parameter is a list of 'student' dictionaries 
    # (pretty much just to pass in currentStudents into the func)
    stdName = input('Enter student name: ')
    for student in students:
        if(student.get('name') != stdName):
            continue
        else:
            return student
    return None
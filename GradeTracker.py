import InputValidation as inValid

def GradeAvgStd(grades) -> int:
    # collects average of a student
    # student is selected outside of function
    # student's grades are passed in as arg named 'grades'
    totalGrade = 0
    i = 0
    for subject in grades:
        totalGrade += grades[subject]
        i += 1
    return totalGrade/i
def GradeAvgSbj(subject, students) -> int:
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
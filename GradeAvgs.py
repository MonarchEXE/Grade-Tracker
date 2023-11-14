def AddStudentKeys(student, grades):
    if not(student.get('name') in grades):
        grades.update({student.get('name') : [0,0]})
def CollectStdGrades(stdGrades, grades, stdName):
    for grade in stdGrades.values():
        grades[stdName][0] += grade
        grades[stdName][1] += 1


def AddSubjectKeys(student, grades):
    for key in student['grades'].keys():
        if not(key in grades):
            grades.update({key : [0,0]})
def CollectSbjGrades(stdGrades, grades) -> None:
    for subject, grade in stdGrades.items():
        grades[subject][0] += grade
        grades[subject][1] += 1

def AvgGrades(collectedGrades, avgs) -> None:
    for subject, tuple in collectedGrades.items():
        avgGrade =  tuple[0]/tuple[1]
        if not(subject in avgs):
            avgs.update({subject : avgGrade})

def CollSubjectGrades(students):
    listGrades = {}
    gradeAvgs = {}
    for student in students:
        AddSubjectKeys(student, listGrades)
        CollectSbjGrades(student['grades'], listGrades)
        AvgGrades(listGrades, gradeAvgs)
    return gradeAvgs

def CollStudentGrades(students):
    listGrades = {}
    gradeAvgs = {}
    for student in students:
        AddStudentKeys(student, listGrades)
        CollectStdGrades(student.get('grades'),listGrades,student.get('name'))
        AvgGrades(listGrades, gradeAvgs)
    return gradeAvgs


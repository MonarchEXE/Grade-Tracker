def AddSubjectKeys(student, grades):
    for key in student['grades'].keys():
        if not(key in grades):
            grades.update({key : [0,0]})

def CollectGrades(stdGrades, grades) -> None:
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
        CollectGrades(student['grades'], listGrades)
        AvgGrades(listGrades, gradeAvgs)
    return gradeAvgs

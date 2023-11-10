class TblDisplay:    
    '''
    
    '''
    def HorizontalBar() -> str:
        horizontalBar = ''
        for i in range(0,50):
            horizontalBar += '-'
        return horizontalBar
    def VerticalBar(title) -> str:
        vBar = '|   '
        vBar += title
        for i in range(0,45-len(str(title))):
            vBar += ' '
        vBar += '|'
        return vBar
    def GradeBar(subject, grade) -> str:
        vBar = '| '
        vBar += subject
        for i in range(0,(30-len(subject))):
            vBar += ' '
        vBar += '|'
        for i in range(0,(15-len(str(grade)))):
            vBar += ' '
        vBar += str(grade)
        vBar += ' |'

        print(vBar)
    def DisplayGrades(students, title, function) -> None:
        xBar = TblDisplay.HorizontalBar()
        titleBar = TblDisplay.VerticalBar(title)
        print(xBar)
        print(titleBar)
        print(xBar)
        gradeAvgs = function(students)
        for subject, grade in gradeAvgs.items():
            TblDisplay.GradeBar(subject, grade)
        print(xBar)

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

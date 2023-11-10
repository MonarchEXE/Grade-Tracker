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
    xBar = HorizontalBar()
    titleBar = VerticalBar(title)
    print(xBar)
    print(titleBar)
    print(xBar)
    gradeAvgs = function(students)
    for subject, grade in gradeAvgs.items():
        GradeBar(subject, grade)
    print(xBar)

import ctypes

class GradeInput:
   def ValidInput() -> int:
        valid = False
        grade = 0
        while(valid == False):
            grade = input('Enter subject grade: ')
            if(GradeInput.TypeCheck(grade) == False or GradeInput.ValueCheck(grade) == False):
                continue
            valid = True
        return grade
   def ValueCheck(value) -> bool:
       if(int(value) < 0 or int(value) > 100):
            raise Exception(ctypes.windll.user32.MessageBoxW(None, u'Enter a valid grade.', u'Error', None))
            return False
       return True
   def TypeCheck(value) -> bool:
        try:
            value = int(value)
            return True
        except:
            ctypes.windll.user32.MessageBoxW(None, u'Invalid input.', u'Error', None)
            return False
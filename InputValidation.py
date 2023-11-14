import ctypes
# module used to display error messages on a small pop-up window
# to reduce the clutter displayed on the terminal 

class GradeInput:
   def ValidInput() -> int:
        valid = False
        grade = 0
        while(valid == False):
            # continuously asks the user for a grade until a valid grade is entered
            grade = input('Enter subject grade: ')
            if(GradeInput.TypeCheck(grade) == False or GradeInput.ValueCheck(grade) == False):
                continue
            valid = True
        return grade
   def ValueCheck(value) -> bool:
       #checks if the grade is within valid values
        if(int(value) < 0 or int(value) > 100):
            raise Exception(ctypes.windll.user32.MessageBoxW(None, u'Enter a valid grade.', u'Error', None))
            # MessageBoxW displays a message box with a given title and message
            # arg 2 is the message, arg 3 is the title
            return False
        return True
   def TypeCheck(value) -> bool:
        # checks if the grade is of the correct DataType (this case, an integer)
        # in the instance of a float, it just floors the value (18.95 becomes 18)
        try:
            value = int(value)
            return True
        except:
            ctypes.windll.user32.MessageBoxW(None, u'Invalid input.', u'Error', None)
            return False
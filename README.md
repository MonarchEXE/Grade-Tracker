# Grade-Tracker
Class project, if you managed to find this then just ignore :/

json file in .vscode is just to debug the program on a cmd terminal instead of the integrated one
in vs code. The four files listed below are the only ones of importance

File purposes:
.gitignore       - list of files and directories that are ignored by git in commits
GradeTracker     - contains functions handling main program features
                   (creating student dictionaries, altering grades, averaging, etc.)
                   note: I *would* put the functions into classes w/ related titles
                   but that means extra boilerplate. no thx
InputValidation  - handles the validation of user inputs (the ones that aren't pre-
                   defined i.e. subject grades)
FileSave         - handles saving student data to a json file. Also handles updating 
                   currentStudents to contain previous data.
Prog             - the cmd UI of the program (not actually the main program)
                   handles user input  


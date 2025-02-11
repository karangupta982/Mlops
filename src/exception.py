# import sys


# def error_message_detail(error,error_detail:sys):
#     _,_,exc_tb=error_detail.exec_info()
#     file_name=exc_tb.tb_frame.f_code.co_filename
#     error_message="Error occured in python script name [{0}] line number [{1}] error message [{2}] "
#     file_name,exc_tb.tb_lineno,str(error)


 
import sys
from src.logger import logging

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
     file_name,exc_tb.tb_lineno,str(error))

    return error_message

    

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)   #inheriting the properties of parent class which is Exception
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
    
    def __str__(self):
        return self.error_message
    


# if __name__=="__main__":

#     try:
#         a =1/0
#     except Exception as e:
#         logging.info("Divide by zero error")
#         raise CustomException(e)




# import sys: This imports the sys module, which provides access to some variables used or maintained by the Python interpreter and to functions that interact strongly with the interpreter.
# from src.logger import logging: This imports the logging object from the logger module located in the src directory. This is typically used for logging messages.
# def error_message_detail(error, error_detail: sys):: This defines a function named error_message_detail that takes two parameters: error and error_detail. The error_detail parameter is expected to be of type sys.
# _, _, exc_tb = error_detail.exc_info():: This line calls the exc_info() method from the error_detail (which is the sys module) to get information about the most recent exception caught by an except clause. It returns a tuple of three values: the exception type, the exception value, and a traceback object. The first two values are ignored (hence the underscores), and the traceback object is assigned to exc_tb.
# file_name = exc_tb.tb_frame.f_code.co_filename: This retrieves the filename where the exception occurred from the traceback object. exc_tb.tb_frame.f_code.co_filename accesses the code object associated with the traceback frame and gets the filename attribute.
# error_message = "Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(file_name, exc_tb.tb_lineno, str(error)): This constructs an error message string using the filename, line number, and the error message. exc_tb.tb_lineno gives the line number where the exception occurred, and str(error) converts the error to a string.
# return error_message: This returns the constructed error message string.
# class CustomException(Exception):: This defines a custom exception class named CustomException that inherits from the built-in Exception class.
# def __init__(self, error_message, error_detail: sys):: This is the initializer method for the CustomException class. It takes two parameters: error_message and error_detail.
# super().__init__(error_message): This calls the initializer of the base Exception class with the error_message.
# self.error_message = error_message_detail(error_message, error_detail=error_detail): This calls the error_message_detail function to get a detailed error message and assigns it to the error_message attribute of the CustomException instance.
# def __str__(self):: This defines the __str__ method for the CustomException class, which is called when the exception is converted to a string.
# return self.error_message: This returns the detailed error message when the exception is converted to a string.
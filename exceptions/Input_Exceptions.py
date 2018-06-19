'''
Created on Sep 28, 2015

@author: Riddhita.Sarcar
'''

'''
This class contains all the exceptions related to invalid input
'''

class InvalidInputException(Exception):
    def __init__(self):
        super().__init__("Please enter a valid input")
        



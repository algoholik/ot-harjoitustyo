'''
All-around utility functions module
'''
import os

def get_file_path(filename: str):
    '''
    Return given filename:str with a full filesystem path to it
    '''
    cwd = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    return os.path.join(cwd, filename)

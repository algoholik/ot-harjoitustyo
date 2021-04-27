'''
Module for Note class
'''
from datetime import datetime

class Note:
    '''-------------------------------------------------------------------------------------
    Note class
    -------------------------------------------------------------------------------------'''
    def __init__(self, n_id: int, n_name: str, n_content: str, n_timestamp: datetime):
        '''---------------------------------------------------------------------------------
        Initialize Note object with parameters:
        ---------------------------------------------------------------------------------'''
        self.n_id           = n_id          #int: unique note id generated in database
        self.n_name         = n_name        #str: note name
        self.n_content      = n_content     #str: note content
        self.n_timestamp    = n_timestamp   #obj: datetime object of time last modified

    def get_id(self) -> int:
        ''' Return note id (int) '''
        return self.n_id

    def get_name(self) -> str:
        ''' Return note name (str) '''
        return self.n_name

    def get_content(self) -> str:
        ''' Return note content (str) '''
        return self.n_content

    def get_timestamp(self) -> datetime:
        ''' Return note time last modified (datetime object) '''
        return self.n_timestamp

    def set_id(self, n_id: int):
        ''' Set note id '''
        self.n_id = n_id

    def set_name(self, n_name: str):
        ''' Set note name (str) '''
        self.n_name = n_name

    def set_content(self, n_content: str):
        ''' Set note content (str) '''
        self.n_content = n_content

    def set_timestamp(self, n_timestamp: datetime):
        ''' Set note time last modified (datetime object) '''
        self.n_timestamp = n_timestamp

    def __str__(self):
        ''' Note object __str__ '''
        return f"{self.n_id}\n{self.n_name}\n{self.n_content}\n{self.n_timestamp}"

    def __repr__(self):
        ''' Note object __repr__ '''
        return f"{self.n_id}\n{self.n_name}\n{self.n_content}\n{self.n_timestamp}"

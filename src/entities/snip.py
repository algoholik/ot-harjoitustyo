'''
Module for Snip class
'''
from datetime import datetime

class Snip:
    '''-------------------------------------------------------------------------------------
    Snip class
    -------------------------------------------------------------------------------------'''
    def __init__(self, s_id: int, s_name: str, s_content: str, s_timestamp: datetime):
        '''---------------------------------------------------------------------------------
        Initialize Snip object with parameters:
        ---------------------------------------------------------------------------------'''
        self.s_id           = s_id          #int: unique snip id generated in database
        self.s_name         = s_name        #str: snip name
        self.s_content      = s_content     #str: snip content
        self.s_timestamp    = s_timestamp   #obj: datetime object of time last modified

    def get_id(self):
        ''' Return snippet id (int) '''
        return self.s_id

    def get_name(self):
        ''' Return snip name (str) '''
        return self.s_name

    def get_content(self):
        ''' Return snip content (str) '''
        return self.s_content

    def get_timestamp(self):
        ''' Return snip time last modified (datetime object) '''
        return self.s_timestamp

    def set_id(self, s_id: int):
        ''' Set snip id '''
        self.s_id = s_id

    def set_name(self, s_name: str):
        ''' Set snip name (str) '''
        self.s_name = s_name

    def set_content(self, s_content: str):
        ''' Set snip content (str) '''
        self.s_content = s_content

    def set_timestamp(self, s_timestamp: datetime):
        ''' Set snip time last modified (datetime object) '''
        self.s_timestamp = s_timestamp

    def __str__(self):
        ''' Snip object __str__ '''
        return f"{self.s_id}\n{self.s_name}\n{self.s_content}\n{self.s_timestamp}"

    def __repr__(self):
        ''' Snip object __repr__ '''
        return f"{self.s_id}\n{self.s_name}\n{self.s_content}\n{self.s_timestamp}"

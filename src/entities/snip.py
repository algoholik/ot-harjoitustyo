'''
Module for Snip class
'''
from datetime import datetime

class Snip:
    '''-------------------------------------------------------------------------------------
    Snip class
    -------------------------------------------------------------------------------------'''
    def __init__(
        self, 
        sid: int, 
        sniptype: int, 
        content: str, 
        modified: datetime
        ):
        '''---------------------------------------------------------------------------------
        Initialize Snip object with parameters:
        ---------------------------------------------------------------------------------'''
        self.sid:       int         = sid          #int: unique snip id generated in database
        self.sniptype:  int         = sniptype        #str: snip name
        self.content:   str         = content     #str: snip content
        self.modified:  datetime    = modified   #obj: datetime object of time last modified

    def get_id(self) -> int:
        ''' Return snippet id (int) '''
        return self.sid

    def get_sniptype(self) -> int:
        ''' Return snip name (str) '''
        return self.sniptype

    def get_content(self) -> str:
        ''' Return snip content (str) '''
        return self.content

    def get_modified(self) -> datetime:
        ''' Return snip time last modified (datetime object) '''
        return self.modified

    def set_id(self, sid: int) -> None:
        ''' Set snip id '''
        self.sid = int(sid)

    def set_sniptype(self, sniptype: int) -> None:
        ''' Set snip name (str) '''
        self.sniptype = sniptype

    def set_content(self, content: str) -> None:
        ''' Set snip content (str) '''
        self.content = str(content)

    def set_timestamp(self, modified: datetime) -> None:
        ''' Set snip time last modified (datetime object) '''
        self.modified = modified

    def __str__(self) -> str:
        ''' Snip object __str__ '''
        return f"Snip #{str(self.sid)} Type: {self.sniptype} Modified: {str(self.modified)}\n{self.content}\n"

    def __repr__(self) -> str:
        ''' Snip object __repr__ '''
        return f"Snip #{str(self.sid)} Type: {self.sniptype} Modified: {str(self.modified)}\n{self.content}\n"

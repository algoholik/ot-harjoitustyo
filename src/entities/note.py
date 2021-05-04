'''
Module for Note class
'''
from datetime import datetime
from entities.snip import Snip

class Note:
    '''-------------------------------------------------------------------------------------
    Note class
    -------------------------------------------------------------------------------------'''
    def __init__(
        self,
        nid: int,
        title: str,
        contents: list,
        modified: datetime
        ):
        '''---------------------------------------------------------------------------------
        Initialize Note object with parameters:
        ---------------------------------------------------------------------------------'''
        self.nid:       int         = nid           #int: unique note id generated in database
        self.title:     str         = title         #str: note name
        self.contents:  list        = contents      #str: note content
        self.modified:  datetime    = modified      #obj: datetime object of time last modified

    def get_id(self) -> int:
        ''' Return note id (int) '''
        return self.nid

    def get_title(self) -> str:
        ''' Return note name (str) '''
        return self.title

    def get_contents(self) -> list:
        ''' Return note content (str) '''
        return self.contents

    def get_modified(self) -> datetime:
        ''' Return note time last modified (datetime object) '''
        return self.modified

    def set_id(self, nid: int) -> None:
        ''' Set note id '''
        self.nid = nid

    def set_title(self, title: str) -> None:
        ''' Set note name (str) '''
        self.title = title

    def set_contents(self, contents: list) -> None:
        ''' Set note content (str) '''
        self.contents = contents

    def set_modified(self, modified: datetime) -> None:
        ''' Set note time last modified (datetime object) '''
        self.modified = modified

    def add_content(self, new_content: Snip) -> None:
        ''' Add snip object to the note object snip list. '''
        self.contents.append(new_content)

    def __str__(self) -> str:
        ''' Note object __str__ '''
        note_header = f"Note #{str(self.nid)} Title: {self.title} ({str(self.modified)})\n"
        output = note_header + "\n".join([str(snip) for snip in self.contents])
        return f"{output}"

    def __repr__(self) -> str:
        ''' Note object __repr__ '''
        note_header = f"Note #{str(self.nid)} Title: {self.title} ({str(self.modified)})\n"
        output = note_header + "\n- ".join([str(snip) for snip in self.contents])
        return f"{output}"

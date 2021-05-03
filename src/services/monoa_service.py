'''
Main module for handling notes and snips between UI and DB
- provides up-to-date lists of snips and notes
- keeps the lists sorted by timestamp, latest first
'''
from collections import OrderedDict
from datetime import datetime
from entities.note import Note
from entities.snip import Snip
import database.db_handler as db_handler

class MonoaService:
    '''
    Main content handler class
    '''
    def __init__(self):
        ''' Load all notes and snippets to lists '''
        self.notes = list()
        self.snip_dict = OrderedDict()
        self.note_dict = OrderedDict()
        self._load_notes()
        self._autocreate_note_if_none()

    def create_note(self, title: str) -> Note:
        ''' Create new note: '''
        init_snip = self.create_snip("")
        snip_list = ";".join([str(init_snip.get_id())])
        note = db_handler.create_note(title, snip_list, datetime.now())
        self.note_dict[note['id']] =    Note(
                                            note['id'],
                                            note['title'],
                                            note['contents'],
                                            note['modified']
                                        )
        self._load_notes()
        return self.get_note_by_id(note['id'])

    def create_snip(self, content: str) -> Snip:
        ''' Create new snip. '''
        snip = db_handler.create_snip(0, content, datetime.now())
        self.snip_dict[snip['id']] =    Snip(
                                            snip['id'],
                                            snip['sniptype'],
                                            snip['content'],
                                            snip['modified']
                                        )
        self._load_snips()
        return self.get_snip_by_id(snip['id'])

    def create_snip_inside_note(self, note_id: int) -> Snip:
        snip = self.create_snip("")
        self.note_dict.get(note_id).add_content(snip)
        self.update_note(self.get_note_by_id(note_id))
        return snip

    def get_note_by_id(self, id: int) -> Note:
        ''' Return note by id '''
        return self.note_dict.get(id)

    def get_snip_by_id(self, id: int) -> Snip:
        ''' Return snip by id '''
        return self.snip_dict.get(id)

    def update_note(self, note: Note) -> None:
        ''' Update note in database '''
        contents = []
        for snip in note.get_contents():
            contents.append(str(snip.get_id()))
        db_handler.update_note(
            note.get_id(),
            note.get_title(),
            contents,
            note.get_modified()
        )
        self._load_notes()
        self._sort_notes()

    def get_notes(self) -> list:
        ''' Return notes '''
        if len(self.note_dict) == 0:
            self.create_note("")
            self._load_notes()
        return list(self.note_dict.values())

    def get_snips(self) -> list:
        ''' Return notes '''
        return list(self.snip_dict.values())

    def get_latest_note_id(self) -> int:
        return max(self.note_dict)

    def get_latest_note(self) -> Note:
        note_id = next(reversed(self.note_dict))
        return self.note_dict.get(note_id)

    def _load_notes(self) -> None:
        ''' Load all notes from database. '''
        self._load_snips()
        for note in db_handler.load_notes():
            snips = [self.get_snip_by_id(int(snip)) for snip in note['contents'].split(";")]
            self.note_dict[note['id']] =    Note(
                                                note['id'],
                                                note['title'],
                                                snips,
                                                note['modified']
                                            )

    def _load_snips(self) -> None:
        ''' Load all snips from database. '''
        for snip in db_handler.load_snips():
            self.snip_dict[snip['id']] =    Snip(
                                                snip['id'],
                                                snip['sniptype'],
                                                snip['content'],
                                                snip['modified']
                                            )

    def _autocreate_note_if_none(self) -> None:
        if len(self.note_dict) == 0:
            self.create_note("")

    def _sort_notes(self) -> None:
        ''' Keep self.notes sorted descending by the timestamp'''
        notes_sortable = OrderedDict()
        for key, value in self.note_dict.items():
            notes_sortable[value.get_modified()] = value
        for key, value in sorted(notes_sortable.items(), reverse=True):
            self.note_dict[key] = value

    def _sort_snips(self) -> None:
        ''' Keep self.snips sorted descending by the timestamp'''
        snips_sortable = OrderedDict()
        for key, value in self.snip_dict.items():
            snips_sortable[value.get_modified()] = value
        for key, value in sorted(snips_sortable.items(), reverse=True):
            self.snip_dict[key] = value

    def update_snip(self, snip: Snip) -> None:
        ''' Update snip by the given id '''
        db_handler.update_snip(
            snip.get_id(),
            snip.get_sniptype(),
            snip.get_content(),
            datetime.now()
        )
        self._load_snips()
        self._sort_snips()

    """

    def get_snips(self):
        ''' Return list of snippets '''
        return self.snips

    def get_snip_by_id(self, s_id: int):
        ''' Return snippet by id '''
        result = None
        for snip in self.snips:
            if snip.get_id() == s_id:
                result = snip
        return result

    def _load_snips(self) -> None:
        ''' Load snippets from database repository '''
        snips = db_handler.load_snips()
        for snip in snips:
            self.snips.append(
                Snip(snip['id'], snip['name'], snip['content'], snip['timestamp'])
            )
        self._sort_snips()

    def _sort_snips(self) -> None:
        ''' Keep self.snips sorted descending by the timestamp'''
        snips_sortable = dict()
        for snip in self.snips:
            snips_sortable[snip.get_timestamp()] = snip
        self.snips.clear()
        for key, value in sorted(snips_sortable.items(), reverse=True):
            self.snips.append(value)
    """

# One and only instance of this class
monoa_service = MonoaService()

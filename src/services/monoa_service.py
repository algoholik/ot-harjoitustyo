from entities.snippet import Snippet
from entities.note import Note
import database.db_handler as db_handler

# Set the default content for a new snippet
default_snippet_content = ""


class MonoaService:
    def __init__(self):
        self.snippets = []
        
        for item in db_handler.load_snippets():
            self.snippets.append(Snippet(item['id'], item['snippet'], item['updated']))

        if len(self.snippets) == 0:
            snippet = db_handler.create_snippet(default_snippet_content)
            self.snippets.append(Snippet(snippet[0], snippet[1], snippet[2]))

    def create_snippet(self, content: str):
        snippet = db_handler.create_snippet(content)
        self.snippets.append(Snippet(snippet[0], snippet[1], snippet[2]))

    def update_snippet(self, id: int, content: str):
        return db_handler.update_snippet(id, content)

    def get_snippets(self):
        return self.snippets
    
    def get_snippet(self, id: int):
        result = None
        for snippet in self.snippets:
            if snippet.get_id() == id:
                result = snippet
        return result


# Init MonoaService for global access
m_service = MonoaService()


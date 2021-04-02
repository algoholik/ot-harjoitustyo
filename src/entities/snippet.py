from datetime import datetime

class Snippet:
    def __init__(self, id:int, snippet:str):
        self.id = id
        self.snippet = snippet

    def __str__(self):
        return f"snippet {self.id}: {self.snippet}"

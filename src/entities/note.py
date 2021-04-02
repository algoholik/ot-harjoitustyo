class Note:
    def __init__(self, id:int, content:str):
        self.id = id
        self.content = content

    def __str__(self):
        return f"note {self.id}: {self.content}"

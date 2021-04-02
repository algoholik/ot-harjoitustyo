from tkinter import Tk, ttk, constants, StringVar
from services.monoa_service import m_service

class UI:
    def __init__(self, root):
        self._root = root
        #self._current_view = None

    def start(self):
        def _create_snippet():
            m_service.create_snippet(entry.get())

        def _get_snippets():
            m_service.get_snippets()


        entry = ttk.Entry(master=self._root)
        button = ttk.Button(master=self._root, text="Create snippet", command=_create_snippet)
        button2 = ttk.Button(master=self._root, text="Print", command=_get_snippets)

        entry.pack()
        button.pack()
        button2.pack()

        entry.focus_set()


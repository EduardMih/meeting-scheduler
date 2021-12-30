import tkinter as tk

title_font = "Helvetica 15 bold"


class Page:
    """
    Generic class for a page to be inherited by all the others pages in application.
    """
    def __init__(self, parent):
        """
        Page class constructor to initialize the object.
        :param parent: Parent frame.
        """
        self.container = tk.Frame(parent, bg="grey")

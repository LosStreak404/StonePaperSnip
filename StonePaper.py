from typing import Optional, Tuple, Union
import customtkinter as CTk

class Application(CTk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x400")
        self.resizable(False, False)





if __name__ == "__main__":
    app = Application()
    app.mainloop()
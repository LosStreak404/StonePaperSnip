from typing import Optional, Tuple, Union
import customtkinter as CTk

class Application(CTk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x400")
        self.resizable(False, False)

        self.massage_frame = CTk.CTkFrame(master=self, 
                                          width=100, 
                                          height=30, 
                                          corner_radius=3,
                                          fg_color="transparent")
        self.massage_frame.grid(row=1, 
                                column=0, 
                                sticky="nsew", 
                                padx=10, pady=10)
        self.message_entry = CTk.CTkEntry(master=self.message_frame,
                                          width=90,
                                          height=25,
                                          corner_radius=5) 




if __name__ == "__main__":
    app = Application()
    app.mainloop()
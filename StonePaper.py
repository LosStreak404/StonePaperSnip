from typing import Optional, Tuple, Union
import customtkinter as CTk

class Application(CTk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x400")
        self.resizable(False, False)

        self.message_frame = CTk.CTkFrame(master=self, 
                                          width=300, 
                                          height=30, 
                                          corner_radius=3,
                                          fg_color="transparent")
        
        self.message_frame.grid(row=1, 
                                column=0, 
                                sticky="nsew", 
                                padx=10, pady=10)
        
        self.message_entry = CTk.CTkEntry(master=self.message_frame,
                                          width=370,
                                          height=25,
                                          corner_radius=5,
                                          fg_color="transparent") 

        self.message_entry.grid(row=1, 
                                column=0,
                                sticky="nsew",
                                padx=5, pady=5)



if __name__ == "__main__":
    app = Application()
    app.mainloop()
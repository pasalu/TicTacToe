from Tkinter import Frame, Button
import BoardUI
from AI import AI


class Menu(Frame):
    BUTTON_WIDTH = 50

    def __init__(self, master, controller):
        """
        Main menu for selecting game modes.
        :param master: The root of the TK widget.
        :param controller: The class that handles switching between frames.
        """
        Frame.__init__(self, master)

        self.master = master
        self.controller = controller

        self.multiplayer = Button(
            self,
            text="Multiplayer",
            width=self.BUTTON_WIDTH,
            command=lambda: self.select_mode(None)
        )
        self.multiplayer.grid(column=0, row=0)

        self.random_ai = Button(
            self,
            text="Versus Random AI",
            width=self.BUTTON_WIDTH,
            command=lambda: self.select_mode(AI.RANDOM))
        self.random_ai.grid(column=0, row=1)

        self.a_star_ai = Button(self, text="Versus A* AI", width=self.BUTTON_WIDTH)
        self.a_star_ai.grid(column=0, row=2)

    def select_mode(self, ai_strategy):
        class_name = BoardUI.__name__.split('.')[-1]  # module.class_name
        self.controller.show_frame(class_name, ai_strategy)

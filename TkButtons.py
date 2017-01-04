# Tests using buttons from Tkinter. Taken from
# http://effbot.org/tkinterbook/tkinter-hello-again.htm

from Tkinter import *

class App:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.button = Button(
                frame,
                text = "QUIT",
                fg = "red",
                command = frame.quit
        )
        self.button.pack(side = LEFT)

        self.hi_there = Button(frame, text = "Hello", command = self.say_hi)
        self.hi_there.pack(side = LEFT)

    def say_hi(self):
        print "Hi there, everyone!"

def main():
    root = Tk()

    app = App(root)

    root.mainloop()
    root.destroy()

if __name__ == "__main__":
    main()

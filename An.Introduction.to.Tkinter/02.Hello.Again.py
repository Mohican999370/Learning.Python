__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = ''
__version__ = '1.0'

from tkinter import *


class App:
    def __init__(self, master: Tk):
        master.title('Hello Again')

        frame = Frame(master)
        frame.pack()

        self.btn_quit = Button(
            master=frame,
            text='Quit',
            fg='red',
            command=frame.quit
        )
        self.btn_quit.pack(side=LEFT)

        self.btn_hello = Button(
            master=frame,
            text='Say Hello',
            command=self.btn_hello_clicked
        )
        self.btn_hello.pack(side=LEFT)

    def btn_hello_clicked(self) -> None:
        print("Hello everyone")
        return


window = Tk()
app = App(window)

window.mainloop()
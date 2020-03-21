import tkinter
from  tkinter import Button, Entry


class MainWindow(tkinter.Frame):
    def __init__(self, master, **kw):
        super(MainWindow, self).__init__(master, **kw)
        self.grid(columnspan=4, ipadx=70)
        self.principal = tkinter.DoubleVar()
        self.principal.set(1000.0)
        self.rate = tkinter.DoubleVar()
        self.rate.set(5.0)
        self.years = tkinter.IntVar()
        self.expression = ''
        self.equation = tkinter.StringVar()
        expression_field = Entry(master, textvariable=self.equation)

        expression_field.grid(columnspan=4, ipadx=70)

        button1 = Button(master, text=' 1 ', fg='black', bg='red',
                         command=lambda: self.press(1), height=1, width=7)
        button1.grid(row=2, column=0)

        button2 = Button(master, text=' 2 ', fg='black', bg='red',
                         command=lambda: self.press(2), height=1, width=7)
        button2.grid(row=2, column=1)

        button3 = Button(master, text=' 3 ', fg='black', bg='red',
                         command=lambda: self.press(3), height=1, width=7)
        button3.grid(row=2, column=2)

        button4 = Button(master, text=' 4 ', fg='black', bg='red',
                         command=lambda: self.press(4), height=1, width=7)
        button4.grid(row=3, column=0)

        button5 = Button(master, text=' 5 ', fg='black', bg='red',
                         command=lambda: self.press(5), height=1, width=7)
        button5.grid(row=3, column=1)

        button6 = Button(master, text=' 6 ', fg='black', bg='red',
                         command=lambda: self.press(6), height=1, width=7)
        button6.grid(row=3, column=2)

        button7 = Button(master, text=' 7 ', fg='black', bg='red',
                         command=lambda: self.press(7), height=1, width=7)
        button7.grid(row=4, column=0)

        button8 = Button(master, text=' 8 ', fg='black', bg='red',
                         command=lambda: self.press(8), height=1, width=7)
        button8.grid(row=4, column=1)

        button9 = Button(master, text=' 9 ', fg='black', bg='red',
                         command=lambda: self.press(9), height=1, width=7)
        button9.grid(row=4, column=2)

        button0 = Button(master, text=' 0 ', fg='black', bg='red',
                         command=lambda: self.press(0), height=1, width=7)
        button0.grid(row=5, column=0)

        plus = Button(master, text=' + ', fg='black', bg='red',
                      command=lambda: self.press("+"), height=1, width=7)
        plus.grid(row=2, column=3)

        minus = Button(master, text=' - ', fg='black', bg='red',
                       command=lambda: self.press("-"), height=1, width=7)
        minus.grid(row=3, column=3)

        multiply = Button(master, text=' * ', fg='black', bg='red',
                          command=lambda: self.press("*"), height=1, width=7)
        multiply.grid(row=4, column=3)

        divide = Button(master, text=' / ', fg='black', bg='red',
                        command=lambda: self.press("/"), height=1, width=7)
        divide.grid(row=5, column=3)

        equal = Button(master, text=' = ', fg='black', bg='red',
                       command=self.equalpress, height=1, width=7)
        equal.grid(row=5, column=2)

        clear = Button(master, text='Clear', fg='black', bg='red',
                       command=self.clear, height=1, width=7)
        clear.grid(row=5, column='1')

    def clear(self):
        self.expression = ""
        self.equation.set("")

    def press(self, num):
        self.expression = self.expression + str(num)
        self.equation.set(self.expression)

    def equalpress(self):
        try:
            total = str(eval(self.expression))
            self.equation.set(total)
            self.expression = ""
        except:
            self.equation.set(" error ")
            self.expression = ""


if __name__ == '__main__':
    application = tkinter.Tk()
    application.title("Calc")
    window = MainWindow(application)
    application.protocol("WM_DELETE_WINDOW", window.quit)
    application.mainloop()
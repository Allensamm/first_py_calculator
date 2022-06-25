from tkinter import *


def buttonClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_input.set(operator)


def buttonClearDisplay():
    global operator
    operator = ""
    text_input.set("")


def buttonEqual():
    global operator
    sum = str(eval(operator))
    text_input.set(sum)
    operator = ""


"""def hello():
    global operator
    h = input('...')
    text_input.set(h)"""


cal = Tk()
cal.title('calculator')
operator = ""
text_input = StringVar('')

textdisplay = Entry(cal, font=('arial', 20, 'bold'),
                    textvariable=text_input, bd=30, insertwidth=4,
                    bg='grey', justify='right').grid(columnspan=4)

button7 = Button(cal, padx=16, bd=8, fg='black', font=('arial',
                                                       20, 'bold'), text='7', bg='grey',
                 command=lambda: buttonClick(7)).grid(row=1, column=0)

button8 = Button(cal, padx=16, bd=8, fg='black', font=('arial',
                                                       20, 'bold'), text='8', bg='grey',
                 command=lambda: buttonClick(8)).grid(row=1, column=1)

button9 = Button(cal, padx=16, bd=8, fg='black', font=('arial',
                                                       20, 'bold'), text='9', bg='grey',
                 command=lambda: buttonClick(9)).grid(row=1, column=2)

Addition = Button(cal, padx=16, bd=8, fg='black', font=('arial',
                                                        20, 'bold'), text='+', bg='grey',
                  command=lambda: buttonClick('+')).grid(row=1, column=3)
# ==============================================================================================================
button4 = Button(cal, padx=16, bd=8, fg='black', font=('arial',
                                                       20, 'bold'), text='4', bg='grey',
                 command=lambda: buttonClick(4)).grid(row=2, column=0)

button5 = Button(cal, padx=16, bd=8, fg='black', font=('arial',
                                                       20, 'bold'), text='5', bg='grey',
                 command=lambda: buttonClick(5)).grid(row=2, column=1)

button6 = Button(cal, padx=16, bd=8, fg='black', font=('arial',
                                                       20, 'bold'), text='6', bg='grey',
                 command=lambda: buttonClick(6)).grid(row=2, column=2)

subtraction = Button(cal, padx=16, bd=8, fg='black', font=('arial',
                                                           20, 'bold'), text='-', bg='grey',
                     command=lambda: buttonClick('-')).grid(row=2, column=3)
# ==============================================================================================================
button1 = Button(cal, padx=16, bd=8, fg='black', font=('arial',
                                                       20, 'bold'), text='1', bg='grey',
                 command=lambda: buttonClick(1)).grid(row=3, column=0)

button2 = Button(cal, padx=16, bd=8, fg='black', font=('arial',
                                                       20, 'bold'), text='2', bg='grey',
                 command=lambda: buttonClick(2)).grid(row=3, column=1)

button3 = Button(cal, padx=16, bd=8, fg='black', font=('arial',
                                                       20, 'bold'), text='3', bg='grey',
                 command=lambda: buttonClick(3)).grid(row=3, column=2)

multiply = Button(cal, padx=16, bd=8, fg='black', font=('arial',
                                                        20, 'bold'), text='*', bg='grey',
                  command=lambda: buttonClick('*')).grid(row=3, column=3)

button0 = Button(cal, padx=16, bd=8, fg='black', font=('arial',
                                                       20, 'bold'), text='0', bg='grey',
                 command=lambda: buttonClick(0)).grid(row=4, column=0)

buttonclear = Button(cal, padx=16, bd=8, fg='black', font=('arial',
                                                           20, 'bold'), text='C', bg='grey',
                     command=buttonClearDisplay).grid(row=4, column=1)

buttonequal = Button(cal, padx=16, bd=8, fg='black', font=('arial',
                                                           20, 'bold'), text='=', bg='grey', command=buttonEqual).grid(
    row=4, column=2)

devide = Button(cal, padx=16, bd=8, fg='black', font=('arial',
                                                      20, 'bold'), text='/', bg='grey',
                command=lambda: buttonClick('/')).grid(row=4, column=3)
"""h = Button(cal, padx=16, bd=8, fg='black', font=('arial',
                                                      20, 'bold'), text='+-', bg='grey',
                command=lambda: buttonClick('+-')).grid(row=4, column=4)"""

cal.mainloop()

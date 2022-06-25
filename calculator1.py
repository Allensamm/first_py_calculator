from tkinter import *
root = Tk()
root.title('calculator')
operator = ''
text_input = StringVar('')

textdisplay = Entry(root, font=('arial', 20, 'bold'),
                    textvariable=text_input, bd=10, insertwidth=5,
                    bg='grey', justify='right').grid(columnspan=4)

def button_clicked(numbers):
    global operator
    operator = operator + str(numbers)
    text_input.set(operator)

def button_clear():
    global operator
    operator = ''
    text_input = ('')

def button_equal():
    global operator
    sum = str(eval(operator))
    text_input.set(sum)
    operator = ''


button7 = Button(root, padx=16, bd=8, fg='black', font=('arial',20, 'bold'), text='7', bg='grey',
command=lambda: button_clicked(7)).grid(row=1, column=0)

button8 = Button(root, padx=16, bd=8, fg='black', font=('arial',20, 'bold'), text='8', bg='grey',
command=lambda: button_clicked(8)).grid(row=1, column=1)

button9 = Button(root, padx=16, bd=8, fg='black', font=('arial',20, 'bold'), text='9', bg='grey',
command=lambda: button_clicked(9)).grid(row=1, column=2)

button_add = Button(root, padx=16, bd=8, fg='black', font=('arial',20, 'bold'), text='+', bg='grey',
command=lambda: button_clicked('+')).grid(row=1, column=3)



button4 = Button(root, padx=16, bd=8, fg='black', font=('arial',20, 'bold'), text='4', bg='grey',
command=lambda: button_clicked(4)).grid(row=2, column=0)

button5 = Button(root, padx=16, bd=8, fg='black', font=('arial',20, 'bold'), text='5', bg='grey',
command=lambda: button_clicked(5)).grid(row=2, column=1)

button6 = Button(root, padx=16, bd=8, fg='black', font=('arial',20, 'bold'), text='6', bg='grey',
command=lambda: button_clicked(6)).grid(row=2, column=2)

button_minus = Button(root, padx=16, bd=8, fg='black', font=('arial',20, 'bold'), text='-', bg='grey',
command=lambda: button_clicked('-')).grid(row=2, column=3)



button1 = Button(root, padx=16, bd=8, fg='black', font=('arial',20, 'bold'), text='1', bg='grey',
command=lambda: button_clicked(1)).grid(row=3, column=0)

button2 = Button(root, padx=16, bd=8, fg='black', font=('arial',20, 'bold'), text='2', bg='grey',
command=lambda: button_clicked(2)).grid(row=3, column=1)

button3 = Button(root, padx=16, bd=8, fg='black', font=('arial',20, 'bold'), text='3', bg='grey',
command=lambda: button_clicked(3)).grid(row=3, column=2)

button_times = Button(root, padx=16, bd=8, fg='black', font=('arial',20, 'bold'), text='*', bg='grey',
command=lambda: button_clicked('*')).grid(row=3, column=3)



button_clear = Button(root, padx=16, bd=8, fg='black', font=('arial',20, 'bold'), text='c', bg='grey',
command=button_clear).grid(row=4, column=1)

from tkinter import *
root = Tk()
root.title('calculator')
operator = ''
text_input = StringVar('')

textdisplay = Entry(root, font=('arial', 20, 'bold'),
                    textvariable=text_input, bd=10, insertwidth=5,
                    bg='grey', justify='right').grid(columnspan=4)

def button_clicked(numbers):
    global operator
    operator = operator + str(numbers)
    text_input.set(operator)

def button_clear():
    global operator
    operator = ''
    text_input = ('')

def button_equal():
    global operator
    sum = str(eval(operator))
    text_input.set(sum)
    operator = ''


button7 = Button(root, padx=16, bd=8, fg='black', font=('arial',20, 'bold'), text='7', bg='grey',
command=lambda: button_clicked(7)).grid(row=1, column=0)

button8 = Button(root, padx=16, bd=8, fg='black', font=('arial',20, 'bold'), text='8', bg='grey',
command=lambda: button_clicked(8)).grid(row=1, column=0)

button9 = Button(root, padx=16, bd=8, fg='black', font=('arial',20, 'bold'), text='9', bg='grey',
command=lambda: button_clicked(9)).grid(row=1, column=0)

button_add = Button(root, padx=16, bd=8, fg='black', font=('arial',20, 'bold'), text='+', bg='grey',
command=lambda: button_clicked('+')).grid(row=1, column=0)



button4 = Button(root, padx=16, bd=8, fg='black', font=('arial',20, 'bold'), text='4', bg='grey',
command=lambda: button_clicked(4)).grid(row=1, column=0)

button5 = Button(root, padx=16, bd=8, fg='black', font=('arial',20, 'bold'), text='5', bg='grey',
command=lambda: button_clicked(5)).grid(row=1, column=0)

button6 = Button(root, padx=16, bd=8, fg='black', font=('arial',20, 'bold'), text='6', bg='grey',
command=lambda: button_clicked(6)).grid(row=1, column=0)

button_minus = Button(root, padx=16, bd=8, fg='black', font=('arial',20, 'bold'), text='-', bg='grey',
command=lambda: button_clicked('-')).grid(row=1, column=0)



button1 = Button(root, padx=16, bd=8, fg='black', font=('arial',20, 'bold'), text='1', bg='grey',
command=lambda: button_clicked(1)).grid(row=1, column=0)

button2 = Button(root, padx=16, bd=8, fg='black', font=('arial',20, 'bold'), text='2', bg='grey',
command=lambda: button_clicked(2)).grid(row=1, column=0)

button3 = Button(root, padx=16, bd=8, fg='black', font=('arial',20, 'bold'), text='3', bg='grey',
command=lambda: button_clicked(3)).grid(row=1, column=0)

button_times = Button(root, padx=16, bd=8, fg='black', font=('arial',20, 'bold'), text='*', bg='grey',
command=lambda: button_clicked('*')).grid(row=1, column=0)



button_clear = Button(root, padx=16, bd=8, fg='black', font=('arial',20, 'bold'), text='c', bg='grey',
command=button_clear).grid(row=1, column=0)

from tkinter import *
root = Tk()
root.title('calculator')
operator = ''
text_input = StringVar('')

textdisplay = Entry(root, font=('arial', 20, 'bold'),
                    textvariable=text_input, bd=10, insertwidth=5,
                    bg='grey', justify='right').grid(columnspan=4)

def button_clicked(numbers):
    global operator
    operator = operator + str(numbers)
    text_input.set(operator)

def button_clear():
    global operator
    operator = ''
    text_input = ('')

def button_equal():
    global operator
    sum = str(eval(operator))
    text_input.set(sum)
    operator = ''


button7 = Button(root, padx=16, bd=8, fg='black', font=('arial',20, 'bold'), text='7', bg='grey',
command=lambda: button_clicked(7)).grid(row=1, column=0)

button8 = Button(root, padx=16, bd=8, fg='black', font=('arial',20, 'bold'), text='8', bg='grey',
command=lambda: button_clicked(8)).grid(row=1, column=0)

button9 = Button(root, padx=16, bd=8, fg='black', font=('arial',20, 'bold'), text='9', bg='grey',
command=lambda: button_clicked(9)).grid(row=1, column=0)

button_add = Button(root, padx=16, bd=8, fg='black', font=('arial',20, 'bold'), text='+', bg='grey',
command=lambda: button_clicked('+')).grid(row=1, column=0)



button4 = Button(root, padx=16, bd=8, fg='black', font=('arial',20, 'bold'), text='4', bg='grey',
command=lambda: button_clicked(4)).grid(row=1, column=0)

button5 = Button(root, padx=16, bd=8, fg='black', font=('arial',20, 'bold'), text='5', bg='grey',
command=lambda: button_clicked(5)).grid(row=1, column=0)

button6 = Button(root, padx=16, bd=8, fg='black', font=('arial',20, 'bold'), text='6', bg='grey',
command=lambda: button_clicked(6)).grid(row=1, column=0)

button_minus = Button(root, padx=16, bd=8, fg='black', font=('arial',20, 'bold'), text='-', bg='grey',
command=lambda: button_clicked('-')).grid(row=1, column=0)



button1 = Button(root, padx=16, bd=8, fg='black', font=('arial',20, 'bold'), text='1', bg='grey',
command=lambda: button_clicked(1)).grid(row=1, column=0)

button2 = Button(root, padx=16, bd=8, fg='black', font=('arial',20, 'bold'), text='2', bg='grey',
command=lambda: button_clicked(2)).grid(row=1, column=0)

button3 = Button(root, padx=16, bd=8, fg='black', font=('arial',20, 'bold'), text='3', bg='grey',
command=lambda: button_clicked(3)).grid(row=1, column=0)

button_times = Button(root, padx=16, bd=8, fg='black', font=('arial',20, 'bold'), text='*', bg='grey',
command=lambda: button_clicked('*')).grid(row=1, column=0)



button_clear = Button(root, padx=16, bd=8, fg='black', font=('arial',20, 'bold'), text='c', bg='grey',
command=button_clear).grid(row=4, column=1)

button_equal = Button(root, padx=16, bd=8, fg='black', font=('arial',20, 'bold'), text='=', bg='grey',
command=button_equal).grid(row=4, column=2)

button_devide= Button(root, padx=16, bd=8, fg='black', font=('arial',20, 'bold'), text='/', bg='grey',
command=lambda: button_clicked('/')).grid(row=4, column=3)

root.mainloop()
from tkinter import *

def button_press(num):
    global equation_text
    equation_text = equation_text + str(num)
    equation_label.set(equation_text)

def equal():
    global equation_text
    try:
        total = str(eval(equation_text))
        equation_label.set(total)
        equation_text = total
    except ZeroDivisionError:
        equation_label.set("Error: Division by 0")
        equation_text = ""
    except SyntaxError:
        equation_label.set("Error: Invalid Input")
        equation_text = ""
    except Exception as e:
        equation_label.set(f"Error: {str(e)}")
        equation_text = ""

def clear():
    global equation_text
    equation_label.set("")
    equation_text= ""


window=Tk()
window.title("Calculator")
window.geometry("400x600")
window.configure(bg='#f0f8ff')
equation_text =""

equation_label = StringVar()

label = Label(
    window,
    textvariable=equation_label,
    font=('consolas', 20, 'bold'),
    bg='#ffffff',
    fg='#000000',
    width=24,
    height=2,
    relief='groove',
    bd=4
)
label.pack(pady=20)


frame=Frame(window)
frame.pack(pady=10)

button_style = {
    'height': 2,
    'width': 5,
    'font': ('Arial', 18, 'bold'),
    'relief': 'ridge',
    'bd': 3
}

button1=Button(frame, text=1,command=lambda: button_press(1),bg='#e6f7ff', fg='#003366',**button_style)
button1.grid(row=2, column=0, padx=5, pady=5)

button2=Button(frame, text=2, command=lambda: button_press(2),bg='#e6f7ff', fg='#003366',**button_style)
button2.grid(row=2, column=1, padx=5, pady=5)

button3=Button(frame, text=3,  command=lambda: button_press(3),bg='#e6f7ff', fg='#003366',**button_style)
button3.grid(row=2, column=2, padx=5, pady=5)

button4=Button(frame, text=4, command=lambda: button_press(4),bg='#e6f7ff', fg='#003366',**button_style)
button4.grid(row=1, column=0, padx=5, pady=5)

button5=Button(frame, text=5, command=lambda: button_press(5),bg='#e6f7ff', fg='#003366',**button_style)
button5.grid(row=1, column=1, padx=5, pady=5)

button6=Button(frame, text=6,  command=lambda: button_press(6),bg='#e6f7ff', fg='#003366',**button_style)
button6.grid(row=1, column=2, padx=5, pady=5)

button7=Button(frame, text=7, command=lambda: button_press(7),bg='#e6f7ff', fg='#003366',**button_style)
button7.grid(row=0, column=0, padx=5, pady=5)

button8=Button(frame, text=8,  command=lambda: button_press(8),bg='#e6f7ff', fg='#003366',**button_style)
button8.grid(row=0, column=1, padx=5, pady=5)

button9=Button(frame, text=9,  command=lambda: button_press(9),bg='#e6f7ff', fg='#003366',**button_style)
button9.grid(row=0, column=2, padx=5, pady=5)

button0=Button(frame, text=0,  command=lambda: button_press(0),bg='#e6f7ff', fg='#003366',**button_style)
button0.grid(row=3, column=1, padx=5, pady=5)

plus=Button(frame, text='+', command=lambda: button_press('+'),bg='#e6f7ff', fg='#003366',**button_style)
plus.grid(row=3, column=3, padx=5, pady=5)

minus=Button(frame, text='-', command=lambda: button_press('-'),bg='#e6f7ff', fg='#003366',**button_style)
minus.grid(row=2, column=3, padx=5, pady=5)

multiply=Button(frame, text='*', command=lambda: button_press('*'),bg='#e6f7ff', fg='#003366',**button_style)
multiply.grid(row=1, column=3, padx=5, pady=5)

divide=Button(frame, text='/', command=lambda: button_press('/'),bg='#e6f7ff', fg='#003366',**button_style)
divide.grid(row=0, column=3, padx=5, pady=5)

decimal=Button(frame, text='.', command=lambda: button_press('.'),bg='#e6f7ff', fg='#003366',**button_style)
decimal.grid(row=3, column=0, padx=5, pady=5)

clear = Button(window, text='CLEAR', bg='#ffcccc', fg='#800000', font=('Arial', 18, 'bold'), command=clear)
clear.pack(pady=10)

equal = Button(frame, text='=', bg='#cceeff', fg='#004d80', command=equal, **button_style)
equal.grid(row=3, column=2, padx=5, pady=5)

window.mainloop()

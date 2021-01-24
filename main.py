from tkinter import *
from decimal import *

x=input("")
if x=="дробь":

    def solver(a, b, c):
        """ Solves quadratic equation and returns the result in formatted string """
        D = b * b - 4 * a * c
        if D >= 0:
            x1 = (-b + sqrt(D)) / (2 * a)
            x2 = (-b - sqrt(D)) / (2 * a)
            text = "The discriminant is: %s 783107\n X1 is: %s \n X2 is: %s \n" % (D, x1, x2)
        else:
            text = "The discriminant is: %s \n This equation has no solutions" % D
        return text


    def inserter(value):
        """ Inserts specified value into text widget """
        output.delete("0.0", "end")
        output.insert("0.0", value)


    def clear(event):
        """ Clears entry form """
        caller = event.widget
        caller.delete("0", "end")


    def handler():
        """ Get the content of entries and passes result to the text """
        try:
            # make sure that we entered correct values
            a_val = float(a.get())
            b_val = float(b.get())
            c_val = float(c.get())
            inserter(solver(a_val, b_val, c_val))
        except ValueError:
            inserter("Make sure you entered 3 numbers")


    root = Tk()
    root.title("Quadratic calculator")
    root.minsize(325, 230)
    root.resizable(width=False, height=False)

    frame = Frame(root)
    frame.grid()

    a = Entry(frame, width=3)
    a.grid(row=1, column=1, padx=(10, 0))
    a.bind("<FocusIn>", clear)
    a_lab = Label(frame, text="x**2+").grid(row=1, column=2)

    b = Entry(frame, width=3)
    b.bind("<FocusIn>", clear)
    b.grid(row=1, column=3)
    b_lab = Label(frame, text="x+").grid(row=1, column=4)

    c = Entry(frame, width=3)
    c.bind("<FocusIn>", clear)
    c.grid(row=1, column=5)
    c_lab = Label(frame, text="= 0").grid(row=1, column=6)

    but = Button(frame, text="Solve", command=handler).grid(row=1, column=7, padx=(10, 0))

    output = Text(frame, bg="lightblue", font="Arial 12", width=35, height=10)
    output.grid(row=2, columnspan=8)

    root.mainloop()


if x=="калькулятор":
    root = Tk()
    root.title('Calculator')

    buttons = (('7', '8', '9', '/', '4'),
               ('4', '5', '6', '*', '4'),
               ('1', '2', '3', '-', '4'),
               ('0', '.', '=', '+', '4')
               )

    activeStr = ''
    stack = []


    def calculate():
        global stack
        global label
        result = 0
        operand2 = Decimal(stack.pop())
        operation = stack.pop()
        operand1 = Decimal(stack.pop())

        if operation == '+':
            result = operand1 + operand2
        if operation == '-':
            result = operand1 - operand2
        if operation == '/':
            result = operand1 / operand2
        if operation == '*':
            result = operand1 * operand2
        label.configure(text=str(result))


    def click(text):
        global activeStr
        global stack
        if text == 'CE':
            stack.clear()
            activeStr = ''
            label.configure(text='0')
        elif '0' <= text <= '9':
            activeStr += text
            label.configure(text=activeStr)
        elif text == '.':
            if activeStr.find('.') == -1:
                activeStr += text
                label.configure(text=activeStr)
        else:
            if len(stack) >= 2:
                stack.append(label['text'])
                calculate()
                stack.clear()
                stack.append(label['text'])
                activeStr = ''
                if text != '=':
                    stack.append(text)
            else:
                if text != '=':
                    stack.append(label['text'])
                    stack.append(text)
                    activeStr = ''
                    label.configure(text='0')


    label = Label(root, text='0', width=35)
    label.grid(row=0, column=0, columnspan=4, sticky="nsew")

    button = Button(root, text='CE', command=lambda text='CE': click(text))
    button.grid(row=1, column=3, sticky="nsew")
    for row in range(4):
        for col in range(4):
            button = Button(root, text=buttons[row][col],
                            command=lambda row=row, col=col: click(buttons[row][col]))
            button.grid(row=row + 2, column=col, sticky="nsew")

    root.grid_rowconfigure(6, weight=1)
    root.grid_columnconfigure(4, weight=1)

    root.mainloop()


from tkinter import Tk, Button, Entry, END
import math

class Calc:
    def getandreplace(self):  # replace x, + and % to symbols that can be used in calculations
        # we wont re write this to the text box until we are done with calculations

        self.txt = self.e.get() # Get value from text box and assign it to the global txt var
        self.txt = self.txt.replace('÷', '/')
        self.txt = self.txt.replace('x', '*')
        self.txt = self.txt.replace('%', '/100')

    def evaluation(self, specfunc):  # Evaluate the items in the text box for calculation specfunc = eq, sqroot or power
        self.getandreplace()
        try:
            self.txt = eval(str(self.txt))  # evaluate the expression using the eval function
        except SyntaxError:
            self.displayinvalid()
        else:
            if any([specfunc == 'sqroot', specfunc == 'power',specfunc=='facto',specfunc=='log',specfunc=='sin',specfunc=='cos',specfunc=='tan',specfunc=='ln',specfunc=='rad',specfunc=='mod',specfunc=='recip',specfunc=='pi']):  # Square Root and Power are special
                self.txt = self.evalspecialfunctions(specfunc)

            self.refreshtext()

    def displayinvalid(self):
        self.e.delete(0, END)
        self.e.insert(0, 'Invalid Input!')

    def refreshtext(self):  # Delete current contents of textbox and replace with our completed evaluatioin
        self.e.delete(0, END)
        self.e.insert(0, self.txt)

    def evalspecialfunctions(self, specfunc):  # Calculate square root and power if specfunc is sqroot or power
        if specfunc == 'sqroot':
            return math.sqrt(float(self.txt))
        elif specfunc == 'power':
            return math.pow(float(self.txt), 2)
        elif specfunc == 'facto':
            return (math.factorial(float(self.txt)))
        elif specfunc =='log':
            return(math.log10(float(self.txt)))
        elif specfunc=='sin':
            k=math.radians(float(self.txt))
            return(math.sin(k))
        elif specfunc=='cos':
            k = math.radians(float(self.txt))
            return (math.cos(k))
        elif specfunc == 'cos':
            k = math.radians(float(self.txt))
            return (math.cos(k))
        elif specfunc == 'cos':
            k = math.radians(float(self.txt))
            return (math.tan(k))
        elif specfunc == 'mod':
            return (abs(float(self.txt)))
        elif specfunc == 'ln':
            return (math.log(float(self.txt),2.71828))
        elif specfunc == 'rad':
            return (math.radians(float(self.txt)))
        elif specfunc=='recip':
            return(1/(float(self.txt)))
        elif specfunc == 'pi':
            return (math.pi)

    def clearall(self): # AC button pressed on form or 'esc" pressed on keyboard
        self.e.delete(0, END)
        self.e.insert(0, '0')

    def clear1(self, event=None):
        # C button press on form or backspace press on keyboard event defined on keyboard press

        if event is None:
            self.txt = self.e.get()[:-1]  # Form backspace done by hand
        else:
            self.txt = self.getvalue()  # No need to manually delete when done from keyboard

            self.refreshtext()

    def action(self, argi: object):  # Number or operator button pressed on form and passed in as argi
        self.txt = self.getvalue()

        self.stripfirstchar()

        self.e.insert(END, argi)

    def keyaction(self, event=None):  # Key pressed on keyboard which defines event
        self.txt = self.getvalue()

        if event.char.isdigit():
            self.stripfirstchar()
        elif event.char in '/*-+%().':
            self.stripfirstchar()
        elif event.char == '\x08':
            self.clear1(event)
        elif event.char == '\x1b':
            self.clearall()
        elif event.char == '\r':
            self.evaluation('eq')
        else:
            self.displayinvalid()
            return 'break'

    def stripfirstchar(self):  # Strips leading 0 from text box with first key or button is pressed
        if self.txt[0] == '0':
            self.e.delete(0, 1)

    def getvalue(self):  # Returns value of the text box
        return self.e.get()

    def __init__(self, master):  # Constructor method
        self.txt = 'o'  # Global var to work with text box contents
        master.title('Calulator')
        master.geometry()
        self.e = Entry(master)
        self.e.grid(row=0, column=0, columnspan=6, pady=3)
        self.e.insert(0, '0')
        self.e.focus_set()  # Sets focus on the text box text area

        # Generating Buttons
        Button(master, text="=", width=3, command=lambda: self.evaluation('eq')).grid(row=4, column=7,columnspan=3)
        Button(master, text="π ", width=3, command=lambda: self.evaluation('pi')).grid(row=4, column=6)

        Button(master, text='AC', width=3, command=lambda: self.clearall()).grid(row=1, column=4)
        Button(master, text="sinx", width=3, command=lambda: self.evaluation('sin')).grid(row=1, column=6)
        Button(master, text="cosx", width=3, command=lambda: self.evaluation('cos')).grid(row=2, column=6)
        Button(master, text="tanx", width=3, command=lambda: self.evaluation('tan')).grid(row=3, column=6)
        Button(master, text="1/x", width=3, command=lambda: self.evaluation('recip')).grid(row=1, column=5)
        Button(master,text="x!",width=3,command=lambda:self.evaluation('facto')).grid(row=4,column=4)
        Button(master, text="log", width=3, command=lambda: self.evaluation('log')).grid(row=4, column=5)
        Button(master, text="rad", width=3, command=lambda: self.evaluation('rad')).grid(row=1, column=7)
        Button(master, text="ln", width=3, command=lambda: self.evaluation('ln')).grid(row=2, column=7)
        Button(master, text="|x|", width=3, command=lambda: self.evaluation('mod')).grid(row=3, column=7)
        Button(master, text="+", width=3, command=lambda: self.action('+')).grid(row=4, column=3)
        Button(master, text="x", width=3, command=lambda: self.action('x')).grid(row=2, column=3)
        Button(master, text="-", width=3, command=lambda: self.action('-')).grid(row=3, column=3)
        Button(master, text="÷", width=3, command=lambda: self.action('÷')).grid(row=1, column=3)
        Button(master, text="%", width=3, command=lambda: self.action('%')).grid(row=4, column=2)
        Button(master, text="7", width=3, command=lambda: self.action('7')).grid(row=1, column=0)
        Button(master, text="8", width=3, command=lambda: self.action('8')).grid(row=1, column=1)
        Button(master, text="9", width=3, command=lambda: self.action('9')).grid(row=1, column=2)
        Button(master, text="4", width=3, command=lambda: self.action('4')).grid(row=2, column=0)
        Button(master, text="5", width=3, command=lambda: self.action('5')).grid(row=2, column=1)
        Button(master, text="6", width=3, command=lambda: self.action('6')).grid(row=2, column=2)
        Button(master, text="1", width=3, command=lambda: self.action('1')).grid(row=3, column=0)
        Button(master, text="2", width=3, command=lambda: self.action('2')).grid(row=3, column=1)
        Button(master, text="3", width=3, command=lambda: self.action('3')).grid(row=3, column=2)
        Button(master, text="0", width=3, command=lambda: self.action('0')).grid(row=4, column=0)
        Button(master, text=".", width=3, command=lambda: self.action('.')).grid(row=4, column=1)
        Button(master, text="(", width=3, command=lambda: self.action('(')).grid(row=2, column=4)
        Button(master, text=")", width=3, command=lambda: self.action(')')).grid(row=2, column=5)
        Button(master, text="√", width=3, command=lambda: self.evaluation('sqroot')).grid(row=3, column=4)
        Button(master, text="x²", width=3, command=lambda: self.evaluation('power')).grid(row=3, column=5)

        # bind key strokes
        self.e.bind('<Key>', lambda evt: self.keyaction(evt))


# Main
root = Tk()
obj = Calc(root)  # object instantiated
root.mainloop()
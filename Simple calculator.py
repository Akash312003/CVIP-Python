import tkinter  
from tkinter import *  
from tkinter import messagebox  
var = ""  
A = 0  
operator = ""  
  

def button1():  
    global var  
    var = var + "1"  
    the_data.set(var)  
  
def button2():  
    global var  
    var = var + "2"  
    the_data.set(var)  
  
def button3():  
    global var  
    var = var + "3"  
    the_data.set(var)  
  
def button4():  
    global var  
    var = var + "4"  
    the_data.set(var)  
  
def button5():  
    global var  
    var = var + "5"  
    the_data.set(var)  
  
def button6():  
    global var  
    var = var + "6"  
    the_data.set(var)  
  
def button7():  
    global var  
    var = var + "7"  
    the_data.set(var)  
  
def button8():  
    global var  
    var = var + "8"  
    the_data.set(var)  
  
def button9():  
    global var  
    var = var + "9"  
    the_data.set(var)  
  
def button0():  
    global var  
    var = var + "0"  
    the_data.set(var)  
  
def buttonAdd():  
    global A  
    global var  
    global operator  
    A = float(var)  
    operator = "+"  
    var = var + "+"  
    the_data.set(var)  
  
def buttonSub():  
    global A  
    global var  
    global operator  
    A = float(var)  
    operator = "-"  
    var = var + "-"  
    the_data.set(var)  
  
def buttonMul():  
    global A  
    global var  
    global operator  
    A = float(var)  
    operator = "*"  
    var = var + "*"  
    the_data.set(var)  
def buttonDiv():  
    global A  
    global var  
    global operator  
    A = float(var)  
    operator = "/"  
    var = var + "/"  
    the_data.set(var)   
def buttonEqual():  
    global A  
    global var  
    global operator  
    A = float(var)  
    operator = "="  
    var = var + "="  
    the_data.set(var)  
def buttonC():  
    global A  
    global var  
    global operator  
    var = ""  
    A = 0  
    operator = ""  
    the_data.set(var)  
def res():  
    global A  
    global operator  
    global var  
    var2 = var  
    if operator == "+":  
        a = float((var2.split("+")[1]))  
        x = A + a  
        the_data.set(x)  
        var = str(x)  
    elif operator == "-":  
        a = float((var2.split("-")[1]))  
        x = A - a  
        the_data.set(x)  
        var = str(x)  
    elif operator == "*":  
        a = float((var2.split("*")[1]))  
        x = A * a  
        the_data.set(x)  
        var = str(x)  
    elif operator == "/":  
        a = float((var2.split("/")[1]))  
        if a == 0:  
            messagebox.showerror("Division by 0 Not Allowed.")  
            A == ""  
            var = ""  
            the_data.set(var)  
        else:  
            x = float(A/a)  
            the_data.set(x)  
            var = str(x)  
  

guiWindow = tkinter.Tk()  

guiWindow.geometry("320x500+400+400")  

guiWindow.resizable(0, 0)  

guiWindow.title("Simple Calculator Using Gui")  
the_data = StringVar()  
guiLabel = Label(  
    guiWindow,  
    text = "Label",  
    anchor = SE,  
    font = (" Lexend", 22),  
    textvariable = the_data,  
    background = "#ffffff",  
    fg = "#000000"  
)  
guiLabel.pack(expand = True, fill = "both")  
 
frameOne = Frame(guiWindow, bg = "#000000")  
frameOne.pack(expand = True, fill = "both") 
frameTwo = Frame(guiWindow, bg = "#000000")  
frameTwo.pack(expand = True, fill = "both")  
frameThree = Frame(guiWindow, bg = "#000000")  
frameThree.pack(expand = True, fill = "both")  

frameFour = Frame(guiWindow, bg = "#000000")  
frameFour.pack(expand = True, fill = "both")  
buttonONE = Button(  
    frameOne,  
    text = "1",  
    font = (" Lexend", 24),  
    relief = GROOVE,  
    border = 0,  
    command = button1
)   
buttonONE.pack(side = LEFT, expand = True, fill = "both")  
buttonTWO = Button(  
    frameOne,  
    text = "2",  
    font = (" Lexend", 24),  
    relief = GROOVE,  
    border = 0,  
    command = button2 
)  
buttonTWO.pack(side = LEFT, expand = True, fill = "both")    
buttonTHREE = Button(  
    frameOne,  
    text = "3",  
    font = (" Lexend", 24),   
    relief = GROOVE,  
    border = 0,  
    command = button3 
)   
buttonTHREE.pack(side = LEFT, expand = True, fill = "both")   
buttonC = Button(  
    frameOne,  
    text = "C",  
    font = (" Lexend", 24),    
    relief = GROOVE,  
    border = 0,  
    command = buttonC
)   
buttonC.pack(side = LEFT, expand = True, fill = "both")  
buttonFOUR = Button(  
    frameTwo,  
    text = "4",  
font = (" Lexend", 24),    
    relief = GROOVE,  
    border = 0,  
    command = button4
)  
buttonFOUR.pack(side = LEFT, expand = True, fill = "both")  
buttonFIVE = Button(  
    frameTwo,  
    text = "5",  
    font = (" Lexend", 24),    
    relief = GROOVE,  
    border = 0,  
    command = button5
)  
buttonFIVE.pack(side = LEFT, expand = True, fill = "both")  
buttonSIX = Button(  
    frameTwo,  
    text = "6",  
    font = ("Lexend", 24),  
    relief = GROOVE,  
    border = 0,  
    command = button6 
)
buttonSIX.pack(side = LEFT, expand = True, fill = "both")  
buttonADD = Button(  
    frameTwo,  
    text = "+",  
    font = ("Lexend", 24),  
    relief = GROOVE,  
    border = 0,  
    command = buttonAdd 
)  
buttonADD.pack(side = LEFT, expand = True, fill = "both")  
buttonSEVEN = Button(  
    frameThree,  
    text = "7",  
    font = ("Lexend", 24),  
    relief = GROOVE,  
    border = 0,  
    command = button7 
)  
buttonSEVEN.pack(side = LEFT, expand = True, fill = "both")   
buttonEIGHT = Button(  
    frameThree,  
    text = "8",  
    font = ("Lexend", 24),  
    relief = GROOVE,  
    border = 0,  
    command = button8 
)  
buttonEIGHT.pack(side = LEFT, expand = True, fill = "both")  
buttonNINE = Button(  
    frameThree,  
    text = "9",  
    font = ("Lexend", 24),  
    relief = GROOVE,  
    border = 0,  
    command = button9
)   
buttonNINE.pack(side = LEFT, expand = True, fill = "both")  
   
buttonSUB = Button(  
    frameThree,  
    text = "-",  
    font = ("Lexend", 24),  
    relief = GROOVE,  
    border = 0,  
    command = buttonSub  
)  
buttonSUB.pack(side = LEFT, expand = True, fill = "both")  

buttonZERO = Button(  
    frameFour,  
    text = "0",  
    font = ("Lexend", 24),  
    relief = GROOVE,  
    border = 0,  
    command = button0
)  
buttonZERO.pack(side = LEFT, expand = True, fill = "both")  
buttonMUL = Button(  
    frameFour,  
    text = "*",  
    font = ("Lexend", 24),  
    relief = GROOVE,  
    border = 0,  
    command = buttonMul 
)  
buttonMUL.pack(side = LEFT, expand = True, fill = "both")  
  
buttonDIV = Button(  
    frameFour,  
    text = "/",  
    font = ("Lexend", 24),  
    relief = GROOVE,  
    border = 0,  
    command = buttonDiv 
)  
buttonDIV.pack(side = LEFT, expand = True, fill = "both")  
  
buttonEQUAL = Button(  
    frameFour,  
    text = "=",  
    font = ("Lexend", 24),  
    relief = GROOVE,  
    border = 0,  
    command = res  
)  
buttonEQUAL.pack(side = LEFT, expand = True, fill = "both")  
guiWindow.mainloop()  

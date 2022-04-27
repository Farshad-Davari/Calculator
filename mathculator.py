from distutils.command.clean import clean
from tkinter import *

from help import clear, equalpress, press

class Mathculator():

  def window(self):
    self.gui = Tk()
    self.gui.configure(bg="black")
    self.gui.title("Mathculator")
    self.gui.geometry("600x250")
    self.gui.resizable(0, 0) #disable resize ability


  def greeting(self):
    # the event function of btn
    def hide():
      text.place_forget() #hide the text
      btn.place_forget() #hide the button 
      self.calculator()

    text = Label(self.gui, 
    text="Welcome to Mathculator", 
    bg="black", 
    fg="#FF6F61")

    btn = Button(self.gui, 
    text="Let's start the app!", 
    bg="black", 
    fg="#FF6F61", 
    pady=8, 
    borderwidth="4",
    command=hide)

    text.configure(font=("TerminalVector", 14))
    text.place(x=150, y=100)
    
    btn.configure(font=("TerminalVector", 13))
    btn.place(x=170, y=150)
   
  def calculator(self):
    # create an instance to work with entry
    equation = StringVar()
    # the entry
    input = Entry(self.gui, 
    textvariable=equation, 
    bg="white", 
    fg="black",
    justify="center")

    # customize the entry
    input.configure(font=("TerminalVector", 14))
    input.place(x=170, y=30)

    # buttons of calculator
    # button number 1
    btn_one = Button(self.gui,
    text="1",
    bg="white",
    fg="#FF6F61",
    pady=3,
    borderwidth=2,
    command=lambda: press(1))
    btn_one.configure(font=("TerminalVector", 14))
    btn_one.place(x=180, y=90)

    # button number 2
    btn_two = Button(self.gui,
    text="2",
    bg="white",
    fg="#FF6F61",
    pady=3,
    borderwidth=2,
    command=lambda: press(2))
    btn_two.configure(font=("TerminalVector", 14))
    btn_two.place(x=250, y=90)

    # button number 3
    btn_three = Button(self.gui,
    text="3",
    bg="white",
    fg="#FF6F61",
    pady=3,
    borderwidth=2,
    command=lambda: press(3))
    btn_three.configure(font=("TerminalVector", 14))
    btn_three.place(x=320, y=90)

    # button plus
    btn_plus = Button(self.gui,
    text="+",
    bg="white",
    fg="#FF6F61",
    pady=3,
    borderwidth=2,
    command=lambda: press("+"))
    btn_plus.configure(font=("TerminalVector", 14))
    btn_plus.place(x=390, y=90)

    # button number 4
    btn_four = Button(self.gui,
    text="4",
    bg="white",
    fg="#FF6F61",
    pady=3,
    borderwidth=2,
    command=lambda: press(4))
    btn_four.configure(font=("TerminalVector", 14))
    btn_four.place(x=180, y=140)

    # button number 5
    btn_five = Button(self.gui,
    text="5",
    bg="white",
    fg="#FF6F61",
    pady=3,
    borderwidth=2,
    command=lambda: press(5))
    btn_five.configure(font=("TerminalVector", 14))
    btn_five.place(x=250, y=140)

    # button number 6
    btn_six = Button(self.gui,
    text="6",
    bg="white",
    fg="#FF6F61",
    pady=3,
    borderwidth=2,
    command=lambda: press(6))
    btn_six.configure(font=("TerminalVector", 14))
    btn_six.place(x=320, y=140)

    # button minus
    btn_minus = Button(self.gui,
    text="-",
    bg="white",
    fg="#FF6F61",
    pady=3,
    borderwidth=2,
    command=lambda: press("-"))
    btn_minus.configure(font=("TerminalVector", 14))
    btn_minus.place(x=390, y=140)

    # button number 7
    btn_seven = Button(self.gui,
    text="7",
    bg="white",
    fg="#FF6F61",
    pady=3,
    borderwidth=2,
    command=lambda: press(7))
    btn_seven.configure(font=("TerminalVector", 14))
    btn_seven.place(x=180, y=190)

    # button number 8
    btn_eight = Button(self.gui,
    text="8",
    bg="white",
    fg="#FF6F61",
    pady=3,
    borderwidth=2,
    command=lambda: press(8))
    btn_eight.configure(font=("TerminalVector", 14))
    btn_eight.place(x=250, y=190)

    # button number 9
    btn_nine = Button(self.gui,
    text="9",
    bg="white",
    fg="#FF6F61",
    pady=3,
    borderwidth=2,
    command=lambda: press(9))
    btn_nine.configure(font=("TerminalVector", 14))
    btn_nine.place(x=320, y=190)

    # button multiply
    btn_multiply = Button(self.gui,
    text="*",
    bg="white",
    fg="#FF6F61",
    pady=3,
    borderwidth=2,
    command=lambda: press("*"))
    btn_multiply.configure(font=("TerminalVector", 14))
    btn_multiply.place(x=390, y=190)

    # button equal
    btn_equal = Button(self.gui,
    text="=",
    bg="white",
    fg="#FF6F61",
    pady=3,
    borderwidth=2,
    command=equalpress)
    btn_equal.configure(font=("TerminalVector", 14))
    btn_equal.place(x=90, y=120)

    # button clear
    btn_clear = Button(self.gui,
    text="Clear",
    bg="white",
    fg="#FF6F61",
    pady=3,
    borderwidth=2,
    command=clear)
    btn_clear.configure(font=("TerminalVector", 10))
    btn_clear.place(x=90, y=170)

    # button number 0
    btn_zero = Button(self.gui,
    text="0",
    bg="white",
    fg="#FF6F61",
    pady=3,
    borderwidth=2,
    command=lambda: press(0))
    btn_zero.configure(font=("TerminalVector", 14))
    btn_zero.place(x=470, y=120)

    # button division
    btn_division = Button(self.gui,
    text="/",
    bg="white",
    fg="#FF6F61",
    pady=3,
    borderwidth=2,
    command=lambda: press("/"))
    btn_division.configure(font=("TerminalVector", 14))
    btn_division.place(x=470, y=160)


  def run(self):
    self.greeting()
    # run the window
    self.gui.mainloop()
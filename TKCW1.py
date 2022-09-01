
from tkinter import *

#import calendar mmodule
import calendar

#function for showing the of the given year
def showCal():
    #creat a new gui window
    window = Tk()

    #set the background color for the winow
    window.config(background="white")

    #set the title of the window
    window.title("Calendar")

    #set the geometry of the window
    window.geometry("550x600")

    #get method returtns current text as a string
    fetch_year = int(year_field.get())

    #calendar method of calendar module returns the calendar of the given year
    cal_content = calendar.calendar(fetch_year)

    #Create a label for showing the conten of the calendar
    cal_year = Label(window, text= cal_content, font="Consolas 10 bold")

    #grid method is used for placing the widgets at certain postions 
    cal_year.grid(row=5, column=1, padx=20)

    #start the gui window
    window.mainloop()

#driver code 
if __name__ == "__main__":

    #creat the main gui window
    gui = Tk()

    #set the background color
    gui.config(background="white")

    #give the name
    gui.title("Calendar")

    #give the geomtery
    gui.geometry("250x140")

    #creat a calendar label with specified font and size
    cal = Label(gui,text="calendar",bg="dark grey", font=("times",28,"bold"))

    #create a entry year label 
    year = Label (gui,text="Enter year", bg="light green")

    #create an entry box to be able to enter some information
    year_field = Entry(gui)

    #create a show button
    Show = Button(gui,text="Show Calendar", fg="black", bg="red", command=showCal)

    Exit = Button(gui,text="Exit", fg="black",bg="red",command=exit)

    cal.grid(row=1 , column=1)
    year.grid(row=2, column=1)
    year_field.grid(row=3, column=1)
    Show.grid(row=4, column=1)
    Exit.grid(row=6,column=1)

    gui.mainloop()










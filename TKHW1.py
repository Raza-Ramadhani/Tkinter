from tkinter import *



def showname():
    print(namex)
    sc = Tk()

    sc.title("HI")

    sc.geometry("400x400")

    sc.config(background="white")


    Showx = Button(window,text="Next", fg="black", bg="red", command=shownametext)

    
    Showx.grid(row=4, column=4)



    sc.mainloop()    

    def shownametext():
        pname = namex.get()
        l = Label(sc, text=f'{pname}, Registered!', pady=20, bg='#ffbf00').pack()




#def showName():
window = Tk()

window.title("Welcome")

window.geometry("400x400")

window.config(background="white")



x = Label(window,text="Test",bg="grey",font="Consolas 20 bold" )

namex = Entry(window)
Exit = Button(window,text="Exit",bg="red",command=exit)
Show = Button(window,text="Next", fg="black", bg="red", command=showname)

namex.grid(row=3, column=3)
Show.grid(row=4, column=3)
x.grid(row=1, column=1)
Exit.grid(row=2,column=1)

window.mainloop()




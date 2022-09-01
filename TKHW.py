
from tkinter import*

def convert():

    sc = Tk()

    sc.title("HI")

    sc.geometry("400x400")

    sc.config(background="white")

    
    temp_celsius = i1.get()
    temp_farhenheit = (str(temp_celsius))
    output.config(text="HI" +(temp_farhenheit))

    output= Label(sc)
    output.grid(row=2, column=1)

    sc.mainloop()    


window = Tk()
window.title("Job")
window.geometry("500x500")

txt1 = Label(window, text="Hire a job")
txt1.grid(row=0,column=0)

i1 = Entry(window)
i1.grid(row=2,column=2)

b1 = Button(window, text="Next", command=convert)
b1.grid(row=3,column=2)

window.mainloop()

from tkinter import*
import tkinter.font as font

def convert():
    temp_celsius = celsius_value.get()
    if(temp_celsius.replace('.','',1).isdigit()):
        error_msg.grid_forget()
        temp_farhenheit = (float(temp_celsius)* 9/5 + 32)
        output_farhenheit.config(text="temprature in farhenheit "+str(temp_farhenheit))
    else:
        error_msg.grid(row=1, column=1)

window = Tk()
window.title("Celsius to Farhenheit")

description = Label(text="celsius --> Farhenheit", font=font.Font(size=20),fg='grey')
description.pack()

frame = Frame(window)
frame.pack(pady = 20)

message_one = Label(frame, text="Enter Tempratur in Celsius", font = font.Font(size= 10))
message_one.grid(row=0, column=0)

celsius_value = Entry(frame)
celsius_value.grid(row=0,column=1)

error_msg = Label(frame, text="Please enter valid input...", font=font.Font(size=8), fg='red')

output_farhenheit = Label(frame, font=font.Font(size=12))
output_farhenheit.grid(row=2, column=0, columnspan = 2, pady=10 )

submit_btn = Button(frame, text='convert',width=30,fg='black',bg='lightgreen',bd=0,padx=20,pady=10,command=convert)
submit_btn.grid(row=3,column=0,columnspan=2,pady=10)

window.geometry("500x250")
window.mainloop()
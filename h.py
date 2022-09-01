import tkinter as tk



def new_screen():
    print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))

    sc = tk.Tk()

    sc.geometry("250x75")

    tk.Label(sc, text="Welcome and HI").grid(row=1, column=0)
    tk.Label(sc, text="Your E-mail Adress is").grid(row=2, column=0)

    t1 = tk.Label(sc, text= str(e1.get()))
    t2 = tk.Label(sc, text= str(e2.get()))

    t1.grid(row=1, column=2)
    t2.grid(row=2, column=2)

    tk.Button(sc, text='Quit', command=master.quit).grid(row=3, column=0, sticky=tk.W, pady=4)

    tk.mainloop()


master = tk.Tk()
tk.Label(master, text="First Name").grid(row=0)
tk.Label(master, text="E-mail").grid(row=1)

e1 = tk.Entry(master)
e2 = tk.Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

tk.Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=tk.W, pady=4)
tk.Button(master, text='Show', command=new_screen).grid(row=3, column=1, sticky=tk.W, pady=4)

tk.mainloop()
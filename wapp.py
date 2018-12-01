import tkinter as tk
from tkinter import Menu
from tkinter import ttk



def quit():
    win.quit()
    win.destroy()
    exit()


win = tk.Tk()

win.title("Weather App")

#Creating a MENU BAR
menuBar = Menu()
win.config(menu=menuBar)



#Add a menu Item
fileMenu = Menu(menuBar, tearoff=0)
fileMenu.add_command(label="New")
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command = quit)
menuBar.add_cascade(label="File", menu = fileMenu)


#HelpMenu()
helpMenu = Menu(menuBar, tearoff=0)
helpMenu.add_command(label="About")
menuBar.add_cascade(label="Help", menu = helpMenu)


#Tab Control
tabControl = ttk.Notebook(win)

tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text = "Tab 1")

tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text ="Tab 2")

tabControl.pack(expand=1, fill="both")


#Container Frame to hold the other widgets
weather_conditions_frame = ttk.LabelFrame(tab1, text="Current Weather Conditions")
weather_conditions_frame.grid(column=0, row=0, padx=8, pady=4)

ttk.Label(weather_conditions_frame, text="Location").grid(column=0, row=0, sticky='w')


city = tk.StringVar()
citySelected = ttk.Combobox(weather_conditions_frame, width =12, textvariable = city)
citySelected['values'] = ('India', 'Brazil', 'China')
citySelected.grid(column=1,row=0)
citySelected.current(0)




























win.mainloop()

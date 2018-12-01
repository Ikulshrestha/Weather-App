import tkinter as tk
from tkinter import Menu
from tkinter import ttk

#QUiT function

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

#ttk.Label(weather_conditions_frame, text="Locationgh:").grid(column=0, row=0, sticky='W')

#combobox
"""city = tk.StringVar()
citySelected = ttk.Combobox(weather_conditions_frame, width =12, textvariable = city)
citySelected['values'] = ('Delhi,India', 'Rio,Brazil', 'Beijing,China')
citySelected.grid(column=1,row=0)


#increaing length of combobox
max_width = max([len(x) for x in citySelected['values']])
new_width = max_width
citySelected.config(width=new_width)


#Adding Label and Textbox widgets
#______________________________________

ENTRY_WIDTH = max_width + 3
"""
ttk.Label (weather_conditions_frame, text="Last Updated:").grid(column=0, row=1, sticky='E')
Updated = tk.StringVar()
updatedEntry = ttk.Entry(weather_conditions_frame, textvariable=Updated,state='readonly')
updatedEntry.grid(column=1, row=1, sticky='W')

#______________________________________

ttk.Label(weather_conditions_frame, text="Weather:").grid(column=0, row=2, sticky='E')
weather = tk.StringVar()
weathEntry = ttk.Entry(weather_conditions_frame, textvariable=weather,state='readonly')
weathEntry.grid(column=1, row=2, sticky='w')

#_______________________________________

ttk.Label(weather_conditions_frame, text="Temperature:").grid(column=0, row=3, sticky='E')
temp = tk.StringVar()
tempEntry = ttk.Entry(weather_conditions_frame, textvariable=temp,state='readonly')
tempEntry.grid(column=1, row=3, sticky='w')

#_______________________________________

ttk.Label(weather_conditions_frame, text="Realtive Humidity:").grid(column=0, row=4, sticky='E')
relhu = tk.StringVar()
relhuEntry = ttk.Entry(weather_conditions_frame, textvariable=relhu,state='readonly')
relhuEntry.grid(column=1, row=4, sticky='w')

#_______________________________________

ttk.Label(weather_conditions_frame, text="Wind:").grid(column=0, row=5, sticky='E')
wind = tk.StringVar()
windEntry = ttk.Entry(weather_conditions_frame, textvariable=wind,state='readonly')
windEntry.grid(column=1, row=5, sticky='w')

#_______________________________________

ttk.Label(weather_conditions_frame, text="Visibily:").grid(column=0, row=6, sticky='E')
visi = tk.StringVar()
visiEntry = ttk.Entry(weather_conditions_frame, textvariable=visi,state='readonly')
visiEntry.grid(column=1, row=6, sticky='w')

#_______________________________________

ttk.Label(weather_conditions_frame, text="Pressure:").grid(column=0, row=7, sticky='E')
msl = tk.StringVar()
mslEntry = ttk.Entry(weather_conditions_frame, textvariable=msl,state='readonly')
mslEntry.grid(column=1, row=7, sticky='w')

#_______________________________________

ttk.Label(weather_conditions_frame, text="Sunrise:").grid(column=0, row=8, sticky='E')
alt = tk.StringVar()
altEntry = ttk.Entry(weather_conditions_frame,  textvariable=alt,state='readonly')
altEntry.grid(column=1, row=8, sticky='w')

#_______________________________________

ttk.Label(weather_conditions_frame, text="Sunset:").grid(column=0, row=9, sticky='E')
sset= tk.StringVar()
ssetEntry = ttk.Entry(weather_conditions_frame, textvariable=sset,state='readonly')
ssetEntry.grid(column=1, row=9, sticky='w')

#_______________________________________

#padding of labels
for child in weather_conditions_frame.winfo_children():
    #child.grid_configure(padx=6, pady=3)
    child.grid_configure(padx=4, pady=2)


#Repositioning of weather_conditions_frame
weather_conditions_frame.grid_configure(column=0, row=1, padx=8, pady=4)

#Create a new label Frame
weather_cities_frame = ttk.LabelFrame(tab1, text="Latest Observation for ")
weather_cities_frame.grid(column=0, row=0, padx=8, pady=4)

#_____________________________________________
#label and combobox into new Frame
ttk.Label(weather_cities_frame, text="City:     ").grid(column=0, row=0)
get_weather_button = ttk.Button(weather_cities_frame, text="Get Weather", command="_get_station").grid(column=2, row=0)


#_____________________________________________

city = tk.StringVar()
#citySelected = ttk.Combobox(weather_conditions_frame, width=12, textvariable=city)
citySelected = ttk.Combobox(weather_cities_frame, width=24, textvariable=city)
citySelected['values'] = ('Uttar Pradesh','London','Rio de Janeiro','Brazil')
citySelected.grid(column=1, row=0)
citySelected.current(0)

#Callback function
def _get_station():
    station = station_id_combo.get()
    get_weather_data(station)
    populate_gui_from_dict()

#____________________
#open weather api
from apikey import OWM_API_KEY_
from urllib.request import urlopen
import json


def get_open_weather_data(city="London,uk"):
    city = city.replace(' ', '%20')
    url = "api.openweathermap.org/data/2.5/weather?q={}&APPID={}".format(city, QWM_API_KEY)
    response = urlopen(url)
    data = response.read().decode()
    json_data = json.loads(data)
    from pprint import pprint
    pprint(json_data)




























win.mainloop()

from tkinter import *
from tkinter import messagebox as tkMessageBox

import Nmea_To_Csv
import Nmea_To_kml
import sqllite

root = Tk()
root.title('GUI')




t = StringVar()


# QUERY FOR FILES

Dater = StringVar()
Timer = StringVar()
latitude=StringVar()
lat_direction=StringVar()
longtitude=StringVar()
lon_direction=StringVar()
Number_of_satellites_being_tracked=StringVar()
altitude = StringVar()
altitude_M=StringVar()
SPEED=StringVar()

Label(root, fg="red",width=30,text='Insert Your Source File Here:').pack(side=LEFT, padx=0)
Entry(root,width=85,textvariable=t, fg="brown", bg='white').pack(side=LEFT, padx=0)

t.set('')

Label(text="\n\n\n\n").pack(side=TOP,padx=0)
Label(text="Click On Button That You want TO active:",fg="teal").pack(side=TOP,padx=0)

Button(text="convert to csv",background="red",relief=SOLID,command = lambda:Nmea_To_Csv.creat_csv(t.get())).pack(side=TOP,padx=0)
Button(text="convert to kml",background="green",relief=SOLID,command = lambda:Nmea_To_kml.create_kml(t.get())).pack(side=TOP,padx=0)
Button(text="create a file to db",background="yellow",relief=SOLID,command = lambda:sqllite.create_table(t.get())).pack(side=TOP,padx=0)
Button(text="Exit",background="grey",relief=SOLID,command=sys.exit).pack(side=TOP,padx=0)

Label(text="\n\n___________________________________________________________________________________________________________________________\n\n").pack(side=TOP,padx=0)

Label(text="Insert Values To the Options That you want to Query to csv or kml:",fg="green").pack(side=TOP,padx=0)

Label(root, fg="teal",width=30,text='date:').pack(side=TOP, padx=0)
Entry(root,width=20,textvariable=Dater, fg="brown", bg='white').pack(side=TOP, padx=0)

Dater.set("YYYY-MM-DD")

Label(root, fg="red",width=30,text='time:').pack(side=TOP, padx=0)
Entry(root,width=20,textvariable=Timer, fg="green", bg='white').pack(side=TOP, padx=0)

Timer.set("HH:MM:SS")



mainloop()
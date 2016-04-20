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

OPTIONS1=StringVar()

frame = Frame(root, width=800, height=1000, bd=1)
frame.pack()
iframe2 = Frame(frame, bd=10, relief=RIDGE)
Label(iframe2, fg="red",width=25,text='Insert Your Source File Here:').pack(side=LEFT, padx=0)
Entry(iframe2,width=30,textvariable=t, fg="brown", bg='white').pack(side=LEFT, padx=0)
Label(iframe2,text="Click On Button That You want TO active:",fg="teal").pack(side=TOP,padx=0)
Button(iframe2,text="convert to csv",background="red",relief=SOLID,command = lambda:Nmea_To_Csv.creat_csv(t.get())).pack(side=LEFT,padx=0)
Button(iframe2,text="convert to kml",background="green",relief=SOLID,command = lambda:Nmea_To_kml.create_kml(t.get())).pack(side=LEFT,padx=0)
Button(iframe2,text="create a file to db",background="yellow",relief=SOLID,command = lambda:sqllite.create_table(t.get())).pack(side=LEFT,padx=0)
Button(iframe2,text="Exit",background="grey",relief=SOLID,command=sys.exit).pack(side=LEFT,padx=0)
t.set('')

iframe2.pack(expand=3, fill=X, pady=0, padx=0)


frame = Frame(root, width=500, height=400, bd=1)
frame.pack()
frame2 = Frame(frame, bd=10, relief=RIDGE)

Label(frame2,text="Insert Values To the Options That you want to Query to csv or kml:",fg="green").pack(side=TOP,padx=0)
Message(frame2,background='yellow',fg="red", text='In Every Option Choose the Sign that You Want To Query From Files:  > , < , <= ,>= , == , !=', width=600,relief=SUNKEN).pack()

Message(frame2,background='yellow',text='1) >= --> Bigger Or Equal To The Value', width=300,relief=SUNKEN).pack(side=LEFT)
Message(frame2,background='yellow', text='2) > --> Bigger Than Value', width=300,relief=SUNKEN).pack(side=LEFT)
Message(frame2,background='yellow', text='3) <= --> Less Or Equal To The Value', width=300,relief=SUNKEN).pack(side=LEFT)
Message(frame2,background='yellow', text='4) < --> Less Than Value', width=300,relief=SUNKEN).pack(side=LEFT)
Message(frame2,background='yellow', text='5) == --> Equal To The Value', width=300,relief=SUNKEN).pack(side=LEFT)
Message(frame2,background='yellow',text='6) != --> Not Eqaul To The Value', width=300,relief=SUNKEN).pack(side=LEFT)
frame2.pack(expand=1, fill=X, pady=0, padx=0)


frame = Frame(root, width=500, height=400, bd=1)
frame.pack()

iframe2 = Frame(frame, bd=2, relief=RIDGE)
Label(iframe2, text='Date:').pack(side=LEFT,padx=0)
Entry(iframe2, textvariable=Dater, bg='white',width=15).pack(side=LEFT,padx=0)
Dater.set('YYYY-MM-DD')

Label(iframe2, text='Option:').pack(side=LEFT,padx=0)
Entry(iframe2, textvariable=OPTIONS1, bg='white',width=2).pack(side=LEFT,padx=0)


Label(iframe2, text='  ').pack(side=LEFT,padx=0)

Label(iframe2, fg="red",text='time:').pack(side=LEFT,padx=0)
Entry(iframe2,textvariable=Timer, fg="green", bg='white').pack(side=LEFT,padx=0)

Timer.set("HH:MM:SS")

Label(iframe2, fg="teal",text='Option:').pack(side=LEFT,padx=0)
Entry(iframe2,width=3,textvariable=OPTIONS1, fg="brown", bg='white').pack(side=LEFT,padx=0)


iframe2.pack(expand=1, fill=X, pady=10, padx=5)





mainloop()
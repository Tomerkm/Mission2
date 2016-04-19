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

Label(root, fg="red",width=25,text='Insert Your Source File Here:').pack(side=LEFT, padx=0)
Entry(root,width=30,textvariable=t, fg="brown", bg='white').pack(side=LEFT, padx=0)

t.set('')


Label(text="Click On Button That You want TO active:",fg="teal").pack(side=TOP,padx=0)

Button(text="convert to csv",background="red",relief=SOLID,command = lambda:Nmea_To_Csv.creat_csv(t.get())).pack(side=TOP,padx=0)
Button(text="convert to kml",background="green",relief=SOLID,command = lambda:Nmea_To_kml.create_kml(t.get())).pack(side=TOP,padx=0)
Button(text="create a file to db",background="yellow",relief=SOLID,command = lambda:sqllite.create_table(t.get())).pack(side=TOP,padx=0)
Button(text="Exit",background="grey",relief=SOLID,command=sys.exit).pack(side=TOP,padx=0)

Label(text="\n\n___________________________________________________________________________________________________________________________\n\n").pack(side=TOP,padx=0)

Label(text="Insert Values To the Options That you want to Query to csv or kml:",fg="green").pack(side=TOP,padx=0)

frame = Frame(root, width=2, height=2, bd=1)
frame.pack()

iframen = Frame(frame, bd=2, relief=FLAT)
Message(iframen,background='yellow',fg="red", text='In Every Option Choose the Sign that You Want To Query From Files: > , < , <= ,>= , == , !=', width=600,relief=SUNKEN).pack()
iframen.pack(expand=1, fill=X, pady=10, padx=5)
Message(iframen,background='yellow',text='1) >= --> Bigger Or Equal To The Value', width=300,relief=SUNKEN).pack()
Message(iframen,background='yellow', text='2) > --> Bigger Than Value', width=300,relief=SUNKEN).pack()
Message(iframen,background='yellow', text='3) <= --> Less Or Equal To The Value', width=300,relief=SUNKEN).pack()
Message(iframen,background='yellow', text='4) < --> Less Than Value', width=300,relief=SUNKEN).pack()
Message(iframen,background='yellow', text='5) == --> Equal To The Value', width=300,relief=SUNKEN).pack()
Message(iframen,background='yellow',text='6) != --> Not Eqaul To The Value', width=300,relief=SUNKEN).pack()
iframen.pack(expand=1, fill=X, pady=10, padx=5)


frame = Frame(root, width=500, height=400, bd=1)
frame.pack()

iframe2 = Frame(frame, bd=2, relief=RIDGE)
Label(iframe2, text='Date:').pack(side=LEFT, padx=5)
Entry(iframe2, textvariable=Dater, bg='white').pack(side=LEFT, padx=5)
Dater.set('YYYY-MM-DD')

Label(iframe2, text='Option:').pack()
Entry(iframe2, textvariable=OPTIONS1, bg='white').pack(side=LEFT, padx=5)



iframe2.pack(expand=1, fill=X, pady=10, padx=5)

frame = Frame(root, width=500, height=400, bd=1)
frame.pack()

iframe2 = Frame(frame, bd=2, relief=RIDGE)
Label(iframe2, text='Date:').pack(side=LEFT, padx=5)
Entry(iframe2, textvariable=Dater, bg='white').pack(side=LEFT, padx=5)
Dater.set('YYYY-MM-DD')

Label(iframe2, text='Option:').pack()
Entry(iframe2, textvariable=OPTIONS1, bg='white').pack(side=LEFT, padx=5)



iframe2.pack(expand=1, fill=X, pady=10, padx=5)


Label(root, fg="teal",width=30,text='Option to date:').pack(side=TOP, padx=0)
Entry(root,width=3,textvariable=OPTIONS1, fg="brown", bg='white').pack(side=TOP, padx=0)

Label(root, fg="red",width=30,text='time:').pack(side=TOP, padx=0)
Entry(root,width=10,textvariable=Timer, fg="green", bg='white').pack(side=TOP, padx=0)

Timer.set("HH:MM:SS")

Label(root, fg="teal",width=30,text='Option to timer:').pack(side=TOP, padx=0)
Entry(root,width=3,textvariable=OPTIONS1, fg="brown", bg='white').pack(side=TOP, padx=0)

Label(root, fg="orange",width=30,text='latitude:').pack(side=TOP, padx=0)
Entry(root,width=5,textvariable=latitude, fg="red", bg='white').pack(side=TOP, padx=0)

latitude.set('')

Label(root, fg="teal",width=30,text='Option to latitude:').pack(side=TOP, padx=0)
Entry(root,width=3,textvariable=OPTIONS1, fg="brown", bg='white').pack(side=TOP, padx=0)

Label(root, fg="blue",width=30,text='lat_direction:').pack(side=TOP, padx=0)
Entry(root,width=2,textvariable=lat_direction, fg="green", bg='white').pack(side=TOP, padx=0)

lat_direction.set('')

Label(root, fg="black",width=30,text='longtitude:').pack(side=TOP, padx=0)
Entry(root,width=5,textvariable=longtitude, fg="green", bg='white').pack(side=TOP, padx=0)

longtitude.set('')

Label(root, fg="teal",width=30,text='Option to longtitude:').pack(side=TOP, padx=0)
Entry(root,width=3,textvariable=OPTIONS1, fg="brown", bg='white').pack(side=TOP, padx=0)

Label(root, fg="brown",width=30,text='lon_direction:').pack(side=TOP, padx=0)
Entry(root,width=2,textvariable=lon_direction, fg="green", bg='white').pack(side=TOP, padx=0)

lon_direction.set('')


Label(root, fg="lightblue",width=30,text='Number_of_satellites_being_tracked:').pack(side=TOP, padx=0)
Entry(root,width=2,textvariable=Number_of_satellites_being_tracked, fg="green", bg='white').pack(side=TOP, padx=0)

Number_of_satellites_being_tracked.set('')

Label(root, fg="teal",width=40,text='Option to Number_of_satellites_being_tracked:').pack(side=TOP, padx=0)
Entry(root,width=3,textvariable=OPTIONS1, fg="brown", bg='white').pack(side=TOP, padx=0)

Label(root, fg="teal",width=30,text='altitude:').pack(side=TOP, padx=0)
Entry(root,width=5,textvariable=altitude, fg="green", bg='white').pack(side=TOP, padx=0)

altitude.set('')

Label(root, fg="grey",width=30,text='altitude_M:').pack(side=TOP, padx=0)
Entry(root,width=2,textvariable=altitude_M, fg="green", bg='white').pack(side=TOP, padx=0)

altitude_M.set('')


Label(root, fg="teal",width=30,text='SPEED:').pack(side=TOP, padx=0)
Entry(root,width=5,textvariable=SPEED, fg="green", bg='white').pack(side=TOP, padx=0)

SPEED.set('')


mainloop()
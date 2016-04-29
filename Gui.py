from tkinter import *
from tkinter import messagebox as tkMessageBox

import Nmea_To_Csv
import Nmea_To_kml
import Interface_Function
import sqllite

root = Tk()
root.title('GUI')




t = StringVar()


# QUERY FOR FILES

Dater = StringVar()
Timer = StringVar()
latitude=StringVar()
longtitude=StringVar()
Number_of_satellites_being_tracked=StringVar()
altitude = StringVar()
SPEED=StringVar()



frame = Frame(root, width=800, height=1000, bd=1)
frame.pack()
iframe2 = Frame(frame, bd=10, relief=RIDGE)
Label(iframe2, fg="red",width=25,text='Insert Your Source File Here:').pack(side=LEFT, padx=0)
Entry(iframe2,width=50,textvariable=t, fg="brown", bg='white').pack(side=LEFT, padx=0)
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

frame2.pack(expand=1, fill=X, pady=0, padx=0)


frame = Frame(root, width=500, height=400, bd=1)
frame.pack()

iframe2 = Frame(frame, bd=2, relief=RIDGE)
Label(iframe2, text='Date:').pack(side=LEFT,padx=0)
Entry(iframe2, textvariable=Dater, bg='white',width=15).pack(side=LEFT,padx=0)
Dater.set('YYYY-MM-DD')



Label(iframe2, text='  ').pack(side=LEFT,padx=0)

Label(iframe2, fg="red",text='time:').pack(side=LEFT,padx=0)
Entry(iframe2,textvariable=Timer, fg="green", bg='white').pack(side=LEFT,padx=0)

Timer.set("HH:MM:SS")


Label(iframe2, text='  ').pack(side=LEFT,padx=0)

Label(iframe2, fg="teal",text='latitude:').pack(side=LEFT,padx=0)
Entry(iframe2,textvariable=latitude, fg="blue", bg='white').pack(side=LEFT,padx=0)

latitude.set("")

Label(iframe2, text='  ').pack(side=LEFT,padx=0)

Label(iframe2, fg="green",text='longtitude:').pack(side=LEFT,padx=0)
Entry(iframe2,textvariable=longtitude, fg="orange", bg='white').pack(side=LEFT,padx=0)

longtitude.set("")


Label(iframe2, text='  ').pack(side=LEFT,padx=0)

Label(iframe2, fg="brown",text='Number_of_satellites_being_tracked:').pack(side=LEFT,padx=0)
Entry(iframe2,textvariable=Number_of_satellites_being_tracked, fg="red", bg='white').pack(side=LEFT,padx=0)

Number_of_satellites_being_tracked.set("")

Label(iframe2, text='  ').pack(side=LEFT,padx=0)

Label(iframe2, fg="brown",text='altitude:').pack(side=LEFT,padx=0)
Entry(iframe2,textvariable=altitude, fg="red", bg='white').pack(side=LEFT,padx=0)

altitude.set("")


iframe2.pack(expand=1, fill=X, pady=10, padx=5)

frame = Frame(root, width=500, height=400, bd=1)
frame.pack()


iframe2 = Frame(frame, bd=2, relief=RIDGE)

Label(iframe2, fg="brown",text='SPEED:').pack(side=LEFT,padx=0)
Entry(iframe2,textvariable=SPEED, fg="red", bg='white').pack(side=LEFT,padx=0)

SPEED.set("")


iframe2.pack(expand=1, fill=X, pady=10, padx=5)

iframe2 = Frame(frame, bd=2, relief=RIDGE)

Label(iframe2,text="Click On Button That You want TO Query from Your Db:",fg="teal").pack(side=TOP,padx=0)
Label(iframe2,text="** If All Buttons's Value Are Empty So it will Query all a Data to a file you will choose ** ",fg="black").pack(side=TOP,padx=0)
Button(iframe2,text="convert to csv",background="red",relief=SOLID,command = lambda:Nmea_To_Csv.create_Csv_Query(Dater.get(),Timer.get(),latitude.get(),longtitude.get(),Number_of_satellites_being_tracked.get(),altitude.get(),SPEED.get())).pack(side=TOP,padx=0)
Button(iframe2,text="convert to kml",background="green",relief=SOLID,command = lambda:Nmea_To_kml.create_KML_Query(Dater.get(),Timer.get(),latitude.get(),longtitude.get(),Number_of_satellites_being_tracked.get(),altitude.get(),SPEED.get())).pack(side=TOP,padx=0)


iframe2.pack(expand=1, fill=X, pady=10, padx=5)



mainloop()
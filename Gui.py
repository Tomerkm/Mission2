from tkinter import *
from tkinter import messagebox as tkMessageBox

import Nmea_To_Csv
import Nmea_To_kml
import sqllite

root = Tk()
root.title('GUI')
t = StringVar()
Label(root, fg="red",width=30,text='Insert Your Source File Here:').pack(side=LEFT, padx=0)
Entry(root,width=85,textvariable=t, fg="brown", bg='white').pack(side=LEFT, padx=50)
t.set('')


Label(text="\n\nClick On Button That You want TO active!\n\n", fg="teal").pack()

Button(text="convert to csv",background="red", command = lambda:Nmea_To_Csv.creat_csv(t.get())).pack()
Button(text="convert to kml",background="green",command = lambda:Nmea_To_kml.create_kml(t.get())).pack()
Button(text="create a file to db",background="yellow", command = lambda:sqllite.create_table(t.get())).pack()
Button(text="Exit",background="grey", command=sys.exit).pack()


Label(text="\n\nClick On Button That You want TO active!", fg="green").pack()

def quit(event):
    if tkMessageBox.askokcancel('Quit','Do you really want to quit?'):
        root.destroy()
root.bind('<q>', quit)

mainloop()
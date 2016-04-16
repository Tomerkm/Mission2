from tkinter import *
import Nmea_To_Csv
import Nmea_To_kml

root = Tk()
root.title('GUI')
t = StringVar()
Label(root,width=30,text='Insert Your Source File Here:').pack(side=LEFT, padx=0)
Entry(root,width=85,textvariable=t, bg='white').pack(side=LEFT, padx=50)
t.set('')
#print(t.get())

Label(text="Click On Button That You want TO active!").pack()

Button(text="convert to csv", command = lambda:Nmea_To_Csv.creat_csv(t.get())).pack()
Button(text="convert to kml",command = lambda:Nmea_To_kml.create_kml(t.get())).pack()
Button(text="create a file to db", command=sys.exit).pack()
Button(text="Exit", command=sys.exit).pack()
mainloop()
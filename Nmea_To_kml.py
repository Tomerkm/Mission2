import sys
import re
import math
from tkinter import messagebox
import os.path
import Interface_Function
import sqlite3

counter=0
counter_F=0


def create_kml(FILE_NAME):


    in_filename = FILE_NAME
    if FILE_NAME=='':
        return
    if not FILE_NAME.endswith(".nmea"):
        messagebox.showinfo("error", "The File Does not End with nmea")
        return
    if not os.path.isfile(FILE_NAME):
        messagebox.showinfo("error", "The Source File Does not exists")
        return

    global counter
    counter+=1


    out_filename = "Kml_Files/out_kml"+str(counter)+".kml"
    kml_file = open(out_filename,'w')

    kml_file.write('<?xml version="1.0"  encoding="UTF-8"?>\n')
    kml_file.write('<kml xmlns="http://www.opengis.net/kml/2.2">\n')
    kml_file.write('<Document>\n')
    kml_file.write('<Folder>\n')
    kml_file.write('<name>Point Features</name>\n')
    kml_file.write('<description>Point Features</description>\n')


    for line in open(in_filename,'r'):


        if not line:
            continue

        # Try to catch corrupt lines early
        if not line.startswith('$GP'):
            continue

        # Skip any sentence other than GPGGA
        if not line.startswith('$GPGGA'):
            continue

        list = line.split(',')

        if list[2][:2]=='':
            continue
        if list[2][2:]=='':
            continue
        if list[4][:3]=='':
            continue
        if list[4][3:]=='':
            continue
        if list[9]=='':
            continue
        if list[1]=='':
            continue


        kml_file.write('<Placemark>\n')
        hhmmss = list[1]
        time = hhmmss[0:2]+":"+ hhmmss[2:4]+":" +hhmmss[4:10]
        latitude = float(list[2][:2]) + (float(list[2][2:]) / 60)
        longtitude = float(list[4][:3]) + (float(list[4][3:]) / 60)
        altitude = list[9]

        kml_file.write('<Point>\n')

        kml_file.write('<coordinates> %s,%s,%s </coordinates>\n' % (longtitude,latitude,altitude))
        kml_file.write('</Point>\n')
        kml_file.write('</Placemark>\n')


    kml_file.write('</Folder>\n')
    kml_file.write('</Document>\n')
    kml_file.write('</kml>\n')
    kml_file.close()
    messagebox.showinfo("Succesfull", "The kml File Has been created in Kml_Files us: out_kml"+str(counter)+".kml")


def create_KML_Query(DATER,TIMER,latitude,longtitude,Number_of_satellites_being_tracked,altitude,SPEED):

    Interface_Function.Valid_Input(DATER,TIMER,latitude,longtitude,Number_of_satellites_being_tracked,altitude,SPEED)
    Query = Interface_Function.create_Query(DATER,TIMER,latitude,longtitude,Number_of_satellites_being_tracked,altitude,SPEED)
    size = Interface_Function.Count_Files_In_Db()
    conn = sqlite3.connect("tk.db")
    cursor = conn.cursor()
    count=1
    global counter_F
    counter_F = counter_F + 1

    out_filename = "Kml_Files/out_kml_Query"+str(counter_F)+".kml"
    kml_file = open(out_filename,'w')

    kml_file.write('<?xml version="1.0"  encoding="UTF-8"?>\n')
    kml_file.write('<kml xmlns="http://www.opengis.net/kml/2.2">\n')
    kml_file.write('<Document>\n')
    kml_file.write('<Folder>\n')
    kml_file.write('<name>Point Features</name>\n')
    kml_file.write('<description>Point Features</description>\n')

    while count<=size:
        for row in cursor.execute("SELECT * FROM FILE"+str(count)+" "+ Query ):

            kml_file.write('<Placemark>\n')


            latituder = round(math.floor(float(row[2]) / 100) + (float(row[2]) % 100) / 60, 6)
            longtituder = round(math.floor(float(row[4]) / 100) + (float(row[4]) % 100) / 60, 6)
            altituder = row[9]

            kml_file.write('<Point>\n')

            kml_file.write('<coordinates> %s,%s,%s </coordinates>\n' % (longtituder,latituder,altituder))
            kml_file.write('</Point>\n')
            kml_file.write('</Placemark>\n')



        count=count+1

    kml_file.write('</Folder>\n')
    kml_file.write('</Document>\n')
    kml_file.write('</kml>\n')
    kml_file.close()
    messagebox.showinfo("Succesfull", "The kml File Has been created in Kml_Files us: out_kml_Query"+str(counter_F)+".kml")

def main():
    print('main')

if __name__ == '__main__':
    main()


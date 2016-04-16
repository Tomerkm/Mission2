import sys
import re
import math
from tkinter import messagebox
import os.path

counter=0

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
    print(counter)

    out_filename = "C:/Users/user/Downloads/Desktop/out_kml"+str(counter)+".kml"
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
    messagebox.showinfo("Succesfull", "The kml File Has been created in your desktop: out_kml "+str(counter)+".csv")


def main():




    in_filename = "C:/Users/user/Downloads/Desktop/br.nmea"
    out_filename = "C:/Users/user/Downloads/Desktop/outer.kml"

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
    kml_file.close();



if __name__ == '__main__':
    main()


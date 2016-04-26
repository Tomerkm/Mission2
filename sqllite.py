import sqlite3
from datetime import datetime
import math
from tkinter import messagebox
import os.path



counter=0


def create_table(FILE_NAME):



    conn = sqlite3.connect("tk.db")
    global counter

    if counter==0:
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        for tbl in tables:
            cursor.execute('''DROP TABLE '''+tbl[0])
            print ("\n DELETED FILE : ########  "+tbl[0]+"  ########")


    if FILE_NAME=='':
        return
    if not FILE_NAME.endswith(".nmea"):
        messagebox.showinfo("error", "The File Does not End with nmea")
        return
    if not os.path.isfile(FILE_NAME):
        messagebox.showinfo("error", "The Source File Does not exists")
        return

    c = conn.cursor()
    counter+=1

    sql = """CREATE TABLE FILE"""+str(counter)+""" (
         dater text,
         timer text,
         latitude FLOAT,
         lat_direction TEXT,
         longtitude FLOAT,
         lon_direction TEXT,
         Number_of_satellites_being_tracked INT,
         Horizontal_dilution_of_position FLOAT,
         altitude FLOAT,
         altitude_M TEXT,
         SPEED INT
          )"""

    c.execute(sql)
    in_filename = FILE_NAME

    list_GPGGA=""
    list_GPRMC=""
    latitude=""
    longtitude=""
    altitude=""
    for line in open(in_filename,'r'):

        if not line:
            continue

        # Try to catch corrupt lines early
        if not line.startswith('$GP'):
            continue

        # Save Values for GPGGA
        if line.startswith('$GPGGA'):
            list_GPGGA = line.split(',')

            if list_GPGGA[2]=='':
                continue
            if list_GPGGA[4]=='':
                continue
            if list_GPGGA[9]=='':
                continue

            latitude = float(list_GPGGA[2])
            longtitude = float(list_GPGGA[4])
            altitude = list_GPGGA[9]
            continue

        if not line.startswith('$GPRMC'):
            continue


        list_GPRMC = line.split(',')
        if list_GPRMC[1]=='':
            continue
        if list_GPRMC[7]=='':
            continue
        if list_GPRMC[9]=='':
            continue
        time = list_GPRMC[1]
        speed = list_GPRMC[7]
        date =  list_GPRMC[9]

        dater=datetime.strptime(date, '%d%m%y')
        timer= datetime.strptime(date, '%H%M%S')

        # merge the time and date columns into one Python datetime object (usually more convenient than having both separately)
        date_and_time = datetime.strptime(date + ' ' + time, '%d%m%y %H%M%S.%f')

        # convert the Python datetime into your preferred string format, see http://www.tutorialspoint.com/python/time_strftime.htm for futher possibilities
        date_and_time = date_and_time.strftime('%y-%m-%d %H:%M:%S.%f')[:-3] # [:-3] cuts off the last three characters (trailing zeros from the fractional seconds)

        # speed is given in knots, you'll probably rather want it in km/h and rounded to full integer values.
        # speed has to be converted from string to float first in order to do calculations with it.
        # conversion to int is to get rid of the tailing ".0".
        speed = int(round(float(speed) * 1.852, 0))


        # Prepare SQL query to INSERT a record into the database.
        sql = "INSERT INTO FILE"+str(counter)+"(dater,timer, \
        latitude, lat_direction, longtitude,lon_direction,Number_of_satellites_being_tracked , Horizontal_dilution_of_position , altitude ,altitude_M,SPEED ) \
        VALUES ('%s','%s', '%f', '%s','%f', '%s', '%d','%f', '%f', '%s','%d' )" % \
        (str(dater.date()),str(timer.time()) , float(latitude) , list_GPGGA[3] , float(longtitude) , list_GPGGA[5], int(list_GPGGA[7]) , float(list_GPGGA[8]) , float(altitude) , list_GPGGA[10],speed)
        try:
            # Execute the SQL command
            c.execute(sql)
            # Commit your changes in the database
            conn.commit()
        except sqlite3.Error as er:
            print(er)
            # Rollback in case there is any error
            conn.rollback()

    messagebox.showinfo("Succesfull", "The File" +str(counter)+ " Has been created in your DB")

def main():
    print('main')





if __name__ == '__main__':
    main()

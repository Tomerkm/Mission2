import sqlite3
from datetime import datetime
import math

def main():

    conn = sqlite3.connect("tk.db")
    c = conn.cursor()

    sql = """CREATE TABLE FILE (
         Time_Clock TEXT,
         latitude FLOAT,
         N TEXT,
         longtitude FLOAT,
         W TEXT,
         Number_of_satellites_being_tracked INT,
         Horizontal_dilution_of_position FLOAT,
         altitude FLOAT,
         altitude_M TEXT,
         SPEED INT
          )"""

    c.execute(sql)


    in_filename = "C:/Users/user/Downloads/Desktop/br.nmea"

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
            latitude = float(list_GPGGA[2][:2]) + (float(list_GPGGA[2][2:]) / 60)
            longtitude = float(list_GPGGA[4][:3]) + (float(list_GPGGA[4][3:]) / 60)
            altitude = list_GPGGA[9]
            continue

        if not line.startswith('$GPRMC'):
            continue


        list_GPRMC = line.split(',')
        time = list_GPRMC[1]
        speed = list_GPRMC[7]
        date =  list_GPRMC[9]

        # merge the time and date columns into one Python datetime object (usually more convenient than having both separately)
        date_and_time = datetime.strptime(date + ' ' + time, '%d%m%y %H%M%S.%f')

        # convert the Python datetime into your preferred string format, see http://www.tutorialspoint.com/python/time_strftime.htm for futher possibilities
        date_and_time = date_and_time.strftime('%d/%m/%y %H:%M:%S.%f')[:-3] # [:-3] cuts off the last three characters (trailing zeros from the fractional seconds)

        # speed is given in knots, you'll probably rather want it in km/h and rounded to full integer values.
        # speed has to be converted from string to float first in order to do calculations with it.
        # conversion to int is to get rid of the tailing ".0".
        speed = int(round(float(speed) * 1.852, 0))


        # Prepare SQL query to INSERT a record into the database.
        sql = "INSERT INTO FILE(Time_Clock, \
        latitude, N, longtitude,W,Number_of_satellites_being_tracked , Horizontal_dilution_of_position , altitude ,altitude_M,SPEED ) \
        VALUES ('%s', '%f', '%s','%f', '%s', '%d','%f', '%f', '%s','%d' )" % \
        (date_and_time , float(latitude) , list_GPGGA[3] , float(longtitude) , list_GPGGA[5], int(list_GPGGA[7]) , float(list_GPGGA[8]) , float(altitude) , list_GPGGA[10],speed)
        try:
            # Execute the SQL command
            c.execute(sql)
            # Commit your changes in the database
            conn.commit()
        except sqlite3.Error as er:

            print(er)
            # Rollback in case there is any error
            conn.rollback()





if __name__ == '__main__':
    main()

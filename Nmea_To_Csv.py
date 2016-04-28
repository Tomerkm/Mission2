import sqlite3
import csv
import datetime
import time
import math
from tkinter import messagebox
import os.path
import Interface_Function

# adapt this to your file

INPUT_FILENAME = 'in.nmea'
OUTPUT_FILENAME = 'out.csv'

counter=0

def creat_csv(FILE_NAME):




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

# open the input file in read mode
    with open(FILE_NAME, 'r') as input_file:

        # open the output file in write mode
        with open("C:/Users/user/Downloads/Desktop/out_csv"+str(counter)+".csv", 'wt') as output_file:

            # create a csv reader object from the input file (nmea files are basically csv)
            reader = csv.reader(input_file)

            # create a csv writer object for the output file
            writer = csv.writer(output_file, delimiter=',', lineterminator='\n')

            # write the header line to the csv file
            writer.writerow(['date_and_time', 'lat', 'lon', 'speed'])

            # iterate over all the rows in the nmea file
            for row in reader:

                if not row:
                    continue

                # skip all lines that do not start with $GPRMC
                if not row[0].startswith('$GPRMC'):
                    continue

                else:

                    # for each row, fetch the values from the row's columns
                    # columns that are not used contain technical GPS stuff that you are probably not interested in
                    time = row[1]
                    warning = row[2]
                    lat = row[3]
                    lat_direction = row[4]
                    lon = row[5]
                    lon_direction = row[6]
                    speed = row[7]
                    date =  row[9]

                    if row[1]=='':
                        continue
                    if row[2]=='':
                        continue
                    if row[3]=='':
                        continue
                    if row[4]=='':
                        continue
                    if row[5]=='':
                        continue
                    if row[6]=='':
                        continue
                    if row[7]=='':
                        continue
                    if row[9]=='':
                        continue


                    # if the "warning" value is "V" (void), you may want to skip it since this is an indicator for an incomplete data row)
                    if warning == 'V':
                        continue

                    # merge the time and date columns into one Python datetime object (usually more convenient than having both separately)
                    date_and_time = datetime.datetime.strptime(date + ' ' + time, '%d%m%y %H%M%S.%f')

                    # convert the Python datetime into your preferred string format, see http://www.tutorialspoint.com/python/time_strftime.htm for futher possibilities
                    date_and_time = date_and_time.strftime('%y-%m-%d %H:%M:%S.%f')[:-3] # [:-3] cuts off the last three characters (trailing zeros from the fractional seconds)

                    # lat and lon values in the $GPRMC nmea sentences come in an rather uncommon format. for convenience, convert them into the commonly used decimal degree format which most applications can read.
                    # the "high level" formula for conversion is: DDMM.MMMMM => DD + (YY.ZZZZ / 60), multiplicated with (-1) if direction is either South or West
                    # the following reflects this formula in mathematical terms.
                    # lat and lon have to be converted from string to float in order to do calculations with them.
                    # you probably want the values rounded to 6 digits after the point for better readability.
                    lat = round(math.floor(float(lat) / 100) + (float(lat) % 100) / 60, 6)
                    if lat_direction == 'S':
                        lat = lat * -1

                    lon = round(math.floor(float(lon) / 100) + (float(lon) % 100) / 60, 6)
                    if lon_direction == 'W':
                        lon = lon * -1

                    # speed is given in knots, you'll probably rather want it in km/h and rounded to full integer values.
                    # speed has to be converted from string to float first in order to do calculations with it.
                    # conversion to int is to get rid of the tailing ".0".
                    speed = int(round(float(speed) * 1.852, 0))

                    # write the calculated/formatted values of the row that we just read into the csv file
                    writer.writerow([date_and_time, lat, lon, speed])

    messagebox.showinfo("Succesfull", "The Csv File Has been created in your desktop: out_csv "+str(counter)+".csv")



def create_Csv_Query(DATER,TIMER,latitude,longtitude,Number_of_satellites_being_tracked,altitude,SPEED):

    Interface_Function.Valid_Input(DATER,TIMER,latitude,longtitude,Number_of_satellites_being_tracked,altitude,SPEED)

    Query=""
    count = 0
    if DATER!="" and DATER!="YYYY-MM-DD":
        Query = "where dater="+"'"+DATER+"'"
        count=count+1

    if TIMER!="" and TIMER!="HH:MM:SS":

        if count==0:
            Query = "where timer="+"'"+TIMER+"'"
        else:
            Query= Query + " And timer="+"'"+TIMER+"'"
        count=count+1

    if latitude!="":
        latitude = int(latitude)
        if count==0:
            Query = "where CAST(latitude AS INT)="+""+str(latitude)+""
        else:
            Query= Query + " And CAST(latitude AS INT)="+""+str(latitude)+""
        count=count+1

    if longtitude!="":
        latitude = int(longtitude)
        if count==0:
            Query = "where CAST(longtitude AS INT)="+""+str(longtitude)+""
        else:
            Query= Query + " And CAST(longtitude AS INT)="+""+str(longtitude)+""
        count=count+1

    if Number_of_satellites_being_tracked!="":
        Number_of_satellites_being_tracked = int(Number_of_satellites_being_tracked)
        if count==0:
            Query = "where CAST(Number_of_satellites_being_tracked AS INT)="+""+str(Number_of_satellites_being_tracked)+""
        else:
            Query= Query + " And CAST(Number_of_satellites_being_tracked AS INT)="+""+str(Number_of_satellites_being_tracked)+""
        count=count+1

    if altitude!="":
        altitude = int(altitude)
        if count==0:
            Query = "where CAST(altitude AS INT)="+""+str(altitude)+""
        else:
            Query=Query + " And CAST(altitude AS INT)="+""+str(altitude)+""
        count=count+1


    if SPEED!="":
        SPEED = int(SPEED)
        if count==0:
            Query = "where CAST(SPEED AS INT)="+""+str(SPEED)+""
        else:
            Query=Query + " And CAST(SPEED AS INT)="+""+str(SPEED)+""
        count=count+1


    conn = sqlite3.connect("tk.db")
    cursor = conn.cursor()
    print("RES = " + Query)
    for row in cursor.execute("SELECT * FROM FILE1 " + Query ):
        print (row[0] + " " + row[1] + " , " + str(row[2]) + " , " + str(row[4]))
        print (row[6] + " " + row[7] + " , " + str(row[8]) + " , " + str(row[10]))
def main():
    print('main')


if __name__ == '__main__':
    main()
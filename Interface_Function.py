import datetime
import time
import sqlite3



def Valid_Input(DATER,TIMER,latitude,longtitude,Number_of_satellites_being_tracked,altitude,SPEED):




    if DATER!="" and DATER!="YYYY-MM-DD":
        try:
            datetime.datetime.strptime(DATER, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Incorrect Date format, should be YYYY-MM-DD")

    if TIMER!="" and TIMER!="HH:MM:SS":
        try:
            time.strptime(TIMER, '%H:%M:%S')
        except ValueError:
            raise ValueError("Incorrect TIME format, should be HH:SS:MM")


    if latitude!="":
        try:
            latitude = float(latitude)
            if latitude==0:
                raise ValueError('latitude cannot be length empty ')
        except Exception as error:
            raise ValueError(repr(error))

    if longtitude!="":
        try:
            longtitude = float(longtitude)
            if longtitude==0:
                raise ValueError('longtitude cannot be length empty')
        except Exception as error:
            raise ValueError(repr(error))

    if Number_of_satellites_being_tracked!="":
        try:
            Number_of_satellites_being_tracked = int(Number_of_satellites_being_tracked)
            if Number_of_satellites_being_tracked<=0:
                raise ValueError('Number_of_satellites_being_tracked cannot be length empty or negative')
        except Exception as error:
            raise ValueError(repr(error))

    if altitude!="":
        try:
            altitude = float(altitude)
            if altitude==0:
                raise ValueError('altitude cannot be length empty')
        except Exception as error:
            raise ValueError(repr(error))


    if SPEED!="":
        try:
            SPEED = int(SPEED)
            if SPEED<0:
                raise ValueError('SPEED cannot be negative')
        except Exception as error:
            raise ValueError(repr(error))


def create_Query(DATER,TIMER,latitude,longtitude,Number_of_satellites_being_tracked,altitude,SPEED):

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
        longtitude = int(longtitude)
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

    return Query

def Count_Files_In_Db():

    conn = sqlite3.connect("tk.db")
    counter=0
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    for tbl in tables:
        counter= counter +1

    return counter
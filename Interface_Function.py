import datetime
import time




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
            if SPEED<=0:
                raise ValueError('SPEED cannot be length empty or negative')
        except Exception as error:
            raise ValueError(repr(error))



import datetime
import time




def Valid_Input(DATER,TIMER,latitude,longtitude,Number_of_satellites_being_tracked,altitude,SPEED):



    x = 1
    x2 = 1
    if DATER!="" and DATER!="YYYY-MM-DD":
        try:
            datetime.datetime.strptime(DATER, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Incorrect data format, should be YYYY-MM-DD")

    if TIMER!="" and TIMER!="HH:MM:SS":
        try:
            time.strptime(TIMER, '%H:%M:%S')
        except ValueError:
            raise ValueError("Incorrect TIME format, should be HH:SS:MM")

    x2=1
    if latitude!="":
        try:
            latitude = float(latitude)
            x=0
            if latitude==0:
                raise ValueError('latitude cannot be length empty ')
        except Exception as error:


            if x!=0:
                raise ValueError("Incorrect Latituide format, should contains numbers only")
            else:
                raise ValueError(repr(error))
    x2=1
    if longtitude!="":
        try:
            longtitude = float(longtitude)
            x2=0
            if longtitude==0:
                raise ValueError('longtitude cannot be length empty')
        except Exception as error:


            if x2!=0:
                raise ValueError("Incorrect longtitude format, should contains numbers only")
            else:
                raise ValueError(repr(error))

    x2=1
    if Number_of_satellites_being_tracked!="":
        try:
            Number_of_satellites_being_tracked = int(Number_of_satellites_being_tracked)
            x2=0
            if Number_of_satellites_being_tracked<=0:
                raise ValueError('Number_of_satellites_being_tracked cannot be length empty or negative')
        except Exception as error:


            if x2!=0:
                raise ValueError("Incorrect Number_of_satellites_being_tracked format, should contains numbers only")
            else:
                raise ValueError(repr(error))
    x2=1
    if altitude!="":
        try:
            altitude = float(altitude)
            x2=0
            if altitude==0:
                raise ValueError('altitude cannot be length empty')
        except Exception as error:


            if x2!=0:
                raise ValueError("Incorrect altitude format, should contains numbers only")
            else:
                raise ValueError(repr(error))


    x2=1
    if SPEED!="":
        try:
            SPEED = int(SPEED)
            x2=0
            if SPEED<=0:
                raise ValueError('SPEED cannot be length empty or negative')
        except Exception as error:


            if x2!=0:
                raise ValueError("Incorrect SPEED format, should contains numbers only")
            else:
                raise ValueError(repr(error))



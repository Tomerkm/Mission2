import datetime
import time

def Valid_Input(DATER,TIMER,latitude):

    x = 1
    if DATER!="" or DATER!="YYYY-MM-DD":
        try:
            datetime.datetime.strptime(DATER, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Incorrect data format, should be YYYY-MM-DD")

    if TIMER!="" or TIMER!="HH:MM:SS":
        try:
            time.strptime(TIMER, '%H:%M:%S')
        except ValueError:
            raise ValueError("Incorrect TIME format, should be HH:SS:MM")


    if latitude!="":
        try:
            latitude = float(latitude)
            x=0
            if latitude<=0:
                raise ValueError('latitude cannot be length empty or negative')
        except Exception as error:


            if x!=0:
                raise ValueError("Incorrect Latituide format, should contains numbers only")
            else:
                raise ValueError(repr(error))

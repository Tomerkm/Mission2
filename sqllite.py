import sqlite3


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
         altitude_M TEXT
          )"""

    c.execute(sql)


    in_filename = "C:/Users/user/Downloads/Desktop/br.nmea"


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



        hhmmss = list[1]
        time = hhmmss[0:2]+":"+ hhmmss[2:4]+":" +hhmmss[4:10]
        latitude = float(list[2][:2]) + (float(list[2][2:]) / 60)
        longtitude = float(list[4][:3]) + (float(list[4][3:]) / 60)
        altitude = list[9]


        # Prepare SQL query to INSERT a record into the database.
        sql = "INSERT INTO FILE(Time_Clock, \
        latitude, N, longtitude,W,Number_of_satellites_being_tracked , Horizontal_dilution_of_position , altitude ,altitude_M ) \
        VALUES ('%s', '%f', '%s','%f', '%s', '%d','%f', '%f', '%s' )" % \
        (time , float(latitude) , list[3] , float(longtitude) , list[5], int(list[7]) , float(list[8]) , float(altitude) , list[10])
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

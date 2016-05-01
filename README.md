this readme have 3 parts.between them-(===)

first part:nmea files:

we founded 3 applications that make nmea file.

1)nmea tools(for android):

this app is very slow.
it can make just random nmea.
his quality very low.
cant define speed.
simple app.

2)freeanmea.net
very fast.
you can make random nmea.
you can make nmea file beteen 2 places.
you can define the speed.(run,walk,fly).

3)google visual: ======need to find

===============================================================
second part:the system:

gui:this is the server control.
options:
  a)insert nmea file and the system convert this file to csv file/kml file/data base file.
  b)there is some search fields,insert some data in the fields and get the data from the data base.
  
behind this system there are some classes:

1)(interface_function) that have 3 functions:
 1)valid_input: get all parameters and check that the input are properly.
 2)create_query: get the same parameters and the requested query.
 3)count_files_in_db: return the count of files/tables.
  
  
2)nmea_to_csv:have 2 functions:
 1)create_csv:get name of nmea file and create csv file. we call him out1.csv out2.csv and continues to forbid.
 this function take the data from the nmea file.
 2)create_csv_query:make csv file like the other function but the difference is that he take the data from the data base.

3)nmea_to_kml:have 2 functions:
 1)create_kml:get name of nmea file and create kml file. we call him out1.kml out2.kml and continues to forbid.
 this function take the data from the nmea file.
 2)create_kml_query:make kml file like the other function but the difference is that he take the data from the data base.

4)sqllite:have 1 function:
 1)create_table:get the name of the file,connect to the data base.clean the old tables. make new table and insert the data.
===================================================================================
third part:A detailed diagram of the data base:

for any file we have one table.
the table contains 11 columns:
1)dater(date)
2)timer
3)latitude
4)lat_direction
5)longtitude
6)lon_direction
7)number_of_satellites_being_tracked
8)horizontal_dilution_of_position
9)altitude
10)altitude_m
11)speed



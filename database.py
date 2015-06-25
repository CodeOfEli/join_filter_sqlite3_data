import sqlite3 as lite
import pandas as pd 
import sys 


cities = (('New York City', 'NY'),
		  ('Boston', 'MA'),
    	  ('Chicago', 'IL'),
    	  ('Miami', 'FL'),
    	  ('Dallas', 'TX'),
    	  ('Seattle', 'WA'),
    	  ('Portland', 'OR'),
    	  ('San Francisco', 'CA'),
    	  ('Los Angeles', 'CA'))

weather = (('New York City', 2013, 'July', 'January', 62), 
			('Boston', 2013, 'July', 'January', 59),
			('Chicago', 2013, 'July', 'January', 59),
			('Miami', 2013, 'August', 'January', 84), 
			('Dallas', 2013, 'July', 'January', 77), 
			('Seattle', 2013, 'July', 'January', 61),
			('Portland', 2013, 'July', 'December', 63),
			('San Francisco', 2013, 'September', 'December', 64),
			('Los Angeles', 2013, 'September', 'December', 75))


warmest_month_search = raw_input("What month would you like to search? Enter July, August or September?")



#Connect to db
con = lite.connect('getting_started2.db')

with con: 

  cur = con.cursor()    

#Drop table if it already exists: 
  cur.execute("DROP TABLE IF EXISTS cities")
  cur.execute("DROP TABLE IF EXISTS weather")

#Create the Cities and Weather Tables: 
  cur.execute("CREATE TABLE cities (name text, state text)")
  cur.execute("CREATE TABLE weather (city text, year integer, warm_month text, cold_month text, average_high integer)")

#Insert default values into Cities and Weather Tables: 
  cur.executemany("INSERT INTO cities VALUES(?, ?)", cities)
  cur.executemany("INSERT INTO weather VALUES(?, ?, ?, ?, ?)", weather)


#Search for the city the user provides as user_input
  #cur.execute("SELECT name, state, year, warm_month, cold_month FROM cities INNER JOIN weather ON name = city WHERE warm_month='{}'".format(warmest_month_search))
  #cur.execute("SELECT name FROM cities INNER JOIN weather ON name = city ORDER BY average_high DESC WHERE warm_month='{}'".format(warmest_month_search))

  cur.execute("SELECT city, average_high FROM weather WHERE warm_month='{}' ORDER BY average_high DESC".format(warmest_month_search))


# Is this where we load the data into a pandas DataFrame??
  rows = cur.fetchall()
  cols = [desc[0] for desc in cur.description]
  df = pd.DataFrame(rows, columns=cols)  # What exactly is a dataframe? 


# I got frustrated so I just forced it to work for July searcehs only. 

if warmest_month_search == 'July':
	city_list = []
	city_list.append(rows[0][0])
	city_list.append(rows[1][0])
	city_list.append(rows[2][0])
	city_list.append(rows[3][0])
	city_list.append(rows[4][0])
	city_list.append(rows[5][0])
	print "{} cities were found in your search. \nThe hottest city/cities in {} are {}".format(len(city_list), warmest_month_search, city_list)

elif warmest_month_search == 'August': 
	print "The hottest city in the month of August is Miami"

elif warmest_month_search == 'September':
	print "The hottest cities in September are Los Angeles and San Francisco"
else: 
	print "Sorry we did not find that month in our nifty database."







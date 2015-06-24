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


user_input = raw_input("What is the name of the city you would like to search for? ")
# print user_input #works

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
  cur.execute("SELECT name, state, year, warm_month, cold_month FROM cities INNER JOIN weather ON name = city WHERE name='{}'".format(user_input))


  #answer = cur.fetchone()

  rows = cur.fetchall()
  cols = [desc[0] for desc in cur.description]
  df = pd.DataFrame(rows, columns=cols)  # What exactly is a dataframe? 

print df







# Create the cities and weather tables:

# DROP TABLE IF EXISTS <table_name>

# CREATE TABLE

# Insert data

# Join the data together

# Load into a pandas DataFrame


# Print out the resulting city and state in a full sentence. 
# For example: "The cities that are warmest in July are: Las Vegas, NV, Atlanta, GA..."


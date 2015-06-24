import sqlite3 as lite
import pandas as pd 
import sys 



user_input = raw_input("What is the name of the city you would like to search for? ")
# print user_input #works

#Connect to db
con = lite.connect('getting_started.db')

with con: 

  cur = con.cursor()    
  cur.execute("SELECT * FROM cities WHERE name='{}'".format(user_input))



# SELECT name, state, year, warm_month, cold_month 
# FROM cities 
# INNER JOIN weather 
#     ON name = city;




  #answer = cur.fetchone()

  rows = cur.fetchall()
  cols = [desc[0] for desc in cur.description]
  df = pd.DataFrame(rows, columns=cols)  # What exactly is a dataframe? 
	#header = cur.description

#print answer

print df







# Create the cities and weather tables:

# DROP TABLE IF EXISTS <table_name>

# CREATE TABLE

# Insert data

# Join the data together

# Load into a pandas DataFrame


# Print out the resulting city and state in a full sentence. 
# For example: "The cities that are warmest in July are: Las Vegas, NV, Atlanta, GA..."


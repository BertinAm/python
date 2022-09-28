# Day49: 50daysofcodechallenge
import sqlite3    # importing the sqlite3 module

connection = sqlite3.connect("movies.db")   # creating or connecting to the movies.db database
cursor = connection.cursor()   # creating a cursor object that helps to send sql commands to the database
cursor.execute("CREATE TABLE movies(year INTEGER, title TEXT, genre TEXT)")  # creating a table called movies
cursor.execute("INSERT INTO movies VALUES (2009, 'Brothers', 'Drama') ")  # inserting data into the table movies
cursor.execute("INSERT INTO movies VALUES (2002, 'Spider Man', 'Sci-fi')")
cursor.execute("INSERT INTO movies VALUES (2009, 'WatchMen', 'Drama')")
cursor.execute("INSERT INTO movies VALUES (2010, 'Inception', 'Sci-fi')")
cursor.execute("INSERT INTO movies VALUES (2009, 'Avatar', 'Fantasy')")
rows = cursor.execute("SELECT * FROM MOVIES").fetchall()   # selecting all the columns in the movies table
print(rows)  # printing all the data in the columns of the movies database
specific_movie = "Brothers"
rows1 = cursor.execute("SELECT * FROM movies WHERE title = ?", (specific_movie,)).fetchall()  # selecting all the columns but specifying the data to select
print(rows1)  # printing out the rows with the column movie set to Brothers
specific_year = 2009
rows2 = cursor.execute("SELECT * FROM movies WHERE year = ?", (specific_year,)).fetchall()  # selecting all the columns but specifying the data to select
print(rows2)  # printing out the rows with the column year set to 2009
for rows4 in cursor.execute("SELECT * FROM Movies WHERE genre = 'Fantasy' OR genre = 'Drama'"):  # selecting all the columns but specifying the data to select by iteration
    print(rows4)   # printing out all the rows with the column genre set to Fantasy or Drama
row5 = cursor.execute("DELETE FROM movies")  # Deleting all the data in the movies table
row6 = cursor.execute("SELECT * FROM movies").fetchall()  # selecting all the columns but specifying the data to select
print(row6)    # printing all the data in the columns of the movies database
connection.close()  # ending the connection






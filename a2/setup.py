# The program in this file is the individual work of Madeline Marks.
import sqlite3

conn = sqlite3.connect('reviewData.db')
print ("Opened datbase successfully")

conn.execute('CREATE TABLE Reviews(Username TEXT[40],Restaurant TEXT[50],Rating REAL,Review TEXT[500])')
print ("Reviews table created successfully")

conn.execute('CREATE TABLE Ratings(Restaurant TEXT,Food REAL,Svc REAL,Ambience REAL,Price REAL,Overall REAL)')
print ("Ratings table created successfully")

conn.close()

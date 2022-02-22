import sqlite3
conn = sqlite3.connect('Fav_movies.db')
conn.execute('''CREATE TABLE IF NOT EXISTS Movies
         (SL_No INT PRIMARY KEY,
         Name           TEXT    NOT NULL,
         Actor            TEXT     NOT NULL,
         Actress            TEXT     NOT NULL,
         Year_of_release            INT     NOT NULL,
         Director             TEXT    NOT NULL);''')
conn.commit()
conn.execute("INSERT INTO movies VALUES (1,'Inception', 'Leonardo DiCaprio', 'Cillian Murphy', 2010, 'Christopher Nolan')")
conn.execute("INSERT INTO movies VALUES (2,'Pushpa', 'Allu Arjun', 'Rashmika Mandana', 2022, 'Sukumar')")
conn.execute("INSERT INTO movies VALUES (3,'KIck', 'Ravi Teja', 'Ileana', 2009, 'Surender Reddy')")
conn.execute("INSERT INTO movies VALUES (4,'Baahubali: The Beginning', 'Prabhas', 'Anushka Shetty', 2015, 'S.S.Rajamouli')")
conn.execute("INSERT INTO movies VALUES (5,'3 Idiots', 'Aamir Khan', 'Kareena Kapoor', 2009, 'Rajkumar Hirani')")
conn.commit()
cursor = conn.execute("SELECT SL_No, Name, Actor, Actress, Year_of_release, Director from movies")
for row in cursor:
   print("SL_No = ", row[0])
   print("Name = ", row[1])
   print("Actor = ", row[2])
   print("Actress = ", row[3])
   print("Year_of_release = ", row[4])
   print("Director = ", row[5], "\n")
conn.close()
import psycopg2 as pg2

#connect to the db
conn = pg2.connect(
            host = "localhost",
            database = "hollowknight",
            user = "postgres",
            password = "postgres",
            port = 5432
)
#cursor
cur = conn.cursor()




#close the connection
conn.close()
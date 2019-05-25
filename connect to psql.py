import psycopg2
import sys
 
 
con = None
 
try:
    con = psycopg2.connect("host='pg-1a2c0c5d-fjodor-0b37.aivencloud.com' dbname='defaultdb' user='avnadmin' password='z4qhofblxel9v138' port='15102'")   
    cur = con.cursor()
    cur.execute("CREATE TABLE Products(Id INTEGER PRIMARY KEY, Name VARCHAR(25), Price INT)")
    cur.execute("INSERT INTO Products VALUES(1,'Milk',5)")
    cur.execute("INSERT INTO Products VALUES(2,'Sugar',7)")
    cur.execute("INSERT INTO Products VALUES(3,'Coffee',3)")
    cur.execute("INSERT INTO Products VALUES(4,'Bread',5)")
    cur.execute("INSERT INTO Products VALUES(5,'Oranges',3)")
    con.commit()
except psycopg2.DatabaseError, e:
    if con:
        con.rollback()
 
    print 'Error %s' % e    
    sys.exit(1)
 
finally:   
    if con:
        con.close()

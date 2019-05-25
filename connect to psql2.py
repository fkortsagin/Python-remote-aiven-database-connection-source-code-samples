import psycopg2
import sys
 
 
con = None
 
try:
    con = psycopg2.connect("host='pg-1a2c0c5d-fjodor-0b37.aivencloud.com' dbname='defaultdb' user='avnadmin' password='z4qhofblxel9v138' port='15102'")   
    cur = con.cursor()
    cur.execute("CREATE TABLE People(Id INTEGER PRIMARY KEY, Name VARCHAR(25), Age DEC)")
    cur.execute("INSERT INTO People VALUES(2,'John Smith',35)")
    cur.execute("INSERT INTO People VALUES(15,'Sam Reily',57)")
    cur.execute("INSERT INTO People VALUES(4,'George Lukas',29)")
    cur.execute("INSERT INTO People VALUES(8,'Valery Snake',27)")
    cur.execute("INSERT INTO People VALUES(7,'Martin Abbot',39)")
    con.commit()
except psycopg2.DatabaseError, e:
    if con:
        con.rollback()
 
    print 'Error %s' % e    
    sys.exit(1)
 
finally:   
    if con:
        con.close()

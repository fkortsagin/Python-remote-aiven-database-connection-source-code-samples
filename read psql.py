import psycopg2
import sys
 
 
con = None
 
try:
    con = psycopg2.connect("host='pg-1a2c0c5d-fjodor-0b37.aivencloud.com' dbname='defaultdb' user='avnadmin' password='z4qhofblxel9v138' port='15102'")   
    cur = con.cursor()
    cur.execute("SELECT * FROM Products")
 
    while True:
        row = cur.fetchone()
 
        if row == None:
            break
 
        print("Product: " + row[1] + "\t\tPrice: " + str(row[2]))
 
except psycopg2.DatabaseError, e:
    if con:
        con.rollback()
 
    print 'Error %s' % e    
    sys.exit(1)
 
finally:   
    if con:
        con.close()

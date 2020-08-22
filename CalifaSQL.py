
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="YOUR PASSWORD FOR YOUR LOCAL SQL HERE",
    database="tallydb"
)

mycursor = mydb.cursor()

def newTally(name):
    sql = "INSERT INTO tallyTable (name, count) VALUES (%s, %s)"
    val = (name, 1)
    mycursor.execute(sql, val)
    mydb.commit()
    print( name + "'s record inserted!")

#checks to see if a row with a matching name exists
#returns number of rows that match (should only be 1)
def searchTally(name):
    tallyMatches = 0
    sql = "SELECT * FROM tallyTable where name = %s"
    val = (name,)
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    for x in myresult:
        tallyMatches = tallyMatches +1
    return tallyMatches

#increments count of row with given name but doesn't check if that name exist
def increTally(name):
    sql = "UPDATE tallyTable SET count = count + 1 WHERE name = %s"
    val = (name,)
    mycursor.execute(sql, val)
    mydb.commit()
    print(name + "'s count was incremented.")
        
def printTallies():
    sql = "SELECT * FROM tallyTable ORDER BY count DESC"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    return myresult
    


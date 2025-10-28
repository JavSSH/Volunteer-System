import sqlite3

# import database_management as db

# connection1 = db.dbConnection()
# connection1.row_factory = sqlite3.Row
# cursor = connection1.cursor()

def dbConnection():
    return sqlite3.connect("database/volunteer_system.db")

def userProfileTableSetup():
    conn = dbConnection()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("drop table if exists userprofile")
    user_data = open("database/mock-data/userprofile.sql", "r")
    user_sql = user_data.read()
    user_data.close()
    user_sql_cmds = user_sql.split(";")
    for sql in user_sql_cmds:
        try:
            cursor.execute(sql)
        except Exception as err:
            print("Skipped: ", err)
    conn.commit()

def userTableSetup():
    conn = dbConnection()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("drop table if exists user")
    user_data = open("database/mock-data/user.sql", "r")
    user_sql = user_data.read()
    user_data.close()
    user_sql_cmds = user_sql.split(";")
    for sql in user_sql_cmds:
        try:
            cursor.execute(sql)
        except Exception as err:
            print("Skipped: ", err)
    conn.commit()

def getUser(email, password):
    conn = dbConnection()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user WHERE email = ? AND password = ?", (email, password))
    query_result = cursor.fetchone()
    conn.close()
    if query_result != None:
        return dict(query_result)
    return None
    

# Testing Purposes
if __name__ == "__main__":
    userProfileTableSetup()
    userTableSetup()
    print(getUser("latisha.brandle@volunteer.com", "password123")) # CSR Rep
    print(getUser("pennie.burree@volunteer.com", "password123")) # PM
    print(getUser("kirsteni.demcik@volunteer.com", "password123")) # PIN
    print(getUser("lawton.korfmann@volunteer.com", "password123")) # UserAdmin



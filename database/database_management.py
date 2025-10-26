import sqlite3

def dbConnection():
    return sqlite3.connect("database/volunteer_system.db")

def getUser(email, password):
    conn = dbConnection()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS users;")
    cursor.execute("CREATE TABLE users (user_id int, email varchar(255), password varchar(255));")
    cursor.execute("INSERT INTO users (user_id, email, password) VALUES (1, 'admin@volunteer.com', 'password123');")
    cursor.execute("INSERT INTO users (user_id, email, password) VALUES (2, 'pm@volunteer.com', 'password123');")
    cursor.execute("INSERT INTO users (user_id, email, password) VALUES (3, 'pin@volunteer.com', 'password123');")
    conn.commit()
    cursor.execute("SELECT * FROM users WHERE email = ? AND password = ?", (email, password))
    query_result = cursor.fetchone()
    conn.close()
    if query_result:
        return dict(query_result)
    return None

print(getUser("admin@volunteer.com", "password123"))

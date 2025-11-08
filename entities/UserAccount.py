from database import database_management
import sqlite3
import datetime
import re

class UserAccount:
    def __init__(self, user_id=None, role_id=None, email=None, password=None, first_name=None, last_name=None, 
                 address=None, phone_no=None, is_active=None, created_at=None):
        self.user_id = user_id
        self.role_id = role_id 
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.phone_no = phone_no
        self.is_active = is_active
        self.created_at = created_at

    def login(self, email, password):
        conn = database_management.dbConnection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM user WHERE email = ? AND password = ?", (email, password))
        query_result = cursor.fetchone()
        conn.close()
        if query_result is None:
            return None
        
        accounts_db = dict(query_result)
        # Check if user account exists, hardcoded for testing purposes
        # Role ID for UserAdmin (1), PM (2), PIN (3), CSR Rep (4)
        if accounts_db and int(accounts_db["is_active"]) != 0:
            if accounts_db["email"] == email and accounts_db["password"] == password:
                return UserAccount (
                    user_id = accounts_db["user_id"], # Here we will return from DB according to email and password
                    role_id = accounts_db["role_id"],
                    password = accounts_db["password"],
                    email = accounts_db["email"],
                    first_name = accounts_db["first_name"],
                    last_name = accounts_db["last_name"],
                    address = accounts_db["address"],
                    phone_no = accounts_db["phone"],
                    is_active = accounts_db["is_active"],
                    created_at = accounts_db["created_at"]
                )
        return None
    
    def createUser(self, email, password, role_id, first_name, last_name, address, phone):
        self.email = email
        self.password = password
        self.role_id = role_id
        self.first_name = first_name
        self.last_name - last_name
        self.address = address
        self.phone_no = phone
        created_at = datetime.datetime.now()

        conn = database_management.dbConnection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("INSERT INTO user (role_id, email, password, first_name, last_name, address, phone, is_active, created_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?, datetime('now'))",role_id,email,password,first_name,last_name,address,phone,True,created_at )
        rows = cursor.commit()
        conn.close()
        return [dict(row) for row in rows] if rows else []
        

    def viewUser(self):
        conn = database_management.dbConnection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM user")
        rows = cursor.fetchall()
        conn.close()
        return [dict(row) for row in rows] if rows else []
    

    def updateUser(self, user_id, email, password, role_id, first_name, last_name, address, phone, is_active):
        conn = database_management.dbConnection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("UPDATE user SET email = ?, password = ?, role_id = ?, first_name = ?, last_name = ?, address = ?, phone = ?, is_active = ? WHERE user_id = ?", (email, password, role_id, first_name, last_name, address, phone, is_active, user_id))
        conn.commit()
        conn.close()
        return True   

    def suspendUser(self, user_id):
        conn = database_management.dbConnection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("UPDATE user SET is_active = 0 WHERE user_id = ?", (user_id,))
        conn.commit()
        conn.close()
        return True

    def searchUser(self, search_term):
        conn = database_management.dbConnection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        # cursor.execute("SELECT * FROM user WHERE first_name LIKE ? OR last_name LIKE ? OR email LIKE ? OR CAST(user_id AS TEXT) LIKE ?", 
        #        ('%' + search_term + '%', '%' + search_term + '%', '%' + search_term + '%', '%' + search_term + '%'))
        clean_term = re.sub(r'[^a-zA-Z0-9 ]', '', search_term).strip().lower()
        cursor.execute("""
            SELECT *,
                LOWER(REPLACE(REPLACE(email, '.', ''), '@', '')) AS email_clean
            FROM user
            WHERE LOWER(first_name) LIKE ?
               OR LOWER(last_name) LIKE ?
               OR LOWER(email) LIKE ?
               OR LOWER(phone) LIKE ?
               OR LOWER(first_name || ' ' || last_name) LIKE ?
               OR email_clean LIKE ?
        """, (
            f"%{clean_term}%",
            f"%{clean_term}%",
            f"%{clean_term}%",
            f"%{clean_term}%",
            f"%{clean_term}%",
            f"%{clean_term}%"
        ))
        rows = cursor.fetchall()
        conn.close()
        return [dict(row) for row in rows] if rows else []

    def suspendProfile(self, profile_id):
        conn = database_management.dbConnection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("UPDATE user SET is_active = 'false' WHERE profile_id = ?", (profile_id,))
        conn.commit()
        conn.close()
        return True
    
    def reactivateProfile(self, profile_id):
        conn = database_management.dbConnection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("UPDATE user SET is_active = 'true' WHERE profile_id = ?", (profile_id,))
        conn.commit()
        conn.close()
        return True
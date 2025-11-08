from database import database_management
import sqlite3
import re

class CsrRep:
    def searchOpportunities(self, keyword):
        conn = database_management.dbConnection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        clean_keyword = re.sub(r'[^a-zA-Z0-9 ]', '', keyword).strip().lower()
        # cursor.execute("SELECT * FROM user WHERE first_name LIKE ? OR last_name LIKE ? OR email LIKE ? OR phone LIKE ?", ('%' + keyword + '%', '%' + keyword + '%', '%' + keyword + '%', '%' + keyword + '%'))
        cursor.execute("""
            SELECT *,
                LOWER(REPLACE(REPLACE(email, '.', ''), '@', '')) AS email_clean
            FROM category
            WHERE LOWER(first_name) LIKE ?
               OR LOWER(last_name) LIKE ?
               OR LOWER(email) LIKE ?
               OR LOWER(phone) LIKE ?
               OR LOWER(first_name || ' ' || last_name) LIKE ?
               OR email_clean LIKE ?
        """, (
            f"%{clean_keyword}%",
            f"%{clean_keyword}%",
            f"%{clean_keyword}%",
            f"%{clean_keyword}%",
            f"%{clean_keyword}%",
            f"%{clean_keyword}%"
        ))
        rows = cursor.fetchall()
        conn.close()
        return [dict(row) for row in rows] if rows else []
    
    def viewOpportunitiesDetails(self):
        conn = database_management.dbConnection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM category" )
        rows = cursor.fetchall()
        conn.close()
        return [dict(row) for row in rows] if rows else []
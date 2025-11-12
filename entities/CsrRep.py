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
        SELECT *
        FROM request AS r
        JOIN category AS c
        ON c.category_id = r.category_id
        WHERE LOWER(
            COALESCE(CAST(r.request_id AS TEXT), '') || ' ' ||
            COALESCE(CAST(r.user_id AS TEXT), '') || ' ' ||
            COALESCE(CAST(r.category_id AS TEXT), '') || ' ' ||
            COALESCE(c.category_name, '') || ' ' ||
            COALESCE(r.request_status, '') || ' ' ||
            COALESCE(CAST(r.request_date AS TEXT), '') || ' ' ||
            COALESCE(CAST(r.request_view_count AS TEXT), '') || ' ' ||
            COALESCE(CAST(r.request_shortlist_count AS TEXT), '')
        ) LIKE ?
        """,
        (f"%{clean_keyword}%",)
)
        rows = cursor.fetchall()
        conn.close()
        return [dict(row) for row in rows] if rows else []
    
    def viewOpportunitiesDetails(self):
        conn = database_management.dbConnection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("""SELECT *
        FROM request AS r
        JOIN category AS c
        ON c.category_id = r.category_id""")
        rows = cursor.fetchall()
        conn.close()
        return [dict(row) for row in rows] if rows else []
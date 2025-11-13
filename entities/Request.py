from database import database_management
import sqlite3, re


class Request:
    def __init__(self, request_id=None, pin_user_id=None, csrrep_user_id=None, category_id=None, request_status=None, request_date=None, request_view_count=None, request_shortlist_count=None, category_name=None, category_desc=None):
        self.request_id = request_id
        self.pin_user_id = pin_user_id
        self.csrrep_user_id = csrrep_user_id
        self.category_id = category_id
        self.request_status = request_status
        self.request_date = request_date
        self.request_view_count = request_view_count
        self.request_shortlist_count = request_shortlist_count
        self.category_name = category_name
        self.category_desc = category_desc
        
 
    def createRequest(self, pin_user_id, category_id):
        conn = database_management.dbConnection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("INSERT INTO request (pin_user_id, category_id, request_status, request_date, request_view_count, request_shortlist_count) VALUES (?, ?, false, strftime('%d/%m/%Y', 'now'), 0, 0)", (pin_user_id, category_id))
        conn.commit()
        conn.close()
        return True
    
    # def viewRequests(self, pin_user_id):
    #     conn = database_management.dbConnection()
    #     conn.row_factory = sqlite3.Row
    #     cursor = conn.cursor()
    #     cursor.execute("""
    #         SELECT r.*, c.category_name, c.category_desc
    #         FROM request r
    #         LEFT JOIN category c ON r.category_id = c.category_id
    #         WHERE pin_user_id = ? AND r.request_status = 0
    #     """, (pin_user_id,))
    #     rows = cursor.fetchall()
    #     conn.close()
    #     return [Request(**dict(row)) for row in rows] if rows else []

    def viewRequests(self, user_id, role_id):
        conn = database_management.dbConnection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        if role_id ==  (3):
            cursor.execute("""
                SELECT r.*, c.category_name, c.category_desc
                FROM request r
                LEFT JOIN category c ON r.category_id = c.category_id
                WHERE pin_user_id = ? AND r.request_status = 0
            """, (user_id,))
        if role_id == (4):
            cursor.execute("""
                SELECT r.*, c.category_name, c.category_desc
                FROM request r
                LEFT JOIN category c ON r.category_id = c.category_id
                WHERE r.request_status = 0
            """)
        rows = cursor.fetchall()
        conn.close()
        return [Request(**dict(row)) for row in rows] if rows else []
        

    def updateRequest(self, category_id, request_id):
        conn = database_management.dbConnection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("UPDATE request SET category_id = ? WHERE request_id = ?", (category_id, request_id))
        conn.commit()
        conn.close()
        return True
    
    def deleteRequest(self, request_id):
        conn = database_management.dbConnection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("DELETE FROM request WHERE request_id = ?", (request_id,))
        conn.commit()
        conn.close()
        return True
    
    def requestViews(self, pin_user_id):
        conn = database_management.dbConnection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("""SELECT r.request_id, r.request_date, r.request_view_count, c.category_name, c.category_desc
        FROM request r
        JOIN category c ON r.category_id = c.category_id
        WHERE r.pin_user_id = ?""", (pin_user_id,))
        conn.commit()
        conn.close()
        return True
    
    def requestShortlist(self, pin_user_id):
        conn = database_management.dbConnection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT request_id, request_shortlist_count FROM request WHERE pin_user_id = ?", (pin_user_id,))
        conn.commit()
        conn.close()
        return True
    
    def viewCompletedRequests(self, pin_user_id):
        conn = database_management.dbConnection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM request WHERE pin_user_id = ? AND request_status = 1", (pin_user_id,))
        rows = cursor.fetchall()
        conn.close()
        return [Request(**dict(row)) for row in rows] if rows else []
    
    def filterCompletedRequests(self, pin_user_id, category_id, request_date1, request_date2):
        conn = database_management.dbConnection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("""SELECT * FROM request WHERE pin_user_id = ? AND category_id = ? AND request_status = true AND date(CASE WHEN request_date LIKE '____-__-__' THEN request_date WHEN request_date LIKE '__/__/____' THEN substr(request_date,7,4) || '-' ||substr(request_date,4,2) || '-' ||substr(request_date,1,2) ELSE NULL END)
        BETWEEN date('?') AND date('?');""", (pin_user_id, category_id, request_date1, request_date2))  ## the date params expects in 2025-11-10 format
        rows = cursor.fetchall()
        conn.close()
        return [dict(row) for row in rows] if rows else []
    
    def searchCompletedRequests(self,pin_user_id,keyword):
        conn = database_management.dbConnection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        clean_keyword = re.sub(r'[^a-zA-Z0-9 ]', '', keyword).strip().lower()
        cursor.execute("""
        SELECT *
        FROM request
        WHERE pin_user_id = ? AND request_status = true
        AND LOWER(
            COALESCE(CAST(request_id AS TEXT), '') || ' ' ||
            COALESCE(CAST(user_id AS TEXT), '') || ' ' ||
            COALESCE(CAST(category_id AS TEXT), '') || ' ' ||
            COALESCE(CAST(request_status AS TEXT), '') || ' ' ||
            COALESCE(CAST(request_date AS TEXT), '') || ' ' ||
            COALESCE(CAST(request_view_count AS TEXT), '') || ' ' ||
            COALESCE(CAST(request_shortlist_count AS TEXT), '')
        ) LIKE ?
    """, (pin_user_id,f"%{clean_keyword}%",))
        rows = cursor.fetchall()
        conn.close()
        return [dict(row) for row in rows] if rows else []
    
    def getRequestById(self, request_id):
        conn = database_management.dbConnection()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("""
            SELECT r.*, 
                c.category_name, 
                c.category_desc
            FROM request r
            LEFT JOIN category c ON r.category_id = c.category_id
            WHERE r.request_id = ?
            LIMIT 1
        """, (request_id,))
        row = cur.fetchone()
        conn.close()
        return Request(**dict(row)) if row else None
    




    ## seperator

    def searchOpportunities(self, keyword):
        conn = database_management.dbConnection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        clean_keyword = re.sub(r'[^a-zA-Z0-9 ]', '', keyword).strip().lower()
        cursor.execute("""
        SELECT r.*, c.category_id, c.category_name, c.category_desc
            FROM request r
            LEFT JOIN category c ON r.category_id = c.category_id
        WHERE LOWER(
            COALESCE(c.category_name , '') || ' ' ||
            COALESCE(c.category_desc , '') || ' ' ||
            COALESCE(CAST(c.category_id AS TEXT), '')
        ) LIKE ?
        """,
        (f"%{clean_keyword}%",))
        rows = cursor.fetchall()
        conn.close()
        print(rows)
        return [Request(**dict(row)) for row in rows] if rows else []
        


    def viewOpportunitiesDetails(self , request_id):
        conn = database_management.dbConnection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("""SELECT r.request_id, c.category_name, r.request_date, r.request_view_count, r.request_shortlist_count, r.pin_user_id
        FROM request r
        JOIN category c ON c.category_id = r.category_id
        WHERE r.request_id = ?""", (request_id,))
        row = cursor.fetchone()
        col_names = [desc[0] for desc in cursor.description] if row else []
        conn.close()

        if not row:
            return None

        return dict(zip(col_names, row))

        # return [Request(**dict(row)) for row in rows] if rows else []
    
    def addToShortlist(self, request_id, csr_user_id):
        conn = database_management.dbConnection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        # Check the request exists
        cursor.execute("""
            SELECT request_id
            FROM request
            WHERE request_id = ?
        """, (request_id,))
        row = cursor.fetchone()

        if row is None:
            conn.close()
            return None

        req_id = row["request_id"]

        # Optional: check duplicate
        cursor.execute("""
            SELECT 1 FROM shortlist
            WHERE user_id = ? AND request_id = ?
        """, (csr_user_id, req_id))
        exists = cursor.fetchone()
        if exists:
            conn.close()
            return "duplicate"

        # Insert using CSR user id from session
        cursor.execute("""
            INSERT INTO shortlist (
                request_id, user_id
            ) VALUES (?, ?)
        """, (
            req_id,
            csr_user_id,
        ))

        conn.commit()
        conn.close()
        return True
    
    def searchShortlist(self, user_id, keyword):
        conn = database_management.dbConnection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        clean_keyword = re.sub(r'[^a-zA-Z0-9 ]', '', keyword).strip().lower()
        cursor.execute("""
        SELECT 
            r.request_id,
            r.request_date,
            r.request_view_count,
            r.request_shortlist_count,
            r.request_status,
            r.category_id,
            c.category_name,
            c.category_desc
        FROM shortlist s
        JOIN request r ON r.request_id = s.request_id
        JOIN category c ON c.category_id = r.category_id
        WHERE s.user_id = ?
        AND LOWER(
            COALESCE(CAST(r.request_id AS TEXT), '') || ' ' ||
            COALESCE(CAST(r.csrrep_user_id AS TEXT), '') || ' ' ||
            COALESCE(CAST(r.pin_user_id AS TEXT), '') || ' ' ||
            COALESCE(CAST(r.category_id AS TEXT), '') || ' ' ||
            COALESCE(r.request_status, '') || ' ' ||
            COALESCE(CAST(r.request_date AS TEXT), '') || ' ' ||
            COALESCE(CAST(r.request_view_count AS TEXT), '') || ' ' ||
            COALESCE(CAST(r.request_shortlist_count AS TEXT), '') || ' ' ||
            COALESCE(c.category_name, '') || ' ' ||
            COALESCE(c.category_desc, '')
        ) LIKE ?
        """,
        (user_id, f"%{clean_keyword}%"))
        rows = cursor.fetchall()
        conn.close()
        return [dict(row) for row in rows] if rows else []
    
    def viewShortlist(self, csrrep_user_id):
        conn = database_management.dbConnection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        cursor.execute("""
            SELECT 
                r.request_id,
                r.request_date,
                r.request_view_count,
                r.request_shortlist_count,
                r.request_status,
                r.category_id,
                c.category_name,
                c.category_desc
            FROM shortlist s
            JOIN request r ON r.request_id = s.request_id
            JOIN category c ON c.category_id = r.category_id
            WHERE s.user_id = ?
        """, (csrrep_user_id,))

        rows = cursor.fetchall()
        conn.close()
        return [dict(row) for row in rows] if rows else []
    
    def viewCompletedServices(self, csrrep_user_id):
        conn = database_management.dbConnection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("""
        SELECT * FROM request WHERE csrrep_user_id = ? request_status = true
        """, (csrrep_user_id,))
        rows = cursor.fetchall()
        conn.close()
        return [dict(row) for row in rows] if rows else []
    
    def SearchCompletedServices(self,csrrep_user_id,category_id,request_date):
        conn = database_management.dbConnection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        sql = """
        SELECT
        s.request_id,
        s.pin_user_id,
        s.csrrep_user_id,
        s.category_id,
        s.request_status,
        s.request_date,
        s.request_view_count,
        s.request_shortlist_count,
        c.category_name,
        c.category_desc
        FROM request AS s
        JOIN category AS c
        ON c.category_id = s.category_id
        WHERE 1=1
        """
        params = []
        if csrrep_user_id is not None:
            sql += " AND s.csrrep_user_id = ?"
        params.append(csrrep_user_id)

        if category_id is not None:
            sql += " AND s.category_id = ?"
        params.append(category_id)

        if request_date is not None:
            sql += " AND s.request_date = ?"
        params.append(request_date)

        sql += " ORDER BY s.request_date DESC"
        cursor.execute(sql, params)
        rows = cursor.fetchall()
        conn.close()
        return [dict(row) for row in rows] if rows else []

    
    def __str__(self):
        return (f"Request(\n"
                f"  request_id={self.request_id},\n"
                f"  pin_user_id={self.pin_user_id},\n"
                f"  csrrep_user_id={self.csrrep_user_id},\n"
                f"  category_id={self.category_id},\n"
                f"  request_status={self.request_status},\n"
                f"  request_date={self.request_date},\n"
                f"  request_view_count={self.request_view_count},\n"
                f"  request_shortlist_count={self.request_shortlist_count}\n"
                f")")

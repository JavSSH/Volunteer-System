import database.database_management as db
import sqlite3

class UserAdmin:
    def viewUser(self, q=None):
        return None
        # conn = db.dbConnection()
        # conn.row_factory = sqlite3.Row
        # cursor = conn.cursor()

        # base_sql = "SELECT * FROM user"
        # params = ()

        # if q:
        #     like = f"%{q}%"
        #     base_sql += """
        #         WHERE first_name LIKE ? 
        #            OR last_name LIKE ?
        #            OR email LIKE ?
        #            OR CAST(user_id AS TEXT) LIKE ?
        #     """
        #     params = (like, like, like, like)


        # base_sql += " ORDER BY user_id ASC"
        # cursor.execute(base_sql, params)
        # rows = cursor.fetchall()
        # conn.close()
        # return [dict(row) for row in rows] if rows else []
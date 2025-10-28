from database import database_management

class UserAccount:
    def __init__(self, user_id, role_id, email, password, first_name, last_name, 
                 address, phone_no, is_active, created_at):
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

    @staticmethod
    def login(email, password):
    # Check if user account exists, hardcoded for testing purposes
    # Role ID for UserAdmin (1), PM (2), PIN (3), CSR Rep (4)
        accounts_db = database_management.getUser(email, password)
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
        
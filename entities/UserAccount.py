class UserAccount:
    def __init__(self, user_id, role_id, password, email, first_name, last_name, 
                 address, phone_no, is_active, created_at):
        self.user_id = user_id
        self.role_id = role_id
        self.password = password
        self.email = email
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
        accounts_db = {
            1:{
                "user_id": 1,
                "role_id": 1,
                "password": "password123",
                "email": "admin@volunteer.com",
                "first_name": "John",
                "last_name": "Cena",
                "address": "123 Apple St",
                "phone_no": "123456789",
                "is_active": True,
                "created_at": "2025-10-24"
            },
            2:{
                "user_id": 2,
                "role_id": 2,
                "password": "password123",
                "email": "pm@volunteer.com",
                "first_name": "Jack",
                "last_name": "Beanstock",
                "address": "456 Bean St",
                "phone_no": "987654312",
                "is_active": True,
                "created_at": "2025-10-23"
            },
            3:{
                "user_id": 3,
                "role_id": 3,
                "password": "password123",
                "email": "pin@volunteer.com",
                "first_name": "John",
                "last_name": "Cena",
                "address": "123 Apple St",
                "phone_no": "123456789",
                "is_active": True,
                "created_at": "2025-10-24"
            },
            4:{
                "user_id": 4,
                "role_id": 4,
                "password": "password123",
                "email": "csrrep@volunteer.com",
                "first_name": "John",
                "last_name": "Cena",
                "address": "123 Apple St",
                "phone_no": "123456789",
                "is_active": True,
                "created_at": "2025-10-24"
            }  
        }
        for key in accounts_db:
            current_row = accounts_db[key]
            if email == current_row["email"] and password == current_row["password"]:
                return UserAccount (
                    user_id = current_row["user_id"], # Here we will return from DB according to email and password
                    role_id = current_row["role_id"],
                    password = password,
                    email = email,
                    first_name = current_row["first_name"],
                    last_name = current_row["last_name"],
                    address = current_row["address"],
                    phone_no = current_row["phone_no"],
                    is_active = current_row["is_active"],
                    created_at = current_row["created_at"]
                )
        return None
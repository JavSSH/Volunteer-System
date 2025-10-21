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

    @classmethod
    def login(self, email, password):
        self.email = email
        self.password = password
        # Check if user account exists, hardcoded for testing purposes
        if self.email == "admin@volunteer.com" and self.password == "password123":
            return True
        else:
            return "Incorrect email or password!"
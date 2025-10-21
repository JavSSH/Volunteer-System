from entities.UserAccount import UserAccount

class UserLoginController:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def login(self, email, password):
        login_check = UserAccount.login(email, password)
        return login_check
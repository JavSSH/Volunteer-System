from entities.UserAccount import UserAccount

class UserLoginController:
    @staticmethod
    def login(email, password):
        return UserAccount.login(email, password)
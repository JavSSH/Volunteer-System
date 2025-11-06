from entities.UserAdmin import UserAdmin

class ViewUserAccController:
    def __init__(self):
        self.user_admin = UserAdmin()

    def viewUser(self, q=None):
        return self.user_admin.viewUser(q=q)
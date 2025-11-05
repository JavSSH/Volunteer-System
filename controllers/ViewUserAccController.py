from entities.UserAdmin import UserAdmin

class ViewUserAccController:
    def __init__(self):
        self.user_admin = UserAdmin()

    def viewUser(self):
        return self.user_admin.viewUser()
    
# class ViewUserAccController:
#     @staticmethod
#     def viewUser():
#         user_admin = UserAdmin()
#         return user_admin.viewUser()
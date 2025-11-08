from entities.UserAccount import UserAccount

class SearchUserAccController:
    @staticmethod
    def searchUser(search_term):
        user_account = UserAccount()
        return user_account.searchUser(search_term)
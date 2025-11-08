from entities.UserProfile import UserProfile    

class ViewProfileController:
    def viewProfile(self):
        user_profile = UserProfile()
        return user_profile.viewProfile()

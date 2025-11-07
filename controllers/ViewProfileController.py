from entities.UserProfile import UserProfile    

class ViewProfileController:
    def viewProfile(user_id):
        user_profile = UserProfile()
        return user_profile.viewProfile()
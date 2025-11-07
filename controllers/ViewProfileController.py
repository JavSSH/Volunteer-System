from entities.UserProfile import UserProfile    

class ViewProfileController:
    @staticmethod
    def getProfile(user_id):
        user_profile = UserProfile(
            profile_id=None,
            user_id=user_id,
            role_id=None,
            description=None,
            status=None,
        )
        return user_profile.getProfile(user_id)
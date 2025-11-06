from entities.UserProfile import UserProfile

class CreateProfileController:
    @staticmethod
    def createProfile(user_id, role_id, description, status):
        user_profile = UserProfile(
            profile_id=None,
            user_id=user_id,
            role_id=role_id,
            description=description,
            status=status,
        )
        return user_profile.createProfile(user_id, role_id, description, status)
    
    
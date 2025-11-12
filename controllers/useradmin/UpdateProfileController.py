from entities.UserProfile import UserProfile    

class UpdateProfileController:
    def __init__(self):
        pass
    
    def updateProfile(user_id, role_id, description, status):
        user_profile = UserProfile(
            user_id=user_id,
            role_id=role_id,
            description=description,
            status=status,
        )
        return user_profile.updateProfile(user_id, role_id, description, status)
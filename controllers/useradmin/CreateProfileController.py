from entities.UserProfile import UserProfile

class CreateProfileController:
    
    def __init__(self,user_id):
       self.user_id = user_id

    def createProfile(role_id, role_name, description, status):
        user_profile = UserProfile(
            
            role_id=role_id,
            role_name=role_name,
            description=description,
            status=status,
        )
        return user_profile.createProfile(role_id, role_name, description, status)
    
    
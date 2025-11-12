from entities.UserAccount import UserAccount   

class SuspendProfileController:
    def __init__(self):
        pass
    
    def suspendProfile(self, role_id):
        user_profile = UserProfile(
            user_id=user_id,
            role_id=None,
            email=None,
            password=None,
            first_name=None,
            last_name=None,
            address=None,
            phone_no=None,
            is_active=None,
            created_at=None
        )
        return user_account.suspendUser(user_id)
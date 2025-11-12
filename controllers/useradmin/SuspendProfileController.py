from entities.UserAccount import UserAccount   

class SuspendProfileController:
    def __init__(self):
        pass
    
    def suspendProfile(user_id, is_active):
        user_account = UserAccount(
            user_id=user_id,
            role_id=None,
            email=None,
            password=None,
            first_name=None,
            last_name=None,
            address=None,
            phone_no=None,
            is_active=is_active,
            created_at=None
        )
        return user_account.suspendUser(user_id, is_active)
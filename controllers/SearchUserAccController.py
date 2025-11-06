from entities.UserAccount import UserAccount

class UpdateUserAccController:
    @staticmethod
    def updateUser(user_id, email, password, role_id, first_name, last_name, address, phone, is_active):
        user_account = UserAccount(
            user_id=user_id,
            role_id=role_id,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            address=address,
            phone_no=phone,
            is_active=is_active,
            created_at=None
        )
        return user_account.updateUser(user_id, email, password, role_id, first_name, last_name, address, phone, is_active)
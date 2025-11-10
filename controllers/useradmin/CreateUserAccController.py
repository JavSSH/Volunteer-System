from entities.UserAccount import UserAccount

class CreateUserAccController:
    def createUser(email, password, role_id, first_name, last_name, address, phone):
        user_account = UserAccount(
            user_id=None,
            role_id=role_id,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            address=address,
            phone_no=phone,
            is_active=1,
            created_at=None
        )
        return user_account.createUser(email, password, role_id, first_name, last_name, address, phone)
from entities.UserProfile import UserProfile

class SearchProfileController:
    @staticmethod
    def searchProfile(keyword):
        user_profile = UserProfile(
            profile_id=None,
            user_id=None,
            role_id=None,
            description=None,
            status=None,
        )
        return user_profile.searchProfile(keyword)
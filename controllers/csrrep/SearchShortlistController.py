from entities.Request import Request

class SearchShortlistController:
    def __init__(self):
        pass
   
    def searchShortlist(self, user_id, keyword):
        request = Request()
        return request.searchShortlist(user_id, keyword)
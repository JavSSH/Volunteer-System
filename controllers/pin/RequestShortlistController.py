from entities.Request import Request

class RequestShortlistController:
    def __init__(self):
        pass
    
    def requestShortlist(self, user_id):
        request = Request()
        return request.requestShortlist(user_id)
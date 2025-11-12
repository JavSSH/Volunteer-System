from entities.Request import Request

class RequestShortlistController:
    def __init__(self):
        pass
    
    def requestShortlist(self, pin_user_id):
        request = Request()
        return request.requestShortlist(pin_user_id)
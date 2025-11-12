from entities.Request import Request

class ViewRequestController:
    def __init__(self):
        pass
    
    def viewRequests(self, user_id):
        request = Request()
        return request.viewRequests(user_id)

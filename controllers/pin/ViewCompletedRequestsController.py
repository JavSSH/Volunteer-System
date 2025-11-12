from entities.Request import Request

class ViewCompletedRequestsController:
    def __init__(self):
        pass
    
    def viewCompletedRequests(self, user_id):
        request = Request()
        return request.viewCompletedRequests(user_id)
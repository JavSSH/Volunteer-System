from entities.Request import Request

class RequestViewController:
    def __init__(self):
        pass
    
    def requestViews(self, user_id):
        request = Request()
        return request.requestViews(user_id)
    
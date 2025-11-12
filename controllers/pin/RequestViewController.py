from entities.Request import Request

class RequestViewController:
    def __init__(self,user_id):
        self.user_id = user_id
    
    def requestViews(self, user_id):
        request = Request()
        return request.requestViews(user_id)
    
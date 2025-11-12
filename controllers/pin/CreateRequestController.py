from entities.Request import Request

class CreateRequestController:
    def __init__(self,user_id):
        self.user_id = user_id
    
    def createRequest(self, user_id, category_id):
        request = Request()
        return request.createRequest(user_id, category_id)
from entities.Request import Request

class CreateRequestController:
    def __init__(self):
        pass
    
    def createRequest(self, pin_user_id, category_id):
        request = Request()
        return request.createRequest(pin_user_id, category_id)
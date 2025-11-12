from entities.Request import Request

class UpdateRequestController:
    def __init__(self):
        pass
    
    def updateRequest(self, category_id, request_id):
        request = Request()
        return request.updateRequest(category_id, request_id)
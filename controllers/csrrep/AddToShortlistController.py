from entities.Request import Request

class AddToShortlistController:
    def __init__(self):
        pass
   
    def addToShortlist(self, request_id,csrrep_user_id):
        request = Request()
        return request.addToShortlist(request_id,csrrep_user_id)
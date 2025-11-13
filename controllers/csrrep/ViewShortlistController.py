from entities.Request import Request

class ViewShortlistController:
    def __init__(self):
        pass
   
    def viewShortlist(self, csrrep_user_id):
        request = Request()
        return request.viewShortlist(csrrep_user_id)
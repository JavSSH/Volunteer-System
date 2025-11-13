from entities.Request import Request

class ViewRequestController:
    def __init__(self, pin_user_id):
        self.pin_user_id = pin_user_id

    def viewRequests(self, pin_user_id):
        request = Request()
        return request.viewRequests(pin_user_id)

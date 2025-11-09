from entities.Request import Request

class ViewRequestController:
    def viewRequests(self, pin_id):
        request = Request()
        return request.viewRequests(pin_id)

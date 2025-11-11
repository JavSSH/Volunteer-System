from entities.Request import Request

class ViewRequestController:
    def viewRequests(self):
        request = Request()
        return request.viewRequests()

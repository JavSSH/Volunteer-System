from entities.Request import Request

class UpdateRequestController:
    def updateRequest(self, request_id, request_detail):
        request = Request()
        return request.updateRequest(request_id, request_detail)
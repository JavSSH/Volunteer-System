from entities.Request import Request

class DeleteRequestController:
    def deleteRequest(self, request_id):
        request = Request()
        return request.deleteRequest(request_id)
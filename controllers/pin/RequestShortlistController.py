from entities.Request import Request

class RequestShortlistController:
    def requestShortlist(self, user_id):
        request = Request()
        return request.requestShortlist(user_id)
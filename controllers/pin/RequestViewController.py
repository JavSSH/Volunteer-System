from entities.Request import Request

class RequestViewController:
    def requestViews(self, user_id):
        request = Request()
        return request.requestViews(user_id)
    
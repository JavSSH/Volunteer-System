from entities.Request import Request

class RequestViewController:
    def requestViews(self, pin_id):
        request = Request()
        return request.requestViews(pin_id)
    
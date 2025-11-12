from entities.Request import Request

class SearchCompletedRequestsController:
    def __init__(self,user_id):
        self.user_id = user_id
    
    def searchCompletedRequests(self,user_id, keyword):
        request = Request()
        return request.searchCompletedRequests(user_id, keyword)
from entities.Request import Request

class FilterCompletedRequests:
    def filterCompletedRequests(self, user_id,request_date1,request_date2):
        request = Request()
        return request.filterCompletedRequests(user_id,request_date1,request_date2)
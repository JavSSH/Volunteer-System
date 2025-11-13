from entities.Request import Request

class SearchCompletedServicesController:
    def __init__(self):
        pass
   
    def searchCompletedServices(self, csrrep_user_id, category_id, request_date):
        opportunity = Request()
        return opportunity.SearchCompletedServices(csrrep_user_id, category_id, request_date)
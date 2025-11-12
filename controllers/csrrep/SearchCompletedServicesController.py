from entities.Opportunity import Opportunity

class SearchCompletedServicesController:
    def __init__(self):
        pass
   
    def searchCompletedServices(self, csrrep_user_id, category_id, request_date):
        opportunity = Opportunity()
        return opportunity.SearchCompletedServices(csrrep_user_id, category_id, request_date)
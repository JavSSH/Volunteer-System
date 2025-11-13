from entities.Opportunity import Opportunity

class SearchShortlistController:
    def __init__(self):
        pass
   
    def searchShortlist(self, csrrep_user_id, keyword):
        opportunity = Opportunity()
        return opportunity.SearchCompletedServices(csrrep_user_id, keyword)
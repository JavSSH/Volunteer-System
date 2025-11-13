from entities.Opportunity import Opportunity

class ViewShortlistController:
    def __init__(self):
        pass
   
    def viewShortlist(self, csrrep_user_id):
        opportunity = Opportunity()
        return opportunity.ViewShortlist(csrrep_user_id)
from entities.Opportunity import Opportunity 

class ViewOpportunitiesDetailsController:
    def __init__(self):
        pass
   
    def viewOpportunitiesDetails(self):
        opportunity = Opportunity()
        return opportunity.viewOpportunitiesDetails()
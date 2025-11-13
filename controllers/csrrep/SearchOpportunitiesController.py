from entities.Opportunity import Opportunity

class SearchOpportunitiesController:
    
    def __init__(self):
        pass

    def searchOpportunities(self, keyword):
        opportunity = Opportunity()
        return opportunity.searchOpportunities(keyword)
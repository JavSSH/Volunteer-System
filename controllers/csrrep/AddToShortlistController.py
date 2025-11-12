from entities.Opportunity import Opportunity

class AddToShortlistController:
    def __init__(self):
        pass
   
    def addToShortlist(self, request_id):
        opportunity = Opportunity()
        return opportunity.addToShortlist(request_id)
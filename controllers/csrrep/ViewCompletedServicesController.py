from entities.Opportunity import Opportunity

class viewCompletedServicesController:
    def __init__(self):
        pass
   
    def viewCompletedServices(self, csrrep_user_id):
        opportunity = Opportunity()
        return opportunity.ViewCompletedServices(csrrep_user_id)
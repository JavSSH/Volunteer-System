from entities.Opportunity import Opportunity

class ViewCompletedServicesController:
    def __init__(self):
        pass
   
    def viewCompletedServices(self, csrrep_user_id):
        opportunity = Opportunity()
        return opportunity.viewCompletedServices(csrrep_user_id)
from entities.CsrRep import CsrRep  

class ViewOpportunitiesDetailsController:
    def __init__(self):
        pass
   
    def viewOpportunitiesDetails(self):
        csr_rep = CsrRep()
        return csr_rep.viewOpportunitiesDetails(self)
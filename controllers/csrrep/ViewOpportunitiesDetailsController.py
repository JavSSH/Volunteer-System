from entities.CsrRep import CsrRep  

class ViewOpportunitiesDetailsController:
    @staticmethod
    def viewOpportunitiesDetails(self):
        csr_rep = CsrRep()
        return csr_rep.viewOpportunitiesDetails(self)
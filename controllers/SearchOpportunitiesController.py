from entities.CsrRep import CsrRep

class SearchOpportunitiesController:
    @staticmethod
    def searchOpportunities(keyword):
        csr_rep = CsrRep()
        return csr_rep.searchOpportunities(keyword)
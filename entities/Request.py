class Request:
    def __init__(self, request_id, pin_id, category_id, opportunity_id, request_status, request_date, request_view_count, request_shortlist_count):
        self.request_id = request_id
        self.pin_id = pin_id
        self.category_id = category_id
        self.opportunity_id = opportunity_id
        self.request_status = request_status
        self.request_date = request_date
        self.request_view_count = request_view_count
        self.request_shortlist_count = request_shortlist_count


    def requestViews(self, request_id):
        self.request_id = request_id
        if request_id:
            self.request_view_count = 100
        return self.request_view_count

    
    def requestShortlist(self, request_id, opportunity_id):
        self.request_id = request_id
        self.opportunity_id = opportunity_id
        if request_id and opportunity_id:
            self.request_shortlist_count = 10
        return self.request_shortlist_count
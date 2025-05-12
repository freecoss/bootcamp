import math
class Pagination():
    def __init__(self, items=None, page_size=10):
        if items != None:
            self.items = items
        else:
            self.items = []
        self.page_size = page_size
        self.current_idx = 0
        if self.items:
            self.total_pages = math.ceil(len(self.items) / self.page_size)
        else:
            self.total_pages = 0
    
    def get_visible_items(self):
        
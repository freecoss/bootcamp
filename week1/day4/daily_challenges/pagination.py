import math
class Pagination():
    def __init__(self, items=None, page_size=10):
        if items != None:
            self.items = items
        else:
            self.items = []
        self.page_size = page_size
        self.current_idx = 0
        self.total_pages = math.ceil(len(self.items) / self.page_size) if self.items else 0

    
    def get_visible_items(self):
        start = self.current_idx*self.page_size
        end = start+self.page_size
        items_current_page = self.items[start:end]
        return items_current_page
    
    def go_to_page(self, page_num):
        if page_num < 1 or page_num > self.total_pages:
            raise ValueError("Invalid page number")
        self.current_idx = page_num - 1
        return self
        
    def first_page(self):
        self.current_idx = 0
        return self
    def last_page(self):
        if self.total_pages>0:
            self.current_idx = self.total_pages-1
        else:
            self.current_idx=0
        return self
    def next_page(self):
        if self.current_idx<self.total_pages-1:
            self.current_idx+=1
        return self
    def previous_page(self):
        if self.current_idx>0:
            self.current_idx-=1
        return self
    
    def __str__(self):
        return "\n".join(str(item) for item in self.get_visible_items())


#test code :
alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)

print(p.get_visible_items())
# ['a', 'b', 'c', 'd']

p.next_page()
print(p.get_visible_items())
# ['e', 'f', 'g', 'h']

p.last_page()
print(p.get_visible_items())
# ['y', 'z']

p.go_to_page(10)
print(p.current_idx + 1)
# Output: 7

p.go_to_page(0)
# Raises ValueError        
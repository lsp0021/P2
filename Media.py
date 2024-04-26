
class Media():

    def __init__(self, id, title, average_rate):
        self._id = id
        self._title = title
        self._average_rate = average_rate
    
    def get_id(self):
        return self._id
    
    def get_title(self):
        return self._title
    
    def set_title(self, title):
        self._title = title

    def get_average_rate(self):
        return self._average_rate
    
    def set_average_rate(self, average_rate):
        self._average_rate = average_rate
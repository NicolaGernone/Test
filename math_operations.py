class Math_operations:
    def __init__(self, list_f, column):
        # init the list and columns
        self.list = list_f 
        self.column = column
    
    """
    Average calculator
    """      
    def avg(self):
        return sum(self.list)/len(self.list)
    
    """
    Max calculator
    """ 
    def max(self):
        max_num = self.list[0] # init the firs value
        for number in self.list:
            if number > max_num:
                max_num = number
        return max_num
    
    """
    Min calculator
    """ 
    def min(self):
        min_val = self.list[0] # init the firs value
        for val in self.list:
            if val < min_val:
                min_val = val
        return min_val
    
    """
    Set the str method to return a string as a class method report
    Return a string chain twith the calculated values of a given column
    """ 
    def __str__(self):
        chain = "{}: Max. {}, Min. {}, Avg. {}".format(self.column, self.max(), self.min(), self.avg())
        return chain
            
    
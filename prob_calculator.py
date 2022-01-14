import copy
import random

class Hat:
    #! draw method, contents instance variable that's a list of strings   
    def __init__(self, contents=None, **kwargs):
        if contents is None:
           contents = []
        self.contents = contents
        self.__dict__.update(kwargs)
        for key, value in kwargs.items():
            for i in range(int(kwargs.get(key))):
                self.contents.append(key)
        
        self.copy = self.contents[:]
        
    def draw(self, number_of_balls):
        balls_drawed = []
        self.contents = self.copy[:]
        
        if number_of_balls >= len(self.contents):
            balls_drawed = self.contents[:]
        else:
            for j in range(number_of_balls):
                balls_drawed.append(self.contents.pop(random.randrange(len(self.contents))))
            
        return balls_drawed
    
    def recompose(self):
        self.contents = self.copy[:]  
        
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    M = 0
    expect = [1]*len(expected_balls)

    for N in range(num_experiments):

        count = []        
        
        balls_drawn_dict = dict()
        
        for item in hat.draw(num_balls_drawn):
            balls_drawn_dict[item] = balls_drawn_dict.get(item, 0) + 1
            
        for key,value in expected_balls.items():
            if balls_drawn_dict.get(key) != None and balls_drawn_dict.get(key) >= value:
                count.append(1)
            else:
                count.append(0)
                
        if count == expect:
            M += 1
                
        hat.recompose()
    
    probability = M/num_experiments
        
    return probability
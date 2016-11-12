#the greedy algorithms for the knapsack problem
#class food
class Food(object):
    def __init__(self,n,v,w):
        self.name=n
        self.value=v
        self.calories=w
    def getValue(self):
        return self.value
    def getCost(self):
        return self.calories
    def density(self):
        return self.getValue()/self.getCost()
    def __str__(self):
        return self.name+"/"+self.value+'/'+self.calories

#build menu of foods
def builMenu(names,values,calories):
    '''names, values, calories lists of same length.
        name a list of strings
        returns list of foods'''
    menu=[]
    for i in range(len(values)):
        menu.append(Food(names[i],values[i],calories[i]))
    return menu

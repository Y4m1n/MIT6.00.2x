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
        return str(self.name)+"/"+str(self.value)+'/'+str(self.calories)

#build menu of foods
def buildMenu(names,values,calories):
    '''names, values, calories lists of same length.
        name a list of strings
        returns list of foods'''
    menu=[]
    for i in range(len(values)):
        menu.append(Food(names[i],values[i],calories[i]))
    return menu

#flexible greedy:use key function to define what does best mean
def greedy(items,maxCost,keyFunction):
    '''assumes items a list, maxCost>=0,
        keyFunction maps elements of items to numbers'''
    itemsCopy=sorted(items,key=keyFunction,
                     reverse=True)
    result=[]
    totalValue,totalCost=0.0,0.0

    for i in range(len(itemsCopy)):
        if (totalCost+itemsCopy[i].getCost())<=maxCost:
            result.append(itemsCopy[i])
            totalCost+=itemsCopy[i].getCost()
            totalValue+=itemsCopy[i].getValue()

    return (result,totalValue)

#test greedy
def testGreedy(items,constraint,keyFunction):
    taken,val=greedy(items,constraint,keyFunction)
    print('Total value of items taken:',val)
    for item in taken:
        print('',item)

def testGreedys(foods, maxUnits):
    print('Use greedy by value to allocate', maxUnits,
          'calories')
    testGreedy(foods, maxUnits, Food.getValue)
    print('\nUse greedy by cost to allocate', maxUnits,
          'calories')
    testGreedy(foods, maxUnits,
               lambda x: 1/Food.getCost(x))
    print('\nUse greedy by density to allocate', maxUnits,
          'calories')
    testGreedy(foods, maxUnits, Food.density)


names = ['wine', 'beer', 'pizza', 'burger', 'fries',
         'cola', 'apple', 'donut', 'cake']
values = [89,90,95,100,90,79,50,10]
calories = [123,154,258,354,365,150,95,195]
foods = buildMenu(names, values, calories)
testGreedys(foods, 1000)



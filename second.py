list= [1,-2,3,4]
cont = 0
def findValueMax(list):
    for key in list:
        if key > cont:
            max = key
    return max
def findValueMin(list):
    for key in list:
        if key < cont:
            min = key 
    return min
print(findValueMax(list))
print(findValueMin(list))
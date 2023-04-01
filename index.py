list = [1,2,4]

def findAvergae(list):
    summation = 0
    cont = 0
    for key in list:
        summation += key
        cont +=1
    return int(summation / cont)
print(findAvergae(list))
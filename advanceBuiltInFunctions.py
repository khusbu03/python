# Advance built in functions
def filterEven(*args):
    newList=[]
    for i in args:
        if(i%2==0):
            newList.append(i)
    return newList        



numbers=[1,2,3,4,5,6,7,7,8,9,9,10]

evenNumbers= filterEven(*numbers)
print("even Numbers",evenNumbers)


# MAP function 

mapFunction=list(map(lambda number : number*2,numbers))
print(mapFunction)


# Filter function
filterFunction=list(filter(lambda number: number%2!=0,numbers))
print(filterFunction)


from functools import reduce

nums = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, nums)
print("reduce in python",product)

names = ["Alice", "Bob"]
scores = [85, 90]
combined = list(zip(names, scores))
print(combined)

fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(index, fruit)


names=["apple","pineApple","orange"]   

newNames.append("")
for index,fruit in enumerate(names):
    print(index,fruit)

print(any(names))
print(names)    
print(newNames)    
print(all(names))

print(all(names))
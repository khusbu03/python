# lambda functionsare used to define a function in a single line

# variable=lambda parameters:expression

sum=lambda a,b: a+b
print(sum(2,3))

square=lambda a : a**2

print(square(4))

numbers=[1,2,3,4,5,6,7,8,9,10]

even=list(filter(lambda num :num%2==0,numbers))
odd=list(filter(lambda num:num%2!=0,numbers))

elementsMap=list(map(lambda num :num*2,numbers))

print(even)
print(odd)
print(elementsMap)


names=["khushi","khusbu","Khushbu Phulara","a"]
print(max(names,key=lambda item:len(item)))



students2=[
    {'name':"rohit","age":32,"score":100},
    {'name':"mohit","age":24,"score":90},
    {'name':"ankit","age":35,"score":95},
]


print(max(students2,key=lambda item :item.get('score'))['name'])
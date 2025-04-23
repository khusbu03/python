# Generator Comprehension

# the only dffernce between  thelist comprehension and the generator comprehnesion is that in case of list we were using the square bracket and in this  we are using the parenthesis

square=(i**2 for i in range(10))
print(square)

print(next(square))

print("printing sqaure iterator first time")
for i in square:
    print(i)

print("printing sqaure iterator again")
for i in square:
    print(i)   
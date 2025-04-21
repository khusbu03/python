# dictionary Comprehension

squares={num:num**2 for num in range(0,6)}
print("Squares of numbers ",squares)


squares={f"square of {num} is":num**2 for num in range(0,4)}
print("Squares of numbers ",squares)


for key,value in squares.items():
    print(f"{key} :{ value}")


demoString="i am learning python for doing backend,then i will learn django"
countAlphabets={char:demoString.count(char) for char in demoString}

print("Alphabets  count",countAlphabets)
odd_even={i:('even' if (i%2==0) else 'odd') for i in range(0,11)}
print("odd even dictionary",odd_even)


# set comprehension
newSet={i**2  for i in range(0,11)}
print(newSet)
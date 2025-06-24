greeting = "Good Morning"
a = 5
#if greeting == "Morning":
if a > 2:
    print("condition matches")
    print("second line")
else:
    print("condition do not match")

print("if else condition code is completed")

# for loop

obj = [2, 3, 5, 6, 7]
for i in obj:
    print("Value of", i)
    print(i*2)

# sum of first natural number
Summation = 0
for j in range(1,6): #range
    Summation = Summation + j
print(Summation)

# While loop

it = 5
while it>1:
    if it != 3: #want to remove
        print(it)
    it = it - 1

print("while loop simple")

New = 10
while New>1:
    if New == 9:
        New = New - 1
        continue
    if New == 3: #want to break
        break
    print(New)

    New = New - 1

print("while loop execution is done with break")

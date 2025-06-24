from encodings.punycode import insertion_sort

values = [1, 2, "aditi z", 4, 5]
# List is data type that allows multiple values and can be different data type

print(values[0]) #1
print(values[3]) #4
print(values[-1]) #5

print(values[1:3]) #2, rahul
values.insert(3, "zod")
print(values)

alphas = ["aditi", "zod", "is a QA"]
print(alphas[0:3])

values.append("you") #add new value in list
print(values)

values[2] = "ADITI" #value update in list
print(values)

del values[1] #value delete from the list
print(values)

#Tuple - same as list data type but immutable

val = (1, 2, "aditi", 4.5)
print(val[1])

#val[2] = "ADITI" - tuple is not support the assignment

#dictionaries - key value pair form and comes in curly braces and written in key:value

dic = { "a":2, 4:"abc", "c":"Adi"}
print(dic[4])
print(dic["c"])

#how to create dictionary
dict ={}

dict["Firstname"] = "Aditi"
dict["lastname"] = "Zod"
dict["Gender"] = "Female"
dict["designation"] ="QA"

print(dict)

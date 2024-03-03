# salute  = input("salutations:")
# name = input("Yout name:");
# print("hello "+salute +" " + name)

def addNum(first, second):
 total = first + second
 return (total)

first = int(input("Input first number:"))
second = int(input("Input second number"))


print("The total sum is equals to " + str(addNum(first,second)))

#tuple
def get_coordinates():
    x = 10
    y = 20
    return x, y

coordinates = get_coordinates()
print(coordinates)  # Output: (10, 20)

# In this section it returns x and y, unlike javascript it only a single value, but in python if you return a multiple value it will result to returning a tuple which is a paranthesis containing values


my_tuple = (1, 2, 3)
my_list = list(my_tuple)
print(my_list)  # Output: [1, 2, 3]

print(my_tuple)

#list are more similar to tuple
# list is mutable meaning it can be change



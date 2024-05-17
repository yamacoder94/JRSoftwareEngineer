#here comes the function!
# just like methods

def hello_word():
    print("tu may")

hello_word()

def greeting(name):
    print("Hi " + name + "!")

greeting("Yamill")

def add(num1 , num2):
    return num1 + num2

num_sum = add(12,15)
print(num_sum)


def mul(num1,num2):
    return num1 * num2

print(mul(add(1,2),add(20,4)))
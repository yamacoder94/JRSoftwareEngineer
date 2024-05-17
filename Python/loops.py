##for loops 

list1 = ['apples', 'bananas', 'cherries']
tup1 = (2,6,10)

for item in list1:
    print(item)

for item in tup1:
    print(item)

    # Python for loop example
    #for i in range(0,11,2): 
    #that way it prints only the even numbers between 0,11
for i in range(0,11,2):
    print("Current index:", i)

for i in range(5,51,5):
    print("Current index:", i)
##this way we only printed the numbers diveded by 5 between 5-51

##nesting for loops
for i in range(0,5):
    for j in range(0,3):
        print(i*j)


#while loops
c = 0
while c  < 5:
    c = c +1 
    if c == 3:
        break
    print('here is the while',c)

##   break comes handy when we want the while to break
## we can use continue and pass 
## contine skips the current interation and movres to the next one 
# pass placeholder that allows to structure the code wit implement it


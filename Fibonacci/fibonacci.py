a,b = 0,1

#  first 10 fibonacci numbers
while a < 10:
    print(a, end=' ')
    a,b = b, a+b

# The first line contains a multiple assignment: the variables a and b simultaneously get the new values 0 and 1. 
# On the last line this is used again, demonstrating that the expressions on the right-hand side are all evaluated 
# first before any of the assignments take place. The right-hand side expressions are evaluated from the left to the right.
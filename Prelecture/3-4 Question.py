# Let  a1  a positive integer. Consider a series:
#a^n+1={a^n/2 if an is even,3a^n + 1 if an is odd. 
# The Collatz conjecture tells for every positive integer  a1 , this series at some 
# points comes to  1 , but it is unsolved till now (an computer experiment showed 
# that the proposition is true for all integers less than as large as  2^68 ). Write 
# a program that, with an given integer input, returns the minimal number of the 
# steps one has to take until the series gets to  1 . Try  a1=7  and  a1=31  to 
# see how many steps to converge (these steps may take more than you would expect).

# in short, the program should return the number of steps it takes to reach 
# 1 from a given positive integer using the Collatz sequence rules.
# collatz sequence: if n is even, divide it by 2; if n is odd, 
# multiply it by 3 and add 1. Repeat this process until you reach 1.
a = int(input("Enter a positive integer: "))
n = 0
for i in range(1000):
    if a == 1:
        break

    if a % 2 == 0:
        a = a // 2
    else:
        a = 3 * a + 1
    n = n + 1
print(n)
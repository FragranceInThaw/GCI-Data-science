# (3-1) Let's assume a variable x contains an integer score from 0 to 100. 
# Write a program using the if statement that prints "pass" if x is 60 or above,
#  and "fail" otherwise.

 # Example score
x = int(input("Enter your score (0-100): "))
print(f"Score: {x}")
if x >= 60:
    print("pass")
else:
    print("fail")
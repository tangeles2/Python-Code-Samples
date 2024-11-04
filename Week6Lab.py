# Tony Angeles
# 11/03/24

# Problem 1
import random
for _ in range(10):
    print(random.randrange(25,35))

# Problem 2
import random
rand_num = random.randrange(0,100)
odd_num = rand_num * 2 + 1
print(odd_num)

# Problem 3
import random
options = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
random_choice = random.choice(options)
print("Random choice is:", random_choice)

# Problem 4
def calculate_pi(n_terms):
    pi = 0
    sign = 1
    for i in range(1 , n_terms * 2, 2):
        pi += sign * 4 / i
        sign *= -1
    return pi
pi_approx = calculate_pi(100000)
print(pi_approx)
import math
print(math.pi)

# Problem 5
import math
radians= 3.14159
degrees = math.degrees(radians)
print(degrees)

# Problem 6
import math
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0:
        return 1
    else:
        return math.factorial(n)
num = int(input("Input a number to compute the factorial: "))
result = factorial(num)
print(f"The factorial of {num} is {result}")

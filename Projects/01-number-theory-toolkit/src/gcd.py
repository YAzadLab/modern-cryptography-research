import time 

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

def gcd_brute_force(a, b):
    highest = 1

    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            highest = i

    return highest

num1 = int(input('What would you like your a value to be in GCD(a, b): '))
num2 = int(input('What would you like your b value to be in GCD(a, b): '))

print("Choose an algorithm:")
print("1. Euclidean Algorithm")
print("2. Brute Force")

choice = input("Enter 1 or 2: ")

if choice == "1":
    start = time.perf_counter()

    result = gcd(num1, num2)

    end = time.perf_counter()

    print(f'The GCD of {num1} and {num2} is {result}')
    print(f'Time taken: {end - start} seconds')

elif choice == "2":
    start = time.perf_counter()

    result = gcd_brute_force(num1, num2)

    end = time.perf_counter()

    print(f'The GCD of {num1} and {num2} is {result}')
    print(f'Time taken: {end - start} seconds')

else:
    print("Invalid choice")
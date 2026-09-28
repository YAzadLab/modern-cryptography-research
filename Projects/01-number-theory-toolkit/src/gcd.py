def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

num1 = int(input('What would you like your a value to be in GCD(a, b): '))
num2 = int(input('What would you like your b value to be in GCD(a, b): '))

print(f'The GCD of {num1} and {num2} is {gcd(num1, num2)}')
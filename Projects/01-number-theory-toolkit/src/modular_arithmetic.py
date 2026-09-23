def calculation(a, b):
    return a//b


choice = int(input('which modulo would you like to use:\n 1. a mod(b)\n 2. a*b mod(c)\n 3. a^b mod(c)\n Enter 1, 2 or 3: '))
if choice == 1:
    num1 = int(input("Enter your a value from a mod(b): "))
    num2 = int(input('Enter your b value from a mod(b): '))
    quotient = calculation(num1, num2)
    output = num1 - quotient*num2

    print(f'{num1} mod {num2} = {output}')
elif choice == 2:
    first_num = int(input('Enter the first number: '))
    second_num = int(input('Enter the number you want to multiply with the first number: '))
    product = first_num * second_num
    print(f'Your a value is now {product}')

    num2 = int(input('Enter your b value from a mod(b): '))
    quotient = calculation(product, num2)
    output = product - quotient*num2

    print(f'{product} mod {num2} = {output}')

#First i need to get the power number 
#Then i need to split the power number into unique powers of 2
#Then i need to solve each power of 2 as a mod on its own
#Then i need to multiply the numbers i get
#Then i need to solve that final one to get the desired result

elif choice == 3:
    #num1 = int(input("Enter your a value from a^b mod(c): "))
    #num2 = int(input('Enter your b value from a^b mod(c): '))
    #power = num1 ** num2
    #num3 = int(input('Enter your c value for a^b mod(c): '))

    #quotient = calculation(power, num3)
    #output = power - quotient*num3

    #print(f'{power} mod {num3} = {output}')

    num1 = int(input("Enter your a value from a^b mod(c): "))
    num2 = int(input('Enter your b value from a^b mod(c): '))
    num3 = int(input('Enter your c value for a^b mod(c): '))

    powers = []
    power = 1
    remaining = num2

    # Split b into powers of 2
    while power <= remaining:
        power *= 2

    power //= 2

    while power > 0:
        if remaining >= power:
            powers.append(power)
            remaining -= power
        power //= 2

    print(f'powers of 2 used: {powers}')

    # Calculate a^1 mod(c)
    quotient = calculation(num1, num3)
    current = num1 - quotient * num3

    # Work out a^2, a^4, a^8, etc. by repeatedly squaring
    results = []

    current_power = 1

    for target_power in reversed(powers):
        while current_power < target_power:
            product = current * current
            quotient = calculation(product, num3)
            current = product - quotient * num3
            current_power *= 2
        results.append(current)
    print(f'Results for required powers: {results}')

    # Multiply the required results together
    answer = 1

    for result in results:
        product = answer * result
        quotient = calculation(product, num3)
        answer = product - quotient * num3

    print(f'{num1}^{num2} mod {num3} = {answer}')

    


    




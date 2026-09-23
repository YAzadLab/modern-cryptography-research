Question 1:
23 mod(7)

use the formula n = qm + R
n = original number in this case 23
m = the mod number in this case 7 
q = the number you get by dividing 23 and 7 without the remainder in this case 23/7 = 3R2 and use 3
R = the remainder

(23) = (3)(7) + 2
hence: 23 mod(7) = 2

Question 2: 
50 mod(9)

50/9 = 5R5
n = qm + r
50 = (5)(9) + 5
50 mod(9) = 5

Question 3:
123 mod(10)

123/10 = 12R3
n = qm + r
123 = (12)(10) + 3
123 mod(10) = 3

Question 4: 
(7+8) mod(5)
15 mod(5)
15/5 = 3R0
so (7+8)mod(5) = 0

Question 5:
(7*8) mod(5)
56 mod(5)
56/5 = 11R1
56 mod(5) = 1

Question 6:
3^5 mod(7)

To solve questions including exponentials we need something called modular exponentiation. 
By using this one of the methods you can use to solve this quesion and other similar questions using
the following steps:

for something like a^b (mod(m)):
    step 1 - Reduce a mod(b)
    step 2 - Break the exponent b into powers of 2
    step 3 - Repeatedly square
    step 4 - Reduce modulo m after every calculation
    step 5 - Multiply the required powers together

We will use this method on the question above

3^5 mod(7)

This is already reduced enough there is no need for step 1

Now break b, in this case 5, into powers of 2:
    5 = 4 + 1

Now we need to calculate:
    3^4mod(7) to get 4
    3^1mod(7) to get 3
    
Now we need to multiply 4 x 3 to get 12mod(7) 

then finally work out the last equation 12od(7) to get 5

Is it more efficient to calculate the entire number first and then take the remainder, or can w take the 
remainders during the calculation?


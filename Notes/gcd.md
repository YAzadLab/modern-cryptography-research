## Experiment

I implemented two different algorithms for calculating the GCD: the Euclidean algorithm and a brute-force algorithm that checks possible divisors of both numbers.

I then used Python's timing functions to measure how long each algorithm took to calculate the GCD. The purpose of this experiment was to see whether two algorithms that produce the same answer can have different computational costs.

### Results

| Input A | Input B | Euclidean Algorithm Time  | Brute-Force Time     |
|---------|---------|---------------------------|----------------------|
| 650000  | 789000  |1.97919999998e-05 sec      |0.0383536669999991 sec|
| 999999  | 888888  |4.97919999986e-05 sec      |0.0502475840000009 sec|
| 777654  | 999786  |8.95799999867e-06 sec      |0.0378452500000001 sec|

I tested increasingly large input values to see how the performance of each algorithm changed.

### Analysis

Both algorithms calculate the same mathematical result, but they approach the problem differently.

The brute-force algorithm checks possible divisors to determine the largest number that divides both inputs. As the input values become larger, the number of possible divisors that may need to be checked also increases.

The Euclidean algorithm instead repeatedly reduces the problem using division and remainders. To calculate `gcd(a, b)`, it continues with `gcd(b, a mod b)` until the remainder becomes 0. This allows it to reduce large inputs quickly rather than checking every possible divisor.

By comparing the execution times, I can investigate the difference in efficiency between the two approaches and see how this difference changes as the input size increases.

## What I learned

This experiment showed me that finding the correct solution to a mathematical problem is not the only important consideration when designing an algorithm. Two algorithms can produce exactly the same answer while requiring very different amounts of computation.

I also learned that the GCD can determine whether two integers are coprime. If `gcd(a, b) = 1`, then the two numbers share no positive divisor other than 1. This is relevant to cryptography because coprimality is important when working with modular inverses and algorithms such as RSA.

Comparing the two GCD algorithms also introduced an important idea for the rest of my research: the difficulty of a mathematical problem depends not only on whether it can be solved, but also on how efficiently it can be solved as the size of the input increases.

Here is the link to my code:
[GCD algorithm](../Projects/01-number-theory-toolkit/src/gcd.py)
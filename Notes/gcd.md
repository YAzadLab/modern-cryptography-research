# Greatest Common Divisor (GCD)

## What is the GCD?

The greatest common divisor of two integers is the largest positive integer
that divides both numbers exactly.

For example:

gcd(48, 18) = 6

because 6 is the largest number that divides both 48 and 18.

## Why is it relevant to cryptography?

The GCD is important in cryptography because it can be used to determine
whether two numbers are coprime.

Two numbers are coprime if their GCD is 1.

## Euclidean Algorithm

The Euclidean algorithm finds the GCD efficiently using repeated division:

48 = 18 × 2 + 12
18 = 12 × 1 + 6
12 = 6 × 2 + 0

Therefore:

gcd(48, 18) = 6

The algorithm stops when the remainder becomes 0.

## My Implementation

[describe or link to gcd.py]

## Experiment

I compared finding the GCD by checking possible divisors with the Euclidean
algorithm.

## What I learned

[Write your own observations here.]

## Questions for Further Research

- Why does the Euclidean algorithm work?
- How much faster is it than checking every possible divisor?
- How does GCD relate to modular inverses?
- Why is being coprime important in RSA?
# CMPS 2200 Assignment 3
## Answers

**Name:** Michael Baron
https://github.com/allan-tulane/sp25-assignment-03-michaelbaron1


Place all written answers from `assignment-03.md` here for easier grading.
## Part 1: Making Change
1a. 
Given $N dollars, to get as few coins as possible using a greedy algorithm you should start with getting the floor 
of log_2 N. this would equal k, so k = log_2 N // 1. this would result in the highest possible coin of denomination 2^k 
that could fit for N$. From there, you would subtract 2^k from N to get new end until basecase of k = 0 and the coins perfectly fit

1b.
This is optimal because 2^(log_2 N // 1) will always be the largest coin of denominiation 2^k that can fits into remaining N dollars.
this will continiously be done until base case of k = 0. We know that 2^k at its largest form is always optimal, and doesnt
run into value/weight organization problem becasue if we were to use a smaller number k, like 2^k-1 instead,
then it would take another coin, 2^k-1, to equal same value as 2^k, making it less efficient

1c. 
the work and span of this is O(logn) becasue N is reduced by a factor of 2 when each coin is added. 

## Part 2: Making Change Again
2a. 
an example of using a greedy algorithm in this scenario, taking the largest coin denomination <= N, that does not work
would be if N = 8, with coin options = [5, 4, 1]. Here, the Greedy Alg would take coin 5, then be forced to takes 3 coins
of value 1, leaving a total coin amount of 4. However, optimally, the algorithm would take 2 coins of size 4. 

2b. ** Since you paid attention in Algorithms class, you realize that
  while this problem does not have the greedy choice property it does
  have an optimal substructure property. State and prove this
  property.
Using memoization, this problem can have an optimal substructure property. to do this, it would essentially take $N
and create 2 possible scenarios, either taking the largest denomination coin < N$ or not, in which case it would create the
same subproblem of taking the next largest coin D < N$ or not, and repeating the process. the key here is for the alg to save time by remembering all combos
this will result in one of the subproblems being the most efficient.

2c.
Essentially, if the optimal solution for amount of coins is F(N), then the work could be expressed as
F(N) = 1 + F(N-d) where d is a coin of the optimal solution. this would recursivly solve since F(N-d) would also
be the optimal solution for the subproblem. this means as N increases, the work would increase by some C * N
making the work o(n) and the span o(n) as the longest tree would also increase with N increasing for any given currency set


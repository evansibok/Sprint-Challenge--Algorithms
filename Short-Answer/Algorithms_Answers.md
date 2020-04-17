#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) O(n) - While we have assigned a value (constant) to `a` and increment it we still have a body of code that iterates the expression `n` number of times and since we don't put constants into considerations, we have a worst case scenario of `O(n)`.

b) O(n^2) - We've got two loops in this code which runs a total of `n * n` times. This means our worst case scenario is automatically `O(n^2)`.

c) O(n) - Being a recursive function the time taken to execute the function call is `n` and given the amount of operations in the call as 3 `=, +, and -` all being term as constant operations, it's agreeable that we have a worst case scenario of `O(n)`.

## Exercise II

[]: # n-story building with infinity eggs
[]: # eggs thrown from floors >= f gets broken
[]: # eggs thrown from floors < f don't get broken
[]: # how can you determine value of f such that the number of dropped + broken eggs is minimized?

#### Answer

- Assuming the eggs are currently of floor f, the likeliness of the eggs to drop and get broken is high
- The only way to minimize the number of dropped + broken eggs is to get to the floor below f

-- Given a number `n` of floors - `defined number of floors is a constant (1)`
-- Count the floors and for every floor we get to, if we are on floors that are below floor `f`, we are allowed to carry eggs
-- If we get to floor `f` or any floor greater than floor `f` we will `not` be allowed to carry eggs. - `Having an ability to count the count the floors (n) times`
-- To move to floors greater than or equals to `f` you must drop the eggs on any of the previous floors lower than `f`.
-- This is significantly control how the eggs are carried and prevent eggs being broken when dropped

`n` constant number of floors = 1
`count` floors `n` number of times = n
base condition where eggs can be carried and dropped

The runtime complexity looks likely to be `O(n)`.

# 4\) Fibonacci Sequence in D.P.

## Implementation example: Fibonacci Sequence in Dynamic Programming

```python
def fibonacciDP(n):
    # Setting up memoization table
    dicFibo = {}
    dicFibo[0] = 0
    dicFibo[1] = 1
    
    # Building up a bigger solutions
    for i in range(2, n + 1):
        dicFibo[i] = dicFibo[i - 1] + dicFibo[i - 2]
    return dicFibo[n]
    
# Execution Part
for i in range(0, 10):
    print(fibonacciDP(i), end=' ')
```

![](.gitbook/assets/image%20%287%29.png)

![](.gitbook/assets/image%20%282%29.png)

* Use a dictionary collection variable type for momoization 
* Memoization
  * Storing a fibonacci number for a particular index
* Now,
  * We have a new space requirement, the dictionary or the table, **O\(N\)**
    * Because table can have at most N lists
  * We have reduced execution time from O\(2ⁿ\) to O\(N\)


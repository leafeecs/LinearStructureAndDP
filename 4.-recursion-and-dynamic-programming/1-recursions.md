# 1\) Recursions

## Concepts of Recursions

* Repeating Problems
* **Divide and Conquer**
* Recursion Function Call
* Recursion Escape
* Recursion Depth

## Repeating Problems and Divide and Conquer

![Repeating Problem](../.gitbook/assets/2019-12-20-12.07.51.png)

* Company A 는 Sales Dept., Manufacturing Dept., R&D Dept. 로 나누어져 있다.
* Company A 안의 Sales Dept. 안에는 또 Seoul, Busan, Deajeon Sales Branch 로 나누어져 있다. Manufacturing Dept. 역시 . . . 로 나누어져 있다. R&D 역시 . . . 로 나누어져 있을 것이다.
* 즉, Sales Dept. 는 결국 같은 형식의 작은 버전의 Company A 구조라 할 수 있다. 이렇게 계속되는 작은 Repeating Problem 을 통해 점점 더 큰 문제를 해결하는 방법을 **Divide and Conquer** 이라 한다.

```python
class Department
    dept = [sales, manufacturing, rnd]
    
    def calculateBudget(self):
        sum = 0
        for i in range(len(dept)):
            sum += dept[i].calculateBudget()
        return sum
```

## More Examples 

### 1. Factorial

```python
def factorial(n):
    if n == 0:
        return 1
    elif n > 0:
        return n * (n - 1) * (n - 2) * . . . * 1
```

We can change return expression as below

```python
def factorial(n):
    # Base Case, i.e. Termination Term
    if n == 0:
        return 1
    elif n > 0:
        return n * factorial(n - 1)
```




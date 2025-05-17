def fibonacci_series(n):
    
    if n <= 0:
        return []
    
    elif n == 1:
        return [0]  
    elif n == 2:
        return [0, 1]
    else:
        series = fibonacci_series(n - 1) 
        series.append(series[-1] + series[-2])
        return series


n = 10
print(f"Fibonacci series up to position {n}: {fibonacci_series(n)}")

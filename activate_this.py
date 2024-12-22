result = []

def divider(a, b):
    if a < b:
        raise ValueError("a is smaller than b")
    if b > 100:
        raise IndexError("b is greater than 100")
    if b == 0:
        raise ZeroDivisionError("b cannot be zero")
    return a / b


data = {10: 2, 2: 5, 123: 4, 18: 0, 8: 4}

for key in data:
    try:
        res = divider(key, data[key])
        result.append(res)
    except (ValueError, IndexError, ZeroDivisionError) as e:
        print(f"Error for key {key}: {e}")  

print("Результати:", result)

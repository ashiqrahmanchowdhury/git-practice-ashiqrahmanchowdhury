from datetime import date
from utils import add, subtract, multiply, safe_divide

print("Ashiq Ramhan Chowdhury")
print("Today's date:", date.today())

# Calculator demo
print("5 + 3 =", add(5, 3))
print("5 - 3 =", subtract(5, 3))
print("5 * 3 =", multiply(5, 3))
print("5 / 0 =", safe_divide(5, 0))
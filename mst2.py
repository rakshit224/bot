def factorial(n):
  """Calculates the factorial of a non-negative integer."""
  # Base Case:
  if n == 0:
    return 1
  # Recursive Case:
  else:
    return n * factorial(n-1)
num = 0
print(f"The factorial of {num} is {factorial(num)}")
# The output of the above code will be:

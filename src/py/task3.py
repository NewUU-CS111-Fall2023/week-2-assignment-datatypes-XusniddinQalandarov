# * Author: Xusniddin Qalandarov
# * Date: 25/10/2023
import random

def generate_100_digit_number():
  """Generates a random 100-digit number."""
  number = ""
  for i in range(100):
    number += str(random.randint(0, 9))
  return number

def divide_by_a(number, a):
  """Divides the given number by A and returns the result."""
  result = int(number) / a
  return result

def main():
  a = int(input("Enter a number A: "))
  number = generate_100_digit_number()
  result = divide_by_a(number, a)
  print(f"The result of dividing {number} by {a} is {result:.100f}.")

if __name__ == "__main__":
  main()

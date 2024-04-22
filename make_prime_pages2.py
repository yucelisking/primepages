import streamlit as st

st.header("This is a header", divider="rainbow")
st.subheader("This is a subheader")

st.image("https://letsenhance.io/static/8f5e523ee6b2479e26ecc91b9c25261e/1015f/MainAfter.jpg")

def is_prime(num):
  """
  Check if the given number is prime.
  """
  if num <= 1:
    return False
  elif num <= 3:
    return True
  elif num % 2 == 0 or num % 3 == 0:
    return False
  i = 5
  while i * i <= num:
    if num % i == 0 or num % (i + 2) == 0:
      return False
    i += 6
  return True

def prime_numbers(start, count):
  """
  Generate prime numbers within the given range (inclusive start, exclusive end).
  """
  num = start
  prime_list = []
  while len(prime_list) < count:
    if is_prime(num):
      prime_list.append(num)
    num += 1
  return prime_list

def format_list(item_list):
  """
  Format the given list as a Markdown bullet list.
  """
  return "\n".join([f"* {item}" for item in item_list])

def create_page(start, count, filename):
  """
  Generate and save a Markdown page listing prime numbers within the given range.
  """
  prime_list = format_list(prime_numbers(start, count))
  with open(filename, "w") as file:
    file.write(prime_list)

if __name__ == "__main__":
  create_page(1, 100, "primes1.md")
  create_page(101, 100, "primes101.md")
  create_page(201, 100, "primes201.md")
  # ... copy and modify the code to create more pages as needed.

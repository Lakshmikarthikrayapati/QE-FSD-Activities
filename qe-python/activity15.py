try:
    print(underfined_variable)
except NameError as e:
    print(f"Caught an error: {e}")
print("Exception continues without halting.")
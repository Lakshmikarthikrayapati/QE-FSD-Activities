fruit = {
    "apple": 100,
    "banana": 30,
    "orange": 50,
    "mango": 80,
    "grapes": 40
}
# fruit available
input = input("Enter  the fruit available to check: ")
print(f"is the {fruit} is available? {input in fruit}")
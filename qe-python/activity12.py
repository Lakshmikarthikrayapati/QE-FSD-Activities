def sum_of_nums(num:int):
    if num <=1:
        return num
    else:
        return num + sum_of_nums_nums(num-1)
print(f"sum_of_nums(10)")
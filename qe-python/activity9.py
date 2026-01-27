def combine_lists(list1, list2):
    odd_from_list1 = [num for num in list1 if num % 2 != 0]
    even_from_list2 = [num for num in list2 if num % 2 == 0]
    new_list = odd_from_list1 + even_from_list2
    return new_list
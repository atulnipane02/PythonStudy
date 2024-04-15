def linear_search_dictionary(dict1, value):
    for k, v in dict1.items():
        if (v == value):
            print("Found at key", k)
            return True
    print("Target is not in the dictionary")
    return False


my_dictionary = {"red": 5, "blue": 3, "yellow": 12, "green": 7}
linear_search_dictionary(my_dictionary, 5)
linear_search_dictionary(my_dictionary, 3)
linear_search_dictionary(my_dictionary, 8)

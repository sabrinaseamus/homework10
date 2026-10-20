my_list = [1, "apple", 3.14, True, "banana", None, "cherry", [1, 2]]
count = 0
for item in my_list:
    if type(item) == str:
        count += 1
print("Count of str elements:", count)
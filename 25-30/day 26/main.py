with open(r"25-30\day 26\file1.txt") as file1:
    list1 = file1.readlines()
with open(r"25-30\day 26\file2.txt") as file2:
    list2 = file2.readlines()

list3 = [int(num) for num in list1 if num in list2]
print(list3)

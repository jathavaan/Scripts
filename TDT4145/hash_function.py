from prettytable import PrettyTable

num_list = []
hashed_list = []
binary = []

mod = int(input("The mod number: "))
num_string = input("Type in your numbers with a space between each number: ")

num_list = list(map(lambda num: int(num), num_string.split(" ")))

print(f"Your hash function is: h(k)=k mod {mod}\n")

for i in range(len(num_list)):
    num = num_list[i]
    hashed_num = num % mod
    hashed_list.append(hashed_num)
    binary.append(bin(hashed_num))

table = PrettyTable()
table.field_names = ["Start number", "Hashed number", "Binary"]

for j in range(len(hashed_list)):
    start_num = num_list[j]
    hashed_num = hashed_list[j]
    binary_num = binary[j]
    table.add_row([start_num, hashed_num, binary_num[2:]])

print()
print(table)

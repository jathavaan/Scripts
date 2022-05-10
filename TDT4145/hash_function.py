from prettytable import PrettyTable

num_list = []
hashed_list = []
binary = []

num_count = int(input("Amount of numbers: "))
mod = int(input("The mod number: "))

iteration = 1

print(f"Your hash function is: h(k)=k mod {mod}\n")

for i in range(num_count):
    num = int(input(f"{iteration}. Write your number: "))
    num_list.append(num)
    hashed_num = num % mod
    hashed_list.append(hashed_num)
    binary.append(bin(hashed_num))

    iteration += 1

table = PrettyTable()
table.field_names = ["Start number", "Hashed number", "Binary"]

for j in range(len(hashed_list)):
    start_num = num_list[j]
    hashed_num = hashed_list[j]
    binary_num = binary[j]
    table.add_row([start_num, hashed_num, binary_num[2:]])

print()
print(table)

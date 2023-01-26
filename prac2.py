a = ""
num = []


while a != "0":
    a = input()
    if a != "0":
        num.append(int(a))




print("*"*8)

print(f"max: {max(num)}")
print(f"min: {min(num)}")
print(f"sum: {sum(num)}")
print(f"av: {(sum(num)/len(num))}")

unique = set(num)


print(unique)

for i in unique:
    print(f"{i} = {num.count(i)}")
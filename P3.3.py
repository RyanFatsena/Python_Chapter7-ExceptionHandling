# Praktikum 3 Nomor 3

file = open("/Users/ryanbrilianfatsena/Documents/data2.txt", "r")
sum = 0
for data in file:
    sum = sum + int(data)
print(sum)

my_list = []
sum = 0
while True:
    num = int(input("A number:"))
    if num == -1:
        break
    my_list.append(num)
    sum = sum + num
print(my_list)
print(sum)
    
    
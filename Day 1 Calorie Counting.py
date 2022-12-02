total_list = []
value = input()
#print(value)
end = 0
while True:
    #print("First True")
    sum = 0
    while True:
        #print("Second True")
        value = input()
        print(value)
        try: value = int(value)
        except:
            #print("Break")
            break
        if value == 1121:
            print("We got 1121!")
            end = 1
            break
        sum += value
    #print(sum)
    print(end)
    total_list.append(sum)
    if end == 1:
        print("Final Break")
        break
max = -1
for i in total_list:
    if i > max:
        max = i
print(max)

total_list.sort(reverse=True)
sum = 0
for i in range(3):
    print(total_list[i])
    sum += total_list[i]
print(sum)
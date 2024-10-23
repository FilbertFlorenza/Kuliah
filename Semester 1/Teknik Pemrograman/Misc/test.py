counter = 0
for i in range(1,781):
    if((i % 2 == 0 or i % 7 == 0) and i % 3 != 0):
        counter += 1

print(counter)
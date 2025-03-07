file_name = "johnny.txt"
cnt = 0
with open(file_name, 'r') as file:
    for line in file:
        cnt += 1

print("Number of lines:", cnt)
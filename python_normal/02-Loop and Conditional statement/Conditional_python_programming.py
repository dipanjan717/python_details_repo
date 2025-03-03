print("Range function ...")

for i in range(0,6):
    print(i)

print("While loop ...")

count = 0

while(count<= 5):
    print(f"count-->{count}")
    count += 1


print("Control Statements...")

print("break statement...")

for i in range(7):
    if i == 5:
        break
    print(i)

print("continue statement...")

for i in range(7):
    if i%2 == 0:
        continue
    print(i)
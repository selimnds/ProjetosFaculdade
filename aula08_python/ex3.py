import os 
os.system("cls")

v = [45, -89, 32, -12, 33]
print(v[0])

for n in range(0, 5, 1):
    if v[n] < 0:
        print(v[n], end=' ')

s = 0 
for n in range(0, 5, 1):
    s += v[n]
print('\n', s)
print(s/5)

for n in range (0, 5, 1):
    if v[n] % 2 != 0:
        print(v[n], end=' ')

g = int(input("Quanto você gastou (sem cifrão ou decimais)? "))

if g > 1000:
    g = g - (g*0.1)
else:
    g = g - (g*0.05)
print(f"{g:.2f}")
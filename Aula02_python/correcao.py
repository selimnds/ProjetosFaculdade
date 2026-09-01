# b) 8
# c) 27.25
# d) PythonLógica de programacao
# e)16.6666
# f) 0
# G) =~ 2.5
# h) ~ 15
# i) Lógica de programaçãoPython.

import os
os.system("cls")
a = 10
b  = 5
c = 3
d = 20.5
e = 7.5
f = 0.75
g = "Python"
h = "Lógica de programação"
i = 2.5

listaDeResp = [a - b + c, d + e - f, g+h, a*b/c, a%b//c, d//e%f, a+d/c-f, h+g+'.',c%a+d//e, c//(a+d)%e]

for i in listaDeResp:
    print(f"resp é: {i} \n")

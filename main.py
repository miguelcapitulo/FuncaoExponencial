from expo import funcao_exponencial
from grafic import mostrar

while True:
    resultado=funcao_exponencial()
    x=resultado[1]
    y=resultado[0]
    print(x)
    print(y)
    c=0
    while c < len(x):
        print(f"({x[c]}, {y[c]})")
        c+=1
    mostrar(x, y)
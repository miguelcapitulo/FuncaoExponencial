def funcao_exponencial():
    print("f(x)=a*b^x")
    while True:
        try:
            a = int(input("Digite o valor de a (diferente de 0): "))
            if a == 0:
                print("O valor de 'a' não pode ser 0. Tente novamente.")
                continue
            else:
                break
        except ValueError:
            print("Entrada inválida! Por favor, insira um número inteiro.")
    while True:
        try:
            b = int(input("Digite o valor de b (b > 0 e b ≠ 1): "))
            if b <= 0 or b == 1:
                print("O valor de 'b' deve ser maior que 0 e diferente de 1. Tente novamente.")
                continue
            else:
                break
        except ValueError:
            print("Entrada inválida! Por favor, insira um número inteiro.")
    while True:
        try:
            i = int(input("Digite o valor de i (início do intervalo): "))
            break
        except ValueError:
            print("Entrada inválida! Por favor, insira um número inteiro.")
    while True:
        try:
            f = int(input("Digite o valor de f (fim do intervalo, deve ser maior ou igual a i): "))
            if f < i:
                print("O valor de 'f' deve ser maior ou igual a 'i'. Tente novamente.")
                continue
            else:
                break
        except ValueError:
            print("Entrada inválida! Por favor, insira um número inteiro.")
    resultados=[]
    x=[]
    while(i<=f):
        resultados.append(a*(b**i))
        x.append(i)
        i +=1
    return list(resultados), list(x)
resultado=funcao_exponencial()
x=resultado[1]
y=resultado[0]
print(x)
print(y)
from grafico import mostrar
mostrar(x,y)






def conceito():
    return('Uma função exponencial é uma função matemática em que a variável aparece no expoente. Ela é geralmente escrita na forma f(x) = a·b^x, onde a é um número real diferente de zero e b é a base, um número positivo e diferente de um. Esse tipo de função é usado para representar situações de crescimento ou decaimento rápido. Quando a base b é maior que 1, a função é crescente, e quando está entre 0 e 1, é decrescente. O gráfico da função exponencial nunca toca o eixo x, aproximando-se dele sem o atingir.')

def funcao_exponencial():
    while True:
        x = float(input("Digite o valor de x: "))
        if x==0:
            print('Resultado: f(x) = 1')
            return(1)
            
        a = float(input("Digite o valor de a (diferente de zero): "))
        while a == 0:
            print("O valor de 'a' deve ser diferente de zero.")
            a = float(input("Digite o valor de a (diferente de zero): "))
            
        b = float(input("Digite o valor de b (diferente de um): "))
        while b ==0 or b ==1:
            print("O valor de 'b' deve ser diferente de zero e diferente de um.")
            b = float(input("Digite o valor de b (diferente de um): "))
        resultado = a*(b**x)
        print(f"O resultado da função exponencial para x={x}, a={a}, b={b} é: {resultado}")
        return resultado

print(funcao_exponencial())

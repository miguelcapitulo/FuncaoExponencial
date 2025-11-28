import matplotlib.pyplot as plt

def mostrar(x, y):
    plt.plot(x, y, color="#0066FF", linestyle='-',marker='')

    plt.title('Gráfico da função')
    plt.xlabel('Eixo X')
    plt.ylabel('Eixo Y')
    
    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(0, color='black', linewidth=1)  

    plt.grid(True)
    plt.legend(['Gráfico exponencial'])
    plt.show()
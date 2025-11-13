import matplotlib.pyplot as plt

def mostrar(x, y):
    plt.plot(x,y, label='Relação entre X e Y', color='#00FF7F', linestyle='-',marker='')
    plt.title('Gráfico da função')
    plt.xlabel('Eixo X')
    plt.ylabel('Eixo Y')
    plt.show()
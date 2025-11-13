import tkinter as tk
from tkinter import messagebox
import math

def obter_valores(tipo):
    valores = {}

    if tipo == "exponencial":
        while True:
            try:
                a = float(input_a.get())
                b = float(input_b.get())
                x = float(input_x.get())
                # Regras da função exponencial
                if b <= 0 or b == 1:
                    messagebox.showerror("Erro", "A base 'b' deve ser positiva e diferente de 1.")
                    return
                if a == 0:
                    messagebox.showerror("Erro", "O coeficiente 'a' não pode ser zero.")
                    return
                valores = {"a": a, "b": b, "x": x}
                break
            except ValueError:
                messagebox.showerror("Erro", "Digite valores numéricos válidos.")
    elif tipo == "1grau":
        while True:
            try:
                a = float(input_a.get())
                b = float(input_b.get())
                x = float(input_x.get())
                if a == 0:
                    messagebox.showerror("Erro", "O coeficiente 'a' não pode ser zero (senão não é 1º grau).")
                    return
                valores = {"a": a, "b": b, "x": x}
                break
            except ValueError:
                messagebox.showerror("Erro", "Digite valores numéricos válidos.")
    elif tipo == "2grau":
        while True:
            try:
                a = float(input_a.get())
                b = float(input_b.get())
                c = float(input_c.get())
                x = float(input_x.get())
                if a == 0:
                    messagebox.showerror("Erro", "O coeficiente 'a' não pode ser zero (senão não é 2º grau).")
                    return
                valores = {"a": a, "b": b, "c": c, "x": x}
                break
            except ValueError:
                messagebox.showerror("Erro", "Digite valores numéricos válidos.")
    return valores


# Função para calcular exponencial
def calcular_exponencial():
    valores = obter_valores("exponencial")
    if not valores: return
    a, b, x = valores["a"], valores["b"], valores["x"]
    resultado = a * (b ** x)
    messagebox.showinfo("Resultado", f"f(x) = {resultado}")

# Função para calcular 1º grau (f(x) = a*x + b)
def calcular_primeiro_grau():
    valores = obter_valores("1grau")
    if not valores: return
    a, b, x = valores["a"], valores["b"], valores["x"]
    resultado = a * x + b
    messagebox.showinfo("Resultado", f"f(x) = {resultado}")

# Função para calcular 2º grau (f(x) = a*x² + b*x + c)
def calcular_segundo_grau():
    valores = obter_valores("2grau")
    if not valores: return
    a, b, c, x = valores["a"], valores["b"], valores["c"], valores["x"]
    resultado = a * (x**2) + b * x + c
    messagebox.showinfo("Resultado", f"f(x) = {resultado}")


# Criação da interface gráfica
janela = tk.Tk()
janela.title("Calculadora de Funções")
janela.geometry("400x350")

tk.Label(janela, text="a:").pack()
input_a = tk.Entry(janela)
input_a.pack()

tk.Label(janela, text="b:").pack()
input_b = tk.Entry(janela)
input_b.pack()

tk.Label(janela, text="c (apenas 2º grau):").pack()
input_c = tk.Entry(janela)
input_c.pack()

tk.Label(janela, text="x:").pack()
input_x = tk.Entry(janela)
input_x.pack()

tk.Label(janela, text="\nEscolha o tipo de função:").pack()

btn_exp = tk.Button(janela, text="Exponencial", command=calcular_exponencial)
btn_exp.pack(pady=5)

btn_1g = tk.Button(janela, text="1º Grau", command=calcular_primeiro_grau)
btn_1g.pack(pady=5)

btn_2g = tk.Button(janela, text="2º Grau", command=calcular_segundo_grau)
btn_2g.pack(pady=5)

janela.mainloop()

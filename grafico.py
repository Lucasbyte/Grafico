import matplotlib.pyplot as plt
import numpy as np

def gera_cabeca(x):
    return 2 * np.sqrt(-abs(abs(x)-1)*abs(3-abs(x))/((abs(x)-1)*(3-abs(x)))) * (1 + abs(abs(x)-3)/(abs(x)-3)) * np.sqrt(1-(x/7)**2) + (5 + 0.97*(abs(x-.5)+abs(x+.5)) - 3*(abs(x-.75)+abs(x+.75))) * (1 + abs(1-abs(x))/(1-abs(x)))

def gera_concavidade_inferior(x):
    return -3 * np.sqrt(1-(x/7)**2) * np.sqrt(abs(abs(x)-4)/(abs(x)-4))

def gera_asa_inferior(x):
    return abs(x/2) - 0.0913722 * x**2 - 3 + np.sqrt(1-(abs(abs(x)-2)-1)**2)

def gera_curva_asa(x):
    return (2.71052 + (1.5 - 0.5*abs(x)) - 1.35526 * np.sqrt(4-(abs(x)-1)**2)) * np.sqrt(abs(abs(x)-1)/(abs(x)-1)) + 0.9

x_values = np.linspace(-10, 10, 900)

cabeca = gera_cabeca(x_values)
concavidade_inferior = gera_concavidade_inferior(x_values)
asa_inferior = gera_asa_inferior(x_values)
curva_asa = gera_curva_asa(x_values)

plt.figure(figsize=(12, 8))

plt.plot(x_values, cabeca, label='cabeca', color='black')
plt.plot(x_values, concavidade_inferior, label='concavidade-inferior', color='gray')
plt.plot(x_values, asa_inferior, label='asa-inferior', color='black')
plt.plot(x_values, curva_asa, label='curva asa', color='gray')

plt.gcf().suptitle('Eu sou a noite, eu sou a sombra, eu sou a Justiça')
plt.title('Eu sou Batman')
plt.xlabel('MEDO')
plt.ylabel('JUSTIÇA')
plt.axhline(0, color='black', linewidth=1.5)  # Linha horizontal do eixo x
plt.axvline(0, color='black', linewidth=1.5)  # Linha vertical do eixo y
plt.grid(True, linestyle='--', alpha=0.8)  # Linhas de grade para melhor visualização
plt.legend()

# Exibição do gráfico
plt.show()

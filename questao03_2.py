import numpy as np
import matplotlib.pyplot as plt

'''
    Autor:      Jonnathan Alves Ramos
    Disciplina: Máquinas Elétricas 1

    Descrição:  Curvas de Torque x Escorregamento de um motor de indução com
                a variação da resistência do rotor.
'''

r1 = 0.2         # ohm
x1 = 1.2j        # ohm
r2 = 0.3         # ohm
x2 = 1.2j        # ohm
rm = 150         # ohm
xm = 18j         # ohm
ws = 2*np.pi*50  # rad/s     ws = 2*pi*f
P = 8            # polos
Va = 440         # V

### Thévenin do circuito completo
# Não simplifica
Zth = ((r1 + x1)**-1 +(xm)**-1 + (rm)**-1)**-1 + x2                        # Zth = (R1 + jX1)//(jXm)//(Rm) + jX2
Vth = Va*((rm**-1 + xm**-1)**-1)/((r1 + x1) + ((rm**-1 + xm**-1)**-1))     # Vth = Va*[(Rm//jXm) / ((R1 + jX1) + (Rm//jXm))]
####
s = np.linspace(0.0001, 0.9999, 500)                                       # Escorregamento: Vetor [0.0001, ..., 1] com 500 elementos em partes iguais
def torque(r):
    # Função que retorna o torque para cada valor de resistência
    I2 = Vth/(Zth + r/s)                                                   # Corrente I2 em relação a cada escorregamento
    Pma =(abs(I2)**2)*(r/s)                                                # Potência do rotor ao lado do estator
    return (3*P/2)*Pma/ws                                                  # Torque para cada escorregamento

T1 = torque(r2)
T2 = torque(2*r2)
T3 = torque(3*r2)
T4 = torque(4*r2)

plt.plot(s, T1, label="1*Rrotor")
plt.plot(s, T2, label="2*Rrotor")
plt.plot(s, T3, label="3*Rrotor")
plt.plot(s, T4, label="4*Rrotor")
plt.legend()
plt.title("Torque x Escorregamento de um motor de indução")
plt.xlabel("escorregamento")
plt.ylabel("Torque [N.m]")
plt.axis(xmin=0, xmax=1, ymin=0)
plt.gca().invert_xaxis()

print("1*Rrotor => Tmax = {:.2f} \t\t escorregamento em Tmax = {:.3f}".format(T1.max(), s[np.where(T1 == T1.max())][0]))
print("2*Rrotor => Tmax = {:.2f} \t\t escorregamento em Tmax = {:.3f}".format(T2.max(), s[np.where(T2 == T2.max())][0]))
print("3*Rrotor => Tmax = {:.2f} \t\t escorregamento em Tmax = {:.3f}".format(T3.max(), s[np.where(T3 == T3.max())][0]))
print("4*Rrotor => Tmax = {:.2f} \t\t escorregamento em Tmax = {:.3f}".format(T4.max(), s[np.where(T4 == T4.max())][0]))

plt.savefig("questao03_2.png")
plt.show()


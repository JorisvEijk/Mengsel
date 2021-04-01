import math
import matplotlib.pyplot as plt

Ca_conc = 0.9
CaIon_conc = 0
Al_conc = 1.2
AlIon_conc = 0
Br2_conc = 1.3
BrIon_conc = 0

# Reactie 1: Ca + Br2 -> Ca2+ + 2 Br-
k1 = 0.5

# Reactie 2: 2 Al + 3Br2 -> 2 Al3+ + 6 Br-
k2 = 0.4

#Reactie 3: 3 Ca + 2 Al3+ -> 3 Ca2+ + 2 Al
k3 = 0.2

time = 0
time_max = 15
dt = 0.01

Ca_set = []
CaIon_set = []
Al_set = []
AlIon_set = []
Br2_set = []
BrIon_set = []
time_set = []

Ca_set.append(Ca_conc)
CaIon_set.append(CaIon_conc)
Al_set.append(Al_conc)
AlIon_set.append(AlIon_conc)
Br2_set.append(Br2_conc)
BrIon_set.append(BrIon_conc)
time_set.append(time)

while time <= time_max:

    d_Al_conc = 0
    d_AlIon_conc = 0
    d_Ca_conc = 0
    d_CaIon_conc = 0
    d_Br2_conc = 0
    d_BrIon_conc = 0

    rate1 = k1 * Ca_conc * Br2_conc
    rate2 = k2 * Al_conc * Br2_conc
    rate3 = k3 * Ca_conc * AlIon_conc

#Reactie 1
    d_Ca_conc -= rate1 * dt
    d_Br2_conc -= rate1 * dt
    d_CaIon_conc += rate1 * dt
    d_BrIon_conc += rate1 * dt * 2

#Reactie 2
    d_Al_conc -= rate2 * dt * 2
    d_Br2_conc -= rate2 * dt * 3
    d_AlIon_conc += rate2 * dt * 2
    d_BrIon_conc += rate2 * dt * 6

#Reactie 3
    d_Ca_conc -= rate3 * dt * 3
    d_AlIon_conc -= rate3 * dt * 2
    d_CaIon_conc += rate3 * dt * 3
    d_Al_conc += rate3 * dt * 2

#Alle veranderingen verwerken
    Ca_conc += d_Ca_conc
    CaIon_conc += d_CaIon_conc
    Al_conc += d_Al_conc
    AlIon_conc += d_AlIon_conc
    Br2_conc += d_Br2_conc
    BrIon_conc += d_BrIon_conc

    time += dt

    Ca_set.append(Ca_conc)
    CaIon_set.append(CaIon_conc)
    Al_set.append(Al_conc)
    AlIon_set.append(AlIon_conc)
    Br2_set.append(Br2_conc)
    BrIon_set.append(BrIon_conc)
    time_set.append(time)

plt.plot(time_set, CaIon_set, 'r', time_set, Ca_set, 'r--', time_set, AlIon_set, 'b', time_set, Al_set, 'b--', time_set, Br2_set, 'g--', time_set, BrIon_set, 'g')
plt.grid(True)
plt.xlabel('tijd')
plt.ylabel('concentratie')
plt.xlim(0, time_max)
plt.ylim(0, 1.5)
plt.show()

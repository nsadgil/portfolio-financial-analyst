#%%
import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np

mois = ["Jan", "Fév", "Mar", "Avr"]
ca = [15000, 18000, 14000, 20000]

plt.plot(mois, ca)
plt.title("Évolution du CA")
plt.xlabel("Mois")
plt.ylabel("Chiffre d'affaires")
plt.show()

#%%
import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np
mois = ["Jan", "Fév", "Mar", "Avr"]
ca = [15000, 18000, 14000, 20000]

plt.plot(mois, ca)
plt.title("Évolution du CA")
plt.xlabel("Mois")
plt.ylabel("Chiffre d'affaires")
plt.show()
# %%
dept = ['Sales', 'IT', 'Marketing']
ca_2024 = [120, 85, 95]  
ca_2025 = [140, 90, 110]

plt.style.use('dark_background')

plt.figure(figsize=(8,5))

x = np.arange(len(dept))
largeur = 0.4
ecart = 0.01

plt.bar(x - largeur/2 - ecart/2, ca_2024, width=0.3, label='CA_2024', color='blue')
plt.bar(x + largeur/2 + ecart/2, ca_2025, width=0.3, label='CA_2025', color='orange')
plt.xticks(x, dept)
plt.legend()
plt.xlabel('Departement')
plt.ylabel('Chiffre d\'affaires (USD)')
plt.title('CA par departement')
plt.gca().set_axisbelow(True)
plt.grid(axis='y', alpha=0.2)
plt.tight_layout()
plt.show()
# %%
dept = ['Sales', 'IT', 'Marketing']
ca = [120, 85, 95]  
plt.figure(figsize = (8,5))
plt.plot(dept, ca, color='#305B7D', marker='o')
plt.title('Evolution du CA')
plt.xlabel('Department')
plt.ylabel('Chiffre d\'affaires')
plt.gca().set_axisbelow(True)
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()

# %%
mois = ["Jan", "Fév", "Mar", "Avr"]
ca = [15000, 18000, 14000, 20000]

plt.figure(figsize=(8,5))
plt.pie(ca, labels=mois, autopct='%1.1f%%')
plt.title('CA%')
plt.tight_layout()
plt.show()

# %%

mois = list(range(1, 13))
ca_2023 = [154958, 133688, 177631, 139480, 168192, 128056, 120718, 135896, 119693, 150657, 175128, 167905]
ca_2024 = [160000, 137000, 180000, 141000, 171000, 131000, 123000, 139000, 122000, 153000, 178000, 171000]

plt.figure(figsize=(8,5))

plt.plot(mois, ca_2023, label= 'CA 2023', marker = 'o')
plt.plot(mois, ca_2024, label = 'CA 2024', marker = 'x')
plt.title('Chiffre d\'affaires annuel')
plt.legend()
plt.tight_layout()
plt.grid(axis='both', alpha = 0.3)
plt.show()

# %%
import matplotlib.pyplot as plt

mois = list(range(1, 13))
ca_2023 = [154958, 133688, 177631, 139480, 168192, 128056, 120718, 135896, 119693, 150657, 175128, 167905]
ca_2024 = [160000, 137000, 180000, 141000, 171000, 131000, 123000, 139000, 122000, 153000, 178000, 171000]

plt.figure(figsize=(8, 5))
plt.plot(mois, ca_2023, color="blue", label='ca_2023', marker='o')
plt.plot(mois, ca_2024, color="red", label='ca_2024', marker='o')
plt.title('Variation du CA par an', fontsize=16)
plt.legend()
plt.xlabel('Mois', fontsize=10)
plt.ylabel("CA (USD)", fontsize=10)
plt.gca().set_axisbelow(True)
plt.grid(alpha=0.5)
plt.tight_layout()
plt.savefig('ca_annuel.png')
plt.show()
# %%
dept = ['Sales', 'IT', 'Marketing']
cogs = [600, 200, 250]              
opex = [400, 550, 650]

plt.figure(figsize=(6,5))
plt.bar(dept, cogs, width=0.4, label='COGS', color='#012350')
plt.bar(dept, opex, width=0.4, bottom=cogs, label='OPEX', color='orange')
plt.legend(loc='upper center')
plt.title('CHARGES PAR DEPERTEMENT', fontsize=13)
plt.xlabel('Department', fontsize = 10)
plt.ylabel('Charges (USD)', fontsize= 10)
plt.tight_layout()
plt.gca().set_axisbelow(True)
plt.grid(axis='y', alpha=0.2)
plt.show()
# %%
mois = ["Janvier", "Février", "Mars", "Avril"]
ca = [12500, 14800, 13200, 17100]
taux_marge = [0.32, 0.38, 0.35, 0.42]

fig,axe1 = plt.subplots(figsize=(8,5))

axe1.bar(mois, ca, label='CA', color='#012350')
axe1.set_ylabel('CA en USD')

axe2 = axe1.twinx()
axe2.plot(mois, taux_marge, label='Taux de marge', color='orange', marker = 'o')
axe2.set_ylabel('Taux de marge')

plt.title('CA et taux de marge par mois')
plt.tight_layout()
plt.legend()
plt.show()
# %%
cmd = [
    25, 42, 58, 63, 75,
    89, 95, 110, 125, 138,
    152, 175, 190, 215, 245,
    280, 320, 375, 450, 620
]
plt.figure(figsize=(8,5))
plt.hist(cmd, bins=6, color='#012350', edgecolor='white')
plt.title('Distribution des commandes')
plt.xlabel('Montant en USD')
plt.ylabel('Nombre de commandes')
plt.grid(axis='y', alpha=0.3)
plt.gca().set_axisbelow(True)
plt.show()
# %%
remise = [0, 5, 10, 15, 20, 25, 30, 35, 40, 50]
profit = [120, 95, 80, 45, 20, -10, 35, 25, -60, -90]

plt.style.use('default')
plt.figure(figsize=(8,5))

plt.scatter(remise, profit, color='orange', alpha=1)
plt.axhline(0, color='red', linewidth = 1)
plt.title('Relation entre remise et profit')
plt.xlabel('Taux de remise')
plt.ylabel('Montant en USD')
plt.grid(axis='y', alpha=0.3)
plt.gca().set_axisbelow(True)
plt.show()
# %%

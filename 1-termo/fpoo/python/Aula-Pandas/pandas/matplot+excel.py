import pandas as pd
import matplotlib.pyplot as plt

p = pd.read_excel('pessoas.xlsx')
plt.pie(p['Idade'], labels=p['Nome'], autopct='%1.1f%%')
plt.show()
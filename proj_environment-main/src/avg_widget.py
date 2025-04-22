# Funksjon for å finne avg_widget
import matplotlib.pyplot as plt
import seaborn as sns
import ipywidgets as widgets
import pandas as pd
from IPython.display import clear_output


file_path = '../data/csv/ENOL_wind_data.csv'
df_ENOL = pd.read_csv(file_path)

def avg_widget(ses=2.5):
    clear_output(wait=True)
    plt.figure(figsize=(6, 4))
    sns.kdeplot(df_ENOL['Wind_speed'], lw=2.5, fill=True, bw_adjust=ses)
    
    plt.xlim(0, 60)
    plt.ylim(0.0, 0.1)
    plt.title(f'Vindhastighet - relativ sannsynlighet (KDE) med glatting: {ses}', fontsize=14)
    plt.xlabel('Vindhastighet (m/s)')
    plt.ylabel('Tetthet')
    plt.grid(True)
    plt.show()

    
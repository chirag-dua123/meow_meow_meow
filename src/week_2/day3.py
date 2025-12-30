import pandas as pd
import matplotlib.pyplot as plt

#creating the dataframe
df = pd.read_csv('titanic.csv')

#filling missing values in 'Fare' column with the mean fare
df = df.fillna(df.mean(numeric_only=True))

#making the plots
bins = 20       #number of bars (intervals)
fig, axes = plt.subplots(1, 3, figsize=(12, 4), sharey=True) #3 subplots in one row with 12x4 size that share the y axis
colors = ['#1f77b4', '#ff7f0e', '#2ca02c']      #colors for each class
for ax, pclass, color in zip(axes, [1, 2, 3], colors):  #looping through each subplot, passenger class and color
        data = df[df['Pclass'] == pclass]['Fare'].dropna()      #getting fare data for the specific passenger class     
        ax.hist(data, bins=bins, color=color, alpha=0.75)
        ax.set_title(f'Class {pclass}')
        ax.set_xlabel('Fare')
        ax.grid(True)

axes[0].set_ylabel('Frequency')
fig.suptitle('Fare Distribution by Passenger Class')
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.savefig('fare_by_pclass.png', dpi=150)

plt.show()
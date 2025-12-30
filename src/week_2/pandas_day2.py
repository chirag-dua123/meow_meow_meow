import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



def main():
    data = pd.read_csv('titanic.csv')
    df = pd.DataFrame(data)
    print(df.shape)
    print(df.info())
    print(df.describe())

    
    df = df.fillna('Unknown')

    print(df)

    print(df.groupby('Pclass').size())

    print(df.columns)

    # Box plot for Fare
    df.boxplot(column='Fare', by='Pclass')
    plt.title('Fare Distribution by Class')
    plt.suptitle('')
    plt.show()

    # Histogram for Fare
    df = df.fillna(df.mean(numeric_only=True))
    for pclass in [1, 2, 3]:
        data = df[df['Pclass'] == pclass]['Fare'].dropna()
        plt.hist(data, bins=20, alpha=0.5, label=f'Class {pclass}')
    plt.xlabel('Fare')
    plt.ylabel('Frequency')
    plt.title('Fare Distribution by Passenger Class')
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == "__main__":
    main()
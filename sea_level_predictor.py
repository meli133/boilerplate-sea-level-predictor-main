import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    df = pd.read_csv('epa-sea-level.csv')

    plt.scatter(
        df['Year'],
        df['CSIRO Adjusted Sea Level']
    )

    result = linregress(
        df['Year'],
        df['CSIRO Adjusted Sea Level']
    )

    years = range(1880, 2051)
    y = result.intercept + result.slope * years
    plt.plot(years, y)

    df_2000 = df[df['Year'] >= 2000]

    result2 = linregress(
        df_2000['Year'],
        df_2000['CSIRO Adjusted Sea Level']
    )

    years2 = range(2000, 2051)
    y2 = result2.intercept + result2.slope * years2
    plt.plot(years2, y2)

    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')

    plt.savefig('sea_level_plot.png')
    return plt.gca()
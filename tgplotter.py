from matplotlib import pyplot as pl

import pandas as pd

import os

filepath = './Tg.pkl'

df = pd.read_pickle(filepath)

systems = df['System'].unique()
for system in systems:

    df1 = df[df['System'] == system]
    compositions = df1['Composition [decimal]'].unique()
    for composition in compositions:

        df2 = df1[df1['Composition [decimal]'] == composition]
        df2 = df2.reset_index(drop=True)  # Reset the index

        fig, ax = pl.subplots(2, 1)

        ax[0].errorbar(
                       df2['Steps [-]'],
                       df2['Mean Tg from E-3kT Curve [K]'],
                       df2['STD Tg from E-3kdT Curve [K]'],
                       linestyle='none',
                       marker='.',
                       color='b',
                       ecolor='r'
                       )

        ax[1].errorbar(
                       df2['Steps [-]'], 
                       df2['Mean Tg from Specific Volume Curve [K]'], 
                       df2['STD Tg from Specific Volume Curve [K]'],
                       linestyle='none',
                       marker='.',
                       color='b',
                       ecolor='r'
                       )


        ax[0].set_xlabel('Cooling Steps [-]')
        ax[0].set_ylabel('Tg from E-3kT [K]')
        ax[0].grid()

        ax[1].set_xlabel('Cooling Steps [-]')
        ax[1].set_ylabel('Tg from Specific Volume [K]')
        ax[1].grid()

        fig.tight_layout()

        location = os.path.join(*df2['Location of Jobs'][0].split('/')[:-2])
        fig.savefig(os.path.join(location, 'Tg_comparisons'))
        pl.close('all')

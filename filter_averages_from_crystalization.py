import pandas as pd
import numpy as np

dfcx = pd.read_csv('All_jobs_with_crystal_info.csv')
dftg = pd.read_pickle('Tg.pkl')

# Modify Ben's columns for mergin datasets
alloys = dfcx['alloy']
elements = [i.split('-')[1] for i in alloys]
comp = dfcx['Comp']
comp = ['{:.2f}'.format(np.round(i, 2)) for i in comp]
comp = [i+j for i, j in zip(elements, comp)]
dfcx['Comp'] = comp

df = dfcx[['alloy', 'Comp', 'Thold', 'Job', 'Run Crystallized']]
df.columns = [
              'System',
              'Composition [decimal]',
              'Steps [-]',
              'Job',
              'Crystallization'
              ]

mergecolumns = [
                'System',
                'Composition [decimal]',
                'Steps [-]',
                'Job',
                ]

dfmerge = pd.merge(dftg, df, on=mergecolumns)

dfmerge.to_html('Tg_and_crystallization.html')  # Export as an HTML table
dfmerge.to_pickle('Tg_and_crystallization.pkl')  # Export as a pickle file

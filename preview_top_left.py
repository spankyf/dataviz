import pandas as pd

home = 'Munster'
away = 'Leinster'

raw_df = pd.read_csv('_preview.csv')
raw_df['baseline'] = raw_df.capres.expanding().mean()
df = raw_df[(raw_df.team == home)|(raw_df.opposition == home)].reset_index()

baseline = df.baseline.plot( )
                                             #orientation=u'vertical')

# a plot each for home and away
actual = df['capres'].plot( marker='o', color='black', linewidth=2)
market = df['hdp'].plot( marker='x', linestyle='dashed',linewidth=1)
derived = df['expected_line'].plot( linestyle='dashed',color='blue',marker='x',linewidth=1)

"""
1 Transpose/rotate 90degrees
2 Each black dot - point on 'actual' - should show match info including opponent name, 
    opponent rateform and ft1 - ft2
3 Shade regions where column intl is 1
4 Gridlines for every 5 points on y axis - this will actually be x axis when rotated. 
5 Allow for panning/zoom
6 Add legend


extra plots:
    scatter plots of expanding means of the blind markets 
    
Toggles:
    show hide expected or market scatters plots
    
"""
import pandas as pd
import numpy as np

df = pd.read_csv('_preview.csv')
home = 'Munster'
away = 'Leinster'
# market returns

metric_columns = df.columns[-6:-4]

for col in metric_columns :

    df[col + '_rtn'] = df[col].expanding().mean()
    df[col + '_rtn'].plot()
    
home_rtn = np.where(df.team == home, df[metric_columns[0]], np.where(df.opposition == home, df[metric_columns[1]], np.nan))
pd.Series(home_rtn).fillna(method='bfill').expanding().mean().plot()

away_rtn = np.where(df.team == away, df[metric_columns[0]], np.where(df.opposition == away, df[metric_columns[1]], np.nan))
pd.Series(away_rtn).fillna(method='bfill').expanding().mean().plot()
#df[(df.team == away)|(df.opposition == away)]
"""
Format Y scale to percent
Add horizontal ax line thin red linestyle at -0.04/-4%
Add horizontal gridlines every 5%
Add legend
Add better styling for lines
 
"""
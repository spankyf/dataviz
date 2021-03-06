import pandas as pd
import numpy as np

df = pd.read_csv('_preview.csv')
home = 'Munster'
away = 'Leinster'
# market returns


match = df[(df.ft1.isnull()) & (df.team == home) & (df.opposition == away)]

df = df[(df.ft1.notnull())]  # remove unplayed games from stats calculations


# put this beside the 'Market cap is'
all_teams_covers_market_array = np.where(
    df.capres < match['hdp'].values[0], 1, 0)


# top left
home_covers_market_at_home_array = np.where(
    df[df.team == home]['capres'] < match['hdp'].values[0], 1, 0)
# bottom left
home_covers_market_array = np.concatenate([np.where(
    df[df.opposition == home]['capres'] > -match['hdp'].values[0], 1, 0), home_covers_market_at_home_array])
# top right
away_covers_market_at_away_array = np.where(
    df[df.opposition == away]['capres'] > match['hdp'].values[0], 1, 0)
# bottom right
away_covers_market_array = np.concatenate([np.where(
    df[df.team == away]['capres'] < -match['hdp'].values[0], 1, 0), away_covers_market_at_away_array])


# put this beside the 'Derived handicap is'
all_teams_covers_derived_array = np.where(
    df.capres < match['expected_line'].values[0], 1, 0)
# top left
home_covers_derived_at_home_array = np.where(
    df[df.team == home]['capres'] < match['expected_line'].values[0], 1, 0)
# bottom left
home_covers_derived_array = np.concatenate([np.where(
    df[df.opposition == home]['capres'] > -match['expected_line'].values[0], 1, 0), home_covers_derived_at_home_array])
# top right
away_covers_derived_at_away_array = np.where(
    df[df.opposition == away]['capres'] > match['expected_line'].values[0], 1, 0)
# bottom right
away_covers_derived_array = np.concatenate([np.where(
    df[df.team == away]['capres'] < -match['expected_line'].values[0], 1, 0), away_covers_derived_at_away_array])

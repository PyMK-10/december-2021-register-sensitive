import pandas as pd
import numpy as np
import seaborn as sns

import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import matplotlib

plt.style.use('ggplot')
from matplotlib.pyplot import figure

% matplotlib
inline
matplotlib.rcParams['figure.figsize'] = (12, 8)

pd.options.mode.chained_assignment = None
df = pd.read_csv(r'f:\hackathon\train.csv', nrows=10000000)

cols = df.columns
# определяем цвета
# желтый - пропущенные данные, синий - не пропущенные
colours = ['#000099', '#ffff00']
sns.heatmap(df[cols].isnull(), cmap=sns.color_palette(colours))

# определяем процент отсутствующих данных
for col in df.columns:
    pct_missing = np.mean(df[col].isnull())
    print('{} - {}%'.format(col, round(pct_missing * 100)))

# сначала создаем индикатор для признаков с пропущенными данными
for col in df.columns:
    missing = df[col].isnull()
    num_missing = np.sum(missing)

    if num_missing > 0:
        print('created missing indicator for: {}'.format(col))
        df['{}_ismissing'.format(col)] = missing

# затем на основе индикатора строим гистограмму
ismissing_cols = [col for col in df.columns if 'ismissing' in col]
df['num_missing'] = df[ismissing_cols].sum(axis=1)
df['num_missing'].value_counts().reset_index().sort_values(by='index').plot.bar(x='index', y='num_missing')

# приводим к одному виду данные по устройствам
df['os_lower'] = df['os'].str.lower()
df['os_lower'].value_counts(dropna=False)

# заполоняем отсутвующие данные в столбцах категорий приложений на основе названия приложения
for i in pd.unique(dfnan['bundle']).tolist():

    dataPar = df[df['bundle'] == i]
    dataPar.dropna(axis=0, inplace=True)
    print(dataPar['gamecategory'].unique(), i)
    print(dataPar['subgamecategory'].unique(), i)
    if dataPar['gamecategory'].unique() != "" and len(:
        df.loc[df['bundle'] == i, 'gamecategory'] = dataPar['gamecategory'].unique()
    if dataPar['subgamecategory'].unique() != "":
        df.loc[df['bundle'] == i, 'subgamecategory'] = dataPar['subgamecategory'].unique()
    else:
        k += 1
    print(f'bundle {i} empty {k}')

    print(" *****************" * 4)

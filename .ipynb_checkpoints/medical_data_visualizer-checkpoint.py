import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('boilerplate-medical-data-visualizer/medical_examination.csv')
#print(df.head())
# 2
df['overweight'] = ((df['weight']/(df['height']/100) ** 2)>25).astype(int)
#print(df)
# 3
df['cholesterol']=(df['cholesterol']>1).astype(int)
df['gluc']=(df['gluc']>1).astype(int)
print(df)
# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df,
                 id_vars=['cardio'],
                 value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])



    # 6
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']) \
               .size() \
               .reset_index(name='total')

    
    # 7



    # 8
    fig = sns.catplot(x='variable', y='total', hue='value', col='cardio', data=df_cat, kind='bar').fig
    fig.show()
    
    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = None

    # 12
    corr = None

    # 13
    mask = None



    # 14
    fig, ax = None

    # 15



    # 16
    fig.savefig('heatmap.png')
    return fig

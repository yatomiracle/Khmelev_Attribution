# -*- coding: utf-8 -*-

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_excel("file.xlsx", sheet_name=0)
a = df.to_numpy()
sns.set(font_scale=1)
hmp = sns.heatmap(a, cmap='Blues', linewidths= .3, yticklabels=['Подписи'])
plt.title("Название", fontsize =20)
plt.show()
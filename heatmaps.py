""" Данный код принимает на вход матрицу в формате xlsx и строит по ней тепловую диаграмму """
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_excel("file.xlsx", sheet_name=0) # чтение xlsx файла с матрицей
a = df.to_numpy() # обработка матрицы как матрицы библиотеки numpy
sns.set(font_scale=1)
hmp = sns.heatmap(a, cmap='Blues', linewidths= .3, yticklabels=['Подписи']) # задание необходимых настроек для построения диаграммы
plt.title("Название", fontsize =20)
plt.show() # построение диаграммы

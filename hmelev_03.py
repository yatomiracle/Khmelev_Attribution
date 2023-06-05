# Программа работает с предобработанным текстом на русском языке.
# Вычисляет приведенную статистику Хмелёва первого текста относительно второго и наоборот,
# а также их среднее.
# Обозначения см. Хмелёв (2000) https://www.philol.msu.ru/~lex/khmelev/published/vestnik/vestnik2000.pdf

chapter_1=open("Сказка о рыбаке и рыбке.txt", 'r',encoding="utf-8").read()
chapter_2=open("Сказка о медведихе.txt", 'r',encoding="utf-8").read()
chapter_3=open("Сказка о золотом петушке.txt", 'r',encoding="utf-8").read()
chapter_4=open("Сказка о попе и о работнике его Балде.txt", 'r',encoding="utf-8").read()
chapter_5=open("Сказка о мёртвой царевне и о семи богатырях.txt", 'r',encoding="utf-8").read()
chapter_6=open("Конек-горбунок.txt", 'r', encoding="utf-8").read()

list_of_texts=[] # все тексты собираются в один большой список
list_of_texts.append(chapter_1)
list_of_texts.append(chapter_2)
list_of_texts.append(chapter_3)
list_of_texts.append(chapter_4)
list_of_texts.append(chapter_5)
list_of_texts.append(chapter_6)

import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

matr=np.zeros((len(list_of_texts),len(list_of_texts))) # строитмся матрица, заполненная нулями

for a in range(len(list_of_texts)):
        print(a)
        text = list_of_texts[a]
        AllTheText=[]
        AllTheText.extend(text)

        if AllTheText[-1]!=' ':
                AllTheText.extend(' ')

        alphabet=list(set(AllTheText)) # для каждого из текстов собирается собственный алфавит
        alphabet.sort()
        print(alphabet)

        m=len(alphabet)

        nu=np.zeros((m,m))
        print(nu)

        q=np.zeros((m,m))

        for i in range(m):
                for j in range(m):
                        for k in range(len(AllTheText)-1):
                                if AllTheText[k]==alphabet[i] and AllTheText[k+1]==alphabet[j]:
                                        nu[i,j]=nu[i,j]+1 # матрица заполняется значениями
                
        for i in range(m):
                for j in range(m):
                        q[i,j]=nu[i,j]/sum(nu[i,:]) # матрица заполняется значениями
                        
        for b in range(len(list_of_texts)):
                text=list_of_texts[b]
                AllTheText=[]
                AllTheText.extend(text)

                if AllTheText[-1]!=' ':
                        AllTheText.extend(' ')

                h=np.zeros((m,m)) 
                p=np.zeros((m,m)) # аналогично создаются матрицы из нулей

                for i in range(m):
                        for j in range(m):
                                for k in range(len(AllTheText)-1):
                                        if AllTheText[k]==alphabet[i] and AllTheText[k+1]==alphabet[j]:
                                              h[i,j]=h[i,j]+1 # происходит заполнение матрицы

                L=0
                L2=0
                for i in range(m):
                        for j in range(m):
                                p[i,j]=0
                                if sum(h[i,:])>0:
                                        p[i,j]=h[i,j]/sum(h[i,:]) # происходит заполнение матрицы


                for i in range(m):
                        for j in range(m):
                                if p[i,j]>0 and q[i,j]>0:
                                        L=L-nu[i,j]*np.log(p[i,j]/q[i,j])
                                        L2=L2-h[i,j]*np.log(q[i,j]/p[i,j])

                matr[a,b]=(L/sum(sum(nu[:,:]))+L2/sum(sum(h[:,:])))/2 # симметричная статистика Хмелёва
                # matr[a,b]=L/sum(sum(nu[:,:]))    # асимметричная статистика Хмелёва

print(matr) # вывод полученной матрицы в консоль

df = pd.DataFrame(matr)
filepath = '327_words_sym.xlsx' 
df.to_excel(filepath, index=False) # сохранение матрицы в формат xlsx

# print(L)
# print('Число знаков text ',sum(sum(nu[:,:])))
# print('Число знаков text2 ',sum(sum(h[:,:])))
# print('Приведенная статистика Хмелёва для text относительно text2 ', L/sum(sum(nu[:,:])))
# print('Приведенная статистика Хмелёва для text2 относительно text ', L2/sum(sum(h[:,:])))
# print('Среднее из них ', (L/sum(sum(nu[:,:]))+L2/sum(sum(h[:,:])))/2)

# Программа работает с предобработанным текстом на русском языке.
# Вычисляет приведенную статистику Хмелёва первого текста относительно второго и наоборот,
# а также их среднее.
# Обозначения см. Хмелёв (2000) https://www.philol.msu.ru/~lex/khmelev/published/vestnik/vestnik2000.pdf

chapter_1=open("короткие сокращ/сокращ_327_0.txt", 'r',encoding="utf-8").read()
chapter_2=open("Сказка о золотом петушке.txt.txt", 'r',encoding="utf-8").read()
chapter_3=open("Сказка о золотом петушке.txt", 'r',encoding="utf-8").read()
chapter_4=open("Сказка о попе и о работнике его Балде.txt", 'r',encoding="utf-8").read()
chapter_5=open("Сказка о мёртвой царевне и о семи богатырях.txt", 'r',encoding="utf-8").read()
chapter_6=open("Конек-горбунок.txt", 'r', encoding="utf-8").read()

list_of_texts=[]
list_of_texts.append(chapter_1)
list_of_texts.append(chapter_2)
list_of_texts.append(chapter_3)
list_of_texts.append(chapter_4)
list_of_texts.append(chapter_5)
list_of_texts.append(chapter_6)

#print(list_of_texts)

import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

matr=np.zeros((len(list_of_texts),len(list_of_texts)))

for a in range(len(list_of_texts)):
        print(a)
        text = list_of_texts[a]
        AllTheText=[]
        AllTheText.extend(text)

        if AllTheText[-1]!=' ':
                AllTheText.extend(' ')

        alphabet=list(set(AllTheText))
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
                                        nu[i,j]=nu[i,j]+1
                
        for i in range(m):
                for j in range(m):
                        q[i,j]=nu[i,j]/sum(nu[i,:])
                        
        for b in range(len(list_of_texts)):
                text=list_of_texts[b]
                AllTheText=[]
                AllTheText.extend(text)

                if AllTheText[-1]!=' ':
                        AllTheText.extend(' ')

                h=np.zeros((m,m))

                p=np.zeros((m,m))

                for i in range(m):
                        for j in range(m):
                                for k in range(len(AllTheText)-1):
                                        if AllTheText[k]==alphabet[i] and AllTheText[k+1]==alphabet[j]:

                                              h[i,j]=h[i,j]+1

                L=0
                L2=0
                for i in range(m):
                        for j in range(m):
                                p[i,j]=0
                                if sum(h[i,:])>0:
                                        p[i,j]=h[i,j]/sum(h[i,:])


                for i in range(m):
                        for j in range(m):
                                if p[i,j]>0 and q[i,j]>0:
                                        L=L-nu[i,j]*np.log(p[i,j]/q[i,j])
                                        L2=L2-h[i,j]*np.log(q[i,j]/p[i,j])

                matr[a,b]=(L/sum(sum(nu[:,:]))+L2/sum(sum(h[:,:])))/2 # symmetric
                # matr[a,b]=L/sum(sum(nu[:,:]))    # asymmetric

print(matr)

df = pd.DataFrame(matr)
filepath = '327_words_sym.xlsx'
df.to_excel(filepath, index=False)

sns.heatmap(matr, cmap='Blues')
plt.title("Тексты полной длины", fontsize =20)
plt.show()

# print(L)
# print('Число знаков text ',sum(sum(nu[:,:])))
# print('Число знаков text2 ',sum(sum(h[:,:])))
# print('Приведенная статистика Хмелёва для text относительно text2 ', L/sum(sum(nu[:,:])))
# print('Приведенная статистика Хмелёва для text2 относительно text ', L2/sum(sum(h[:,:])))
# print('Среднее из них ', (L/sum(sum(nu[:,:]))+L2/sum(sum(h[:,:])))/2)

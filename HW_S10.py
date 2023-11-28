'''
В ячейке ниже представлен код генерирующий DataFrame, 
которая состоит всего из 1 столбца. 
Ваша задача перевести его в one hot вид. 
Сможете ли вы это сделать без get_dummies?
'''

# Работа выполнялась в Google.Colab

import pandas as pd

# Вариант 1
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()

values = data['whoAmI'].unique()
one_hot = pd.DataFrame()
for i in values:
  one_hot[i] = (data['whoAmI'] == i).astype(int)
one_hot.head()

# Вариант 2
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data2 = pd.DataFrame({'whoAmI':lst})
data2.head()

data2.loc[data2['whoAmI'] == 'robot', 'robot'] = 1
data2.loc[data2['whoAmI'] != 'robot', 'robot'] = 0
data2.loc[data2['whoAmI'] == 'human', 'human'] = 1
data2.loc[data2['whoAmI'] != 'human', 'human'] = 0
data2[['robot', 'human']] = data2[['robot', 'human']].astype(int)
data2.drop('whoAmI', axis= 1 , inplace= True)
data2.head()
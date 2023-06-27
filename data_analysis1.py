import pandas as pd
df = pd.read_csv('GoogleApps.csv')

#ЗАГРУЗКА И ОПИСАНИЕ ДАННЫХ

# Как называется приложение, расположенное первым в наборе данных?
print(df.head())


# К какой категории (Category) относится приложение, расположенное последним в наборе данных?
print(df.tail())


# Сколько столбцов содержится в наборе данных?
# Данные какого типа хранятся в каждом из столбцов?
print(df.info())


# Укажи среднее арифметическое и медиану размера приложений (Size)
print(df.describe())

#ФИЛЬТРАЦИЯ ДАННЫХ

# Сколько стоит (Price) самое дешёвое платное приложение (Type == 'Paid)?
print(df[df['Type'] == 'Paid']['Price'].min())


# Чему равно медианное (median) количество установок (Installs)
# приложений из категории (Category) "ART_AND_DESIGN"?
print(df[df['Category'] == 'ART_AND_DESIGN']['Installs'].median())


# На сколько максимальное количество отзывов (Reviews) для бесплатных приложений (Type == 'Free')
# больше максимального количества отзывов для платных приложений (Type == 'Paid')?
free = df[df['Type'] == 'Free']['Reviews'].max()
paid = df[df['Type'] == 'Paid']['Reviews'].max()
print(free - paid)


# Каков минимальный размер (Size) приложения для тинейджеров (Content Rating == 'Teen')?
print(df[df['Content Rating'] == 'Teen']['Size'].min())

# *К какой категории (Category) относится приложение с самым большим количеством отзывов (Reviews)?
print(df[df['Reviews'] == df['Reviews'].max()]['Category'])


# *Каков средний (mean) рейтинг (Rating) приложений стоимостью (Price) более 20 долларов и 
# с количеством установок (Installs) более 10000?
print(df[(df['Price'] > 20) & (df['Installs'] > 10000)]['Rating'].mean())

#ОТОБРАЖЕНИЕ ДАННЫХ
import matplotlib.pyplot as plt

#df.plot() #параметры по умолчанию
#plt.show()

#Гистограмма
#df['Size'].plot(kind='hist',bins=7)  #кол-во приложений от размера гистограммы
#plt.show()

#Ящик с усами
#df.plot(kind='box')
#plt.show()
#df['Rating'].plot(kind='box')
#plt.show()

#Диаграмма рассеивания
#df.plot(x='Rating',y='Price',kind='scatter')
#plt.show()

#Круговая диаграмма
#df['Category'].value_counts().plot(kind='pie',use_index=True)
#plt.show()

#Распределение приложений по категориям (столбиковая диаграмма)
#df['Category'].value_counts().plot(kind='bar',use_index=True)
#plt.show()
#df['Category'].value_counts().plot(kind='barh',use_index=True,figsize=(5,8),title='Распределение приложений по категориям',grid=True)
#plt.show()

print(df.pivot_table(columns='Type',index='Category',values='Rating',aggfunc='median'))
temp = df.pivot_table(columns='Type',index='Category',values='Rating',aggfunc='median')
temp.fillna(-1, inplace=True)
temp.plot(kind='barh',subplots=True,layout=(1,2),figsize=(11,8),sharey=True,grid=True)
plt.show()

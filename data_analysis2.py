import pandas as pd
df = pd.read_csv('GoogleApps.csv')


# 1 Сколько всего приложений с категорией ('Category') 'BUSINESS'?
print(df['Category'].value_counts())


# 2 Чему равно соотношение количества приложений для подростков ('Teen') и для детей старше 10 ('Everyone 10+')?
# Ответ запиши с точностью до сотых.
temp = df['Content Rating'].value_counts()
print('Соотношение:', round(temp['Teen'] / temp['Everyone 10+'], 2))


# 3.1 Чему равен средний рейтинг ('Rating') платных ('Paid') приложений?
# Ответ запиши с точностью до сотых.
temp = df.groupby(by = 'Type')['Rating'].mean()
print(temp['Paid'])


# 3.2 На сколько средний рейтинг ('Rating') бесплатных ('Free') приложений меньше среднего рейтинга платных ('Paid')?
# Ответ запиши с точностью до сотых.
print(round(temp['Paid'] - temp['Free'], 2))


# 4 Чему равен минимальный и максимальный размер ('Size') приложений в категории ('Category') 'COMICS'?
# Запиши ответы с точностью до сотых.
print(df.groupby(by = 'Category')['Size'].agg(['min', 'max']))


# Бонус 1. Сколько приложений с рейтингом ('Rating') строго больше 4.5 в категории ('Category') 'FINANCE'?
temp = df[df['Rating'] > 4.5]['Category'].value_counts()
print(temp['FINANCE'])


# Бонус 2. Чему равно соотношение бесплатных ('Free') и платных ('Paid') игр с рейтингом ('Rating') больше 4.9?
temp = df[(df['Category'] == 'GAME') & (df['Rating'] > 4.9)]['Type'].value_counts()
print(temp['Free'] / temp['Paid'])

''''''
# 1 Выведи на экран минимальный, средний и максимальный рейтинг ('Rating') платных и бесплатных приложений ('Type') с точностью до десятых.
print(round(df.groupby(by = 'Type')['Rating'].agg(['min', 'mean', 'max']), 1))


# 2 Выведи на экран минимальную, медианную (median) и максимальную цену ('Price') платных приложений (Type == 'Paid') для # разных целевых аудиторий ('Content Rating')
print(df[df['Type'] == 'Paid'].groupby(by = 'Content Rating')['Price'].agg(['min', 'median', 'max']))


# 3 Сгруппируй данные по категории ('Category') и целевой аудитории ('Content Rating') любым удобным для тебя способом
# посчитай максимальное количество отзывов ('Reviews') в каждой группе.
# Сравни результаты для категорий 'EDUCATION', 'FAMILY' и 'GAME':
# В какой возрастной группе больше всего отзывов получило приложение из категории 'EDUCATION'? 'FAMILY'? 'GAME'?


# Подсказка: ты можешь выбрать из DataFrame несколько столбцов одновременно с помощью такого синтаксиса:
# df[[<столбец 1>, <столбец 2>, <столбец 3>]]
temp = df.pivot_table(index = 'Content Rating', columns = 'Category', values = 'Reviews', aggfunc = 'max')
print(temp[['EDUCATION', 'FAMILY', 'GAME']])


# 4 Сгруппируй платные (Type == 'Paid') приложения по категории ('Category') и целевой аудитории ('Content Rating')
# Посчитай среднее количество отзывов ('Reviews') в каждой группе
# Обрати внимание, что в некоторых ячейках полученной таблицы отражается не число, а значение "NaN" - Not a Number
# Эта запись означает, что в данной группе нет ни одного приложения.
# Выбери названия категорий, в которых есть платные приложения для всех возрастных групп и расположи их в алфавитном порядке.
print(df[df['Type'] == 'Paid'].pivot_table(columns = 'Content Rating', index = 'Category', values = 'Reviews', aggfunc = 'mean'))


# Бонусная задача. Найди категории бесплатных (Type == 'Free') приложений,
# в которых приложения разработаны не для всех возрастных групп ('Content Rating')
print(df[df['Type'] == 'Free'].pivot_table(index = 'Category', columns = 'Content Rating', values = 'Reviews', aggfunc = 'mean'))

''''''
import pandas as pd
df = pd.read_csv('GoogleApps.csv')

# 1 задание: во сколько раз количество приложений для аудитории «все пользователи»  превышает количество приложения для пользователей «старше 10 лет»? 
Everyone = df[(df['Content Rating'] == 'Everyone')] ['Content Rating'].count()
Everyone10 = df[(df['Content Rating'] == 'Everyone 10+')] ['Content Rating'].count()
print('Соотношение приложений для всех и для детей:', Everyone/Everyone10)


# 2 задание: чему равен средний размер приложений для каждой целевой аудитории?
print('Средний размер приложений для аудитории Everyone:', df[df['Content Rating'] == 'Everyone']['Size'].mean())
print('Средний размер приложений для аудитории Everyone 10+:', df[df['Content Rating'] == 'Everyone 10+']['Size'].mean())
print('Средний размер приложений для аудитории Teen:', df[df['Content Rating'] == 'Teen']['Size'].mean())


# 3 задание: чему равен минимальный и максимальный размер платных и бесплатных приложений для каждой целевой аудитории? #Обозначения: а) целевой аудитории E10 - Everyone 10+; E - Everyone; T -Teen б) тип приложения F- бесплатное; P - платное.


E10_min_F = df[(df['Content Rating'] == 'Everyone 10+') & (df['Type'] =='Free')] ['Size'].min()
E_min_F = df[(df['Content Rating'] == 'Everyone') & (df['Type'] =='Free')] ['Size'].min()
T_min_F = df[(df['Content Rating'] == 'Teen') & (df['Type'] =='Free')] ['Size'].min()
E10_min_F = df[(df['Content Rating'] == 'Everyone 10+') & (df['Type'] =='Free')] ['Size'].min()
E_min_F = df[(df['Content Rating'] == 'Everyone') & (df['Type'] =='Free')] ['Size'].min()
T_min_F = df[(df['Content Rating'] == 'Teen') & (df['Type'] =='Free')] ['Size'].min()
E10_max_F = df[(df['Content Rating'] == 'Everyone 10+') & (df['Type'] =='Free')] ['Size'].max()
E_max_F = df[(df['Content Rating'] == 'Everyone') & (df['Type'] =='Free')] ['Size'].max()
T_max_F = df[(df['Content Rating'] == 'Teen') & (df['Type'] =='Free')] ['Size'].max()
E10_min_P = df[(df['Content Rating'] == 'Everyone 10+') & (df['Type'] =='Paid')] ['Size'].min()
E_min_P = df[(df['Content Rating'] == 'Everyone') & (df['Type'] =='Paid')] ['Size'].min()
T_min_P = df[(df['Content Rating'] == 'Teen') & (df['Type'] =='Paid')] ['Size'].min()
E10_max_P = df[(df['Content Rating'] == 'Everyone 10+') & (df['Type'] =='Paid')] ['Size'].max()
E_max_P = df[(df['Content Rating'] == 'Everyone') & (df['Type'] =='Paid')] ['Size'].max()
T_max_P = df[(df['Content Rating'] == 'Teen') & (df['Type'] =='Paid')] ['Size'].max()
print('Минимальный размер бесплатных приложений:', 'E10 =', E10_min_F, ';',  'E =', E_min_F, ';',  'T =', T_min_F)
print('Максимальный размер бесплатных приложений:', 'E10 =', E10_max_F, ';',  'E =', E_max_F, ';',  'T =', T_max_F)
print('Минимальный размер платных приложений:', 'E10 =', E10_min_P, ';',  'E =', E_min_P, ';',  'T =', T_min_P)
print('Максимальный размер платных приложений:', 'E10 =', E10_max_P, ';',  'E =', E_max_P, ';',  'T =', T_max_P)

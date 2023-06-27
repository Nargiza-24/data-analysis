import pandas as pd
df = pd.read_csv('GooglePlayStore_wild.csv')
# Выведи информацию о всем DataFrame, чтобы узнать, какие столбцы нуждаются в очистке
print(df.info())


# Сколько в датасете приложений, у которых не указан ('NaN') рейтинг ('Rating')?
print(len(df[pd.isnull(df['Rating'])]))

# Замени пустое значение ('NaN') рейтинга ('Rating') для таких приложений на -1.
df['Rating'].fillna(-1, inplace = True)


# Определи, какое ещё значение размера ('Size') хранится в датасете помимо Килобайтов и Мегабайтов, замени его на -1.
# Преобразуй размеры приложений ('Size') в числовой формат (float). Размер всех приложений должен измеряться в Мегабайтах.
print(df['Size'].value_counts())


def set_size(size):
   if size[-1] == 'M':
      return float(size[:-1])
   elif size[-1] == 'k':
      return float(size[:-1]) / 1024
   return -1
df['Size'] = df['Size'].apply(set_size)


# Чему равен максимальный размер ('Size') приложений из категории ('Category') 'TOOLS'?
print(df[df['Category'] == 'TOOLS']['Size'].max())


# Бонусные задания
# Замени тип данных на целочисленный (int) для количества установок ('Installs').
# В записи количества установок ('Installs') знак "+" необходимо игнорировать.
# Т.е. если в датасете количество установок равно 1,000,000+, то необходимо изменить значение на 1000000
def set_installs(installs):
   if installs == '0':
       return 0
   return int(installs[:-1].replace(',', ''))
df['Installs'] = df['Installs'].apply(set_installs)


# Сгруппируй данные по типу ('Type') и целевой аудитории ('Content Rating') любым удобным для тебя способом,
# посчитай среднее количество установок ('Installs') в каждой группе. Результат округли до десятых.
# В полученной таблице найди ячейку с самым большим значением.
# К какой возрастной группе и типу приложений относятся данные из этой ячейки?
print(round(df.pivot_table(index = 'Content Rating', columns = 'Type', values = 'Installs', aggfunc = 'mean')), 1)


# У какого приложения не указан тип ('Type')? Какой тип там необходимо записать в зависимости от цены?
print(df[pd.isnull(df['Type'])])
# Чтобы увидеть все столбцы вместо многоточия, можно применить iloc[0].
# print(df[pd.isnull(df['Type'])].iloc[0])
df['Type'].fillna('Free', inplace = True)


# Выведи информацию о всем DataFrame, чтобы убедиться, что очистка прошла успешно
print(df.info())

''''''

# Очистка данных из первого задания
df['Rating'].fillna(-1, inplace = True)


def set_size(size):
  if size[-1] == 'M':
     return float(size[:-1])
  elif size[-1] == 'k':
     return float(size[:-1]) / 1024
  return -1
df['Size'] = df['Size'].apply(set_size)


def set_installs(installs):
  if installs == '0':
      return 0
  return int(installs[:-1].replace(',', ''))
df['Installs'] = df['Installs'].apply(set_installs)


df['Type'].fillna('Free', inplace = True)


# Замени тип данных на дробное число (float) для цен приложений ('Price')
def make_price(price):
 if price[0] == '$':
     return float(price[1:])
 return 0
df['Price'] = df['Price'].apply(make_price)


# Вычисли, сколько долларов разработчики заработали на каждом платном приложении
df['Profit'] = df['Installs'] * df['Price']


# Чему равен максимальный доход ('Profit') среди платных приложений (Type == 'Paid')?
print(df[df['Type'] == 'Paid']['Profit'].max())


# Создай новый столбец, в котором будет храниться количество жанров. Назови его 'Number of genres'
def split_genres(genres):
   return genres.split(';')


df['Genres'] = df['Genres'].apply(split_genres)
df['Number of genres'] = df['Genres'].apply(len)


# Какое максимальное количество жанров ('Number of genres') хранится в датасете?
print(df['Number of genres'].max())


# Бонусное задание
# Создай новый столбец, хранящий сезон, в котором было произведено последнее обновление ('Last Updated') приложения. Назови его 'Season'
def set_season(date):
   month = date.split()[0]
   seasons = {'Зима': ['December', 'January', 'February'],
              'Весна': ['March', 'April', 'May'],
              'Лето': ['June', 'July', 'August'],
              'Осень': ['September', 'October', 'November']}
   for season in seasons:
       if month in seasons[season]:
           return season
   return 'Сезон не установлен'


df['Season'] = df['Last Updated'].apply(set_season)


# Выведи на экран сезоны и их количество в датасете
print(df['Season'].value_counts())

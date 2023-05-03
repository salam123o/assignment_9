import pandas as pd
friend_names=pd.read_csv(r"C:\Users\HP\Documents\Trainee\Salam_gitclone\salam_assignments\assign_8_a\Friends_names.csv")
print(friend_names)
print(friend_names.head())
friend_names.info()
print(friend_names.shape)
print(friend_names.tail())


import pandas
df=pandas.read_excel(r"C:\Users\HP\Documents\Trainee\Salam_gitclone\salam_assignments\assign_8_b\friend_names.xls",sheet_name="Sheet1")
print(df)
print(df.head())
df.info()
print(df.shape)
print(df.tail())


import pandas 
family_members=pandas.read_csv(r"C:\Users\HP\Documents\Trainee\Salam_gitclone\salam_assignments\assign_8_a\family_names.txt",sep="*")
print(family_members)
print(family_members.head())
family_members.info()
print(family_members.shape)
print(family_members.tail())

import pandas
Vegfood_items=pandas.read_csv(r"C:\Users\HP\Documents\Trainee\Salam_gitclone\salam_assignments\assign_8_a\Vegfood_items.txt",sep="|")
print(Vegfood_items)
print(Vegfood_items.head())
Vegfood_items.info()
print(Vegfood_items.shape)
print(Vegfood_items.tail())

import pandas
NonVegfood_items=pandas.read_csv(r"C:\Users\HP\Documents\Trainee\Salam_gitclone\salam_assignments\assign_8_a\NonVegfood_items.txt",sep="|")
print(NonVegfood_items)
print(NonVegfood_items.head())
NonVegfood_items.info()
print(NonVegfood_items.shape)
print(NonVegfood_items.tail())

import pandas
month_names=pandas.read_csv(r"C:\Users\HP\Documents\Trainee\Salam_gitclone\salam_assignments\assign_8_a\month_names.txt",sep="&")
print(month_names)
print(month_names)
print(month_names.head())
month_names.info()
print(month_names.shape)
print(month_names.tail())

import pandas
colours_names=pandas.read_csv(r"C:\Users\HP\Documents\Trainee\Salam_gitclone\salam_assignments\assign_8_a\colours_names.txt",sep="^",encoding="utf8")
print(colours_names)

import pandas
family_members=pandas.read_excel(r"C:\Users\HP\Documents\Trainee\Salam_gitclone\salam_assignments\assign_8_b\family_members.xls",sheet_name="Sheet1")
print(family_members)
print(family_members.head())
family_members.info()
print(family_members.shape)
print(family_members.tail())

import pandas
Vegfood_item=pandas.read_excel(r"C:\Users\HP\Documents\Trainee\Salam_gitclone\salam_assignments\assign_8_b\Vegfood_items.xlsx",sheet_name="Sheet1")
print(Vegfood_item)
print(Vegfood_item.head())
Vegfood_item.info()
print(Vegfood_item.shape)
print(Vegfood_item.tail())


import pandas
NonVegfood_item=pandas.read_excel(r"C:\Users\HP\Documents\Trainee\Salam_gitclone\salam_assignments\assign_8_b\NonVegfood_items.xlsx",sheet_name="Sheet1")
print(NonVegfood_item)
print(NonVegfood_item.head())
NonVegfood_item.info()
print(NonVegfood_item.shape)
print(NonVegfood_item.tail())



import pandas
month_names=pandas.read_excel(r"C:\Users\HP\Documents\Trainee\Salam_gitclone\salam_assignments\assign_8_b\month_names.xlsx",sheet_name="Sheet1")
print(month_names)
print(month_names)
print(month_names.head())
month_names.info()
print(month_names.shape)
print(month_names.tail())








"""2. Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
Ваша задача — вывести дату в текстовом виде, например: второе ноября 2013 года.
Склонением пренебречь (2000 года, 2010 года)"""

#d=str(input())
date="14.04.1980"

[dd,mm,yyyy]=date.split(".")

if dd[0]=="1":
    print("10")
if dd=="01":
    d="Первое"

#print(dd1)
#print(dd,mm,yyyy)
#print(dd,mm,yyyy)


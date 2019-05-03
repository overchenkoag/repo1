"""Работа с файлами
1. Создать модуль music_serialize.py. В этом модуле определить словарь для вашей любимой музыкальной группы, например:
my_favourite_group = {
‘name’: ‘Г.М.О.’,
‘tracks’: [‘Последний месяц осени’, ‘Шапито’],
‘Albums’: [{‘name’: ‘Делать панк-рок’,‘year’: 2016},
{‘name’: ‘Шапито’,‘year’: 2014}]}

С помощью модулей json и pickle сериализовать данный словарь в json и в байты, вывести результаты в терминал.
Записать результаты в файлы group.json, group.pickle соответственно. В файле group.json указать кодировку utf-8.
2: Создать модуль music_deserialize.py. В этом модуле открыть файлы group.json и group.pickle, прочитать из них информацию.
Получить объект — словарь из предыдущего задания."""
import json

data={
    "country":{
        "Russia":{
            "president":"Putin",
            "phonecode":7,
            "domains":["рф","ru","su"]
        },
        "Finland":{
            "president":"Niinisto",
            "phonecode":358,
            "domains":["fi","ax"]
        }
    }
}
a=["a","b","c"]

#with open("data_file.json", "w") as write_file:
#    json.dump(data, write_file)
serial=json.dumps(data)
#print(type(serial))
deserial=json.loads(serial)
print(type(deserial["country"]))
print(type(deserial["country"]["Russia"]["domains"]))
json.


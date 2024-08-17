##Dictionary
import pprint
my_dict = {
    'name' : 'john',
    'age' : '32',
    'city' : 'Hanoi'
    }
# print(my_dict)
# print(my_dict['name'])
# print(my_dict['city'])
# pprint.pprint(my_dict)
# my_dict['name'] = 'dirty mouse'.upper()
# pprint.pprint(my_dict)
# for key, value in my_dict.items():
#     print(key,value)
# for i, key in enumerate(my_dict):
#     print(i, key, my_dict[key])
# for key in my_dict.values():
#     print(key)
for i, (key, value) in enumerate(my_dict.items()):
    print(i, key, value)
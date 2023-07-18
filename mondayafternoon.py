


# You have two lists:
# For both lists, find and print items that appear more than once, and print how many times they appear.

# print(colors.count('yellow'))

# l = ['a', 'a', 'a', 'a', 'b', 'c', 'c']

# print(l.count('a'))

# a = collections.Counter(colors)
# print(a)

from collections import Counter

colors = ['yellow','green','yellow','blue','red','black','white','blue','orange','yellow','white','pink','magenta','offwhite']
#colors.sort()
cities = ['tokyo','new york','boise','nishinomiya','boise','seattle','dallas','mexico city','london','tokyo', 'boise']
#cities.sort()

def process(mylist):
    mylist.sort()
    my_counter = Counter(mylist)
    a = my_counter.items()
    # print(a)
    for val in a:
        # print(val)
        color,number = val
        if number > 1:
            print(color,number,sep=':')

print('===Colors===')
process(colors)

print('===Cities===')
process(cities)


# val = my_counter.values()
# print(val)
# key = my_counter.keys()
# print(key)

# for v in val:
#     print(f'The value is {v}')
#     if v > 1:
#         print(f'The value {v} is bigger than 1.')
#     else:
#         print(f'The value {v} is equal to 1.')





# my_array = ['きゅうり', 'トマト', 'レタス', 'レタス', 'コーン', 'オニオン', 'きゅうり', 'きゅうり']
# my_counter = Counter(my_array)
# my_counter_values = my_counter.values()
# print(type(my_counter_values))
# print(my_counter_values)

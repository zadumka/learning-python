my_dict = {'key1':123,'key2':[12,23,33],'key3':['item0','item1','item2']}
print(my_dict)
print(my_dict['key3'])
print(my_dict['key3'][1].upper())
print(my_dict['key1']- 123)

# We can also create keys by assignment.
# For instance if we started off with an empty dictionary, we could continually add to it:
d = {}
d ['My sun'] = 'Alexandr'
d ['he is'] = 7
print(d)

# Nesting with Dictionaries (Вкладення зі словниками)
d = {'зрілий':{'соковитий':{'червоний':'томат'}}}
print(d['зрілий']['соковитий']['червоний'])

order_num = {'k1':100, 'k2':200}
order_num['k3'] = 300
print(order_num)

my_dict = {'one': 0, 'two': 0, 'three': 0, 'six': 0, 'ten': 0, 'five': 0, 'seven': 0}
my_dict['one'] = 1
print(my_dict)

d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print(d['k1'][2]['k2'][1]['tough'][2][0])

# ? Задача: Список перетворити на словник, де влова будуть ключем а числа значенням (значення буде списком)

a = ['first', 3, 5, 8, 'second', 10, 20, 'third', 34, 56, 70, 'fourth', -60]
my_dict1 = {}
curent_str = None

for i in a:
    if(type(i) == str):
        my_dict1[i] = []
        curent_str = i
    else:
        my_dict1[curent_str].append(i)
print(my_dict1)

# ? Задача: Підрахувати кількість слів в тексті
my_text = 'основи алгоритмізації і програмування мовою Python основи мовою програмування основи'

d1 = {}
for e in my_text.split():
    if e in d1:
        d1[e] = d1[e] + 1
    else:
        d1[e] = 1
print(d1)

print(d1)


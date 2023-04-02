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



"""
Data Structure
    List
    Tuple
    Dictionary

Assignment:
1. Create a list of dictionary where you store directory, add at least 10 elements
    [{'name': 'xyz', 'phone': 12343232, 'address': 'so and so'}]

2. Create a employee dictionary, need at least 10 elements
    {'<employee_no>: {'emp_id': 'emp_123232', 'name': 'emp name', 'skill_sets': ['QA', 'Python', 'SQL']}
"""

# var_list = list() # []
# var_list_1 = [10, 121, 30, 14, 53, 14, 64, 47, 78, 9]
# print(var_list[1:9:2])
#
# var_list.append(1)
# var_list.extend(var_list_1)
# var_list.append(10)
# var_list.sort()
# print(var_list)
# print(var_list)
#
# var_list_str = ['This', '1is', 'test', 'sort', 'z', 'b', 'v']
# var_list_str.sort()
# print(var_list_str)
# print(var_list_1)
# var_list_1.pop(1)
# print(var_list_1)
# var_list_1.remove(14)
# var_list_1.clear()
# print(var_list_1)

#
# var_tuple = ([], {}, (1,), {})
# print(var_tuple)
# var_tuple[0].append(1)
# var_tuple[1]['a'] = 1
# var_tuple[0].append(2)
# print(var_tuple)


# var_dict = {}   # dict()
# var_dict['key1'] = 'value1'

var_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
print(var_dict.keys())
print(var_dict.values())
print(var_dict.items())
print(F"key1: {var_dict.get('key1')}")
# print(var_dict['key1'])
var_dict.pop('key3')
print(var_dict)
var_dict.update({
    'key4': 'value4',
    # 'key5': 'value5',
    # 'key6': {'key7': [{'key8': 'value8'}]}
})
print(var_dict)

x = [1,2,3]
y = [4,5,6]
x.extend(y)
print(x)
print(y)


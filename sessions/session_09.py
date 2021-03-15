"""
Looping Statement
    - For
    - while
"""

'''
for <iter> in <iterable_object>:
    <statement_1>
    <statement_2>

'''
x = ['10', 2, '3', 4, 5, 6]

# for i in x[::2]:
#     print(i, type(i))

# for i in range(1, 10, 1):  #  (0, 10, 1)
#     print(pow(2, i))
#

'''
while <condition>:
    <statement_1> 
    <statement_2>
'''
# no = 1
# while no <= 10:
#     print(no)
#     no += 1


for i in range(0, 5):
    for j in range(0,5):
        print('*', end=" ")
    print("")
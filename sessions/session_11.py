"""
User Defined Function
    - Named Function
        * function without arguments and return
        * function with arguments and without return
        * function with return and without argument
        * function with arguments and return
        * function with function as argument
        * function returns function
    - Unnamed Function
        * args
        * kwargs

Assignment:
    convert session_10 assignment into functions
"""

'''
def <function_name>(<argument1>, <argument2>):
    <statement_1>
    <statement_2>
    
    <statement_3>
    return <return_1>, <return_2>
'''


# def greetings():
#     print("Hello from Function")


# def greetings(name, message="Hello"):
#     print(F"{message} {name}")


# greetings(name='Pavan', message='Hi')

# greetings(name='Pavan')


# def greetings():
#     var = 1
#     return "Hello", var


# print(type(greetings()))
# message, name = greetings()
#
# print(name, type(name))
# print(message, type(message))

# def greetings(name, message="Hello"):
#     return F"{message} {name}"
#
#
# print(greetings(name='Jimmy', message='Bye'))

# def greetings(*args):
#     if len(args) >= 2:
#         return F"{args[0]} {args[1]}"
#     elif len(args) == 1:
#         return f"Hello {args[0]}"
#     else:
#         return "Hi Jimmy"
#
# print(greetings())
# print(greetings(*['Jimmy']))
# print(greetings(*['Bye', 'Jimmy']))
# print(greetings(*['why', 'Jimmy', '?']))


def greetings(**kwargs):
    return F"{kwargs.get('message', 'Hi')} {kwargs.get('name', 'Jimmy')} {kwargs.get('garbage', '')}"


print(greetings())
print(greetings(**{'name': 'Jimmy'}))
print(greetings(**{'message': 'Bye', 'name': 'Jimmy'}))
print(greetings(**{'message': 'why', 'name': 'Jimmy', 'garbage': '?'}))

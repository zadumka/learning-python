#? Nested Statements and Scope/ Вкладені оператори та область

#! LEGB Rule:

#! L: Local - Імена, призначені в будь-який спосіб всередині функції (def або lambda) і не оголошені
#! як глобальні всередині цієї функції.

#! E: Enclosing function locals - імена в локальному обсязі будь-яких і всіх обмежуючих функцій
#! (def або lambda), від внутрішніх до зовнішніх.

#! G: Global (module) -  Імена, призначені на верхньому рівні файлу модуля або
#! оголошені як глобальні в def всередині файлу.

#! B: Built-in (Python) - Імена, попередньо призначені в модулі вбудованих імен:
#! open, range, SyntaxError,...

#? Local

#  x is local here:
#lambda x: x ** 2

#? E: Enclosing function locals - схоже на вкладеність ДІМ?Дерево
# Global
name = 'This is the global string'

def greet():
    # Enclosing
#    name = 'Sammy'

    def hello():
        #Local
        name = 'I am local name'
        print('Hello ' + name)
    hello()
greet()


x = 50
def func(x):
    print(f'X ix {x}')
    x = 200
    print(f'I changed X to {x}')
func(x)






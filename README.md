# Финальное задание по курсу Python
Сервис по приготовлению и доставке пиццы.

В файле pizza_classes.py содержится абстрактный класс пиццы и три наследника. 

В файле pizza_functions содержатся функции, отвечающие за приготовление и доставку пиццы.

В файле cli.py содержится интерфейс командной строки. 


## Командная строка

### Menu
Чтобы увидеть меню, введите

`$ python3 cli.py menu`

### Order 
Чтобы сделать заказ c доставкой, введите 

`$ python3 cli.py order {pizza name} --delivery --size {"L"\"XL""}`

Чтобы сделать заказ и забрать его самостоятельно, введите

`$ python3 cli.py order {pizza name} --size {"L"\"XL""}`

## Тестирование
Тесты с покрытием запускаются с помощью 

`$ pytest --cov=cli --cov=pizza_functions --cov=pizza_classes --cov`

Привожу результaты тестов.

~~~~---------- coverage: platform linux, python 3.10.6-final-0 -----------
Name                      Stmts   Miss  Cover
---------------------------------------------
cli.py                       30      7    77%
pizza_classes.py             35      2    94%
pizza_functions.py           28      2    93%
test_cli.py                  24      1    96%
test_pizza_classes.py        24      1    96%
test_pizza_functions.py      26      1    96%
---------------------------------------------
TOTAL                       167     14    92%~~~~



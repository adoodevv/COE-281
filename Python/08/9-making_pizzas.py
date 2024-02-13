import pizza_module # imports entire module

pizza_module.make_pizza(16, 'pepperoni')
pizza_module.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# syntax: module_name.function_name()

"""
import specific function syntax
from module_name import function_name

Use 'as' to give alias to function
from module_name import function_name as fn
Module can also be given alias

Import all functins in module syntax
from module_name import *
"""
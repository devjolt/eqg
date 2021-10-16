from django.shortcuts import render
from random import randint
from . import ab_ops_with_int_frac_dec_logic
import sys
from gcsemaths import gcsemaths_classes_functions as cf

def list_callable_functions():
    """returns list of all modules in this file
    This function MUST remain in this file to work correctly!
    Used by:
    modulesList
    previousNext
    """
    entireModuleList = []
    for key, value in globals().items():
        if callable(value) and value.__module__ == __name__:
            entireModuleList.append(key)
    return entireModuleList

def a_modules_list():
    return cf.moduleListGen(list_callable_functions(), 'ab_a', 0, 4)

def b_modules_list():
    return cf.moduleListGen(list_callable_functions(), 'ab_b', 0, 4)

def c_modules_list():
    return cf.moduleListGen(list_callable_functions(), 'ab_c', 0, 4)

def d_modules_list():
    return cf.moduleListGen(list_callable_functions(), 'ab_d', 0, 4)

def e_modules_list():
    return cf.moduleListGen(list_callable_functions(), 'ab_e', 0, 4)

def modulesList():#this list is used by views to automatically generate views!
    return cf.moduleListGen(list_callable_functions(), 'a', 0, 1)

for module in ab_ops_with_int_frac_dec_logic.modulesList():#generates every logic function as a view, depending on their required template
    exec(f"def {module}(request):\n\treturn render(request, 'gcsemaths/gcsemathsPaperMarkschemeReveal.html', cf.view_builder('ab_ops_with_int_frac_dec_logic', cf.currentFuncName()))")
    

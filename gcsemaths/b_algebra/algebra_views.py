from django.shortcuts import render
from random import randint
from . import algebra_logic
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

def modulesList():#this list is used by views to automatically generate views!
    return cf.moduleListGen(list_callable_functions(), 'b', 0, 1)

def a_modules_list():
    return cf.moduleListGen(list_callable_functions(), 'ba', 0, 2)

def b_modules_list():
    return cf.moduleListGen(list_callable_functions(), 'bb', 0, 2)

def c_modules_list():
    return cf.moduleListGen(list_callable_functions(), 'bc', 0, 2)

def d_modules_list():
    return cf.moduleListGen(list_callable_functions(), 'bd', 0, 2)

def e_modules_list():
    return cf.moduleListGen(list_callable_functions(), 'be', 0, 2)

def f_modules_list():
    return cf.moduleListGen(list_callable_functions(), 'bf', 0, 2)

for module in algebra_logic.modulesList():#generates every logic function as a view, depending on their required template
    exec(f"def {module}(request):\n\treturn render(request, 'gcsemaths/gcsemathsPaperMarkschemeReveal.html', cf.view_builder('algebra_logic', cf.currentFuncName()))")
    

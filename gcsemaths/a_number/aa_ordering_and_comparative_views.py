from django.shortcuts import render
from random import randint
from . import aa_ordering_and_comparative_logic
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
    return cf.moduleListGen(list_callable_functions(), 'a', 0, 1)

def a_modules_list():
    return cf.moduleListGen(list_callable_functions(), 'aa_a', 0, 4)

def b_modules_list():
    return cf.moduleListGen(list_callable_functions(), 'aa_b', 0, 4)

def c_modules_list():
    return cf.moduleListGen(list_callable_functions(), 'aa_c', 0, 4)

for module in aa_ordering_and_comparative_logic.modulesList():#generates every logic function as a view, depending on their required template
    exec(f"def {module}(request):\n\treturn render(request, 'gcsemaths/gcsemathsPaperMarkschemeReveal.html', cf.view_builder('aa_ordering_and_comparative_logic', cf.currentFuncName()))")
    
#Random question generator
def ordering_and_comparative_random(request):
    whole_list = aa_ordering_and_comparative_logic.modulesList()
    #question_list = [q for q in whole_list if q[3] == 'a' ] unneeded in this function but here for reference...
    selected_question = whole_list[randint(0, len(whole_list)-1)]
    template_dict = cf.view_builder("aa_ordering_and_comparative_logic", selected_question)
    print(selected_question)
    return render(request, "gcsemaths/gcsemathsPaperMarkschemeReveal.html", template_dict)
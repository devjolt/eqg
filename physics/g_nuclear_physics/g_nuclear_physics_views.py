from django.shortcuts import render
from random import randint
from . import gx_nuclear_physics_logic
import sys
from physics import physics_classes_functions as ucf

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

def modulesList():#this list is used by urls to automatically generate paths based on what's in this file
    return ucf.moduleListGen(list_callable_functions(), 'g', 0, 1)


def nuclear_physics_home(request):
    modules = ('gx_a')
    context = {}
    for module in modules:
        context[module] = ucf.url_name_list_from(ucf.moduleListGen(list_callable_functions(), module, 0, 4))
    return render(request, 'physics/g_nuclear_physics.html', context)

def module_shortcut(selected):
    if selected[0:2] == 'gx':
        context = ucf.view_builder('gx_nuclear_physics_logic', selected)
    return context

def random_printable_A_question(request):
    eligible = [i for i in modulesList() if i[-5] == 'p' and i[-3] == 'a']
    selected = eligible[randint(0, len(eligible)-1)]
    return render(request, "physics/printablePaperMSRevealAB.html", module_shortcut(selected))

def random_printable_B_question(request):
    eligible = [i for i in modulesList() if i[-5] == 'p' and i[-2] == 'b']
    selected = eligible[randint(0, len(eligible)-1)]
    return render(request, "physics/printablePaperMSRevealAB.html", module_shortcut(selected))
    
def random_printable_A_section(request):
    eligible = [i for i in modulesList() if i[-5] == 'p' and i[-3] == 'a']
    total_marks = 0
    target_marks = 60
    question_number = 1
    qlist = []
    while total_marks < target_marks:
        context = module_shortcut(eligible[randint(0, len(eligible)-1)])
        total_marks += int(context['marksBase'])
        context['questionNumber'] = question_number
        question_number += 1
        qlist.append(context)
        continue
    return render(request, "physics/printablePaperMSRevealAB.html", {'qlist':qlist})

def random_printable_B_section(request):
    eligible = [i for i in modulesList() if i[-5] == 'p' and i[-2] == 'b']
    total_marks = 0
    target_marks = 25
    question_number = 7
    qlist = []
    while total_marks < target_marks:
        context = module_shortcut(eligible[randint(0, len(eligible)-1)])
        total_marks += int(context['marksBase'])
        context['questionNumber'] = question_number
        question_number += 1
        qlist.append(context)
        continue
    return render(request, "physics/printablePaperMSRevealAB.html", {'qlist':qlist, 'qtype':'multi'})

def random_interactive_A_question(request):
    eligible = [i for i in modulesList() if i[-4] == 'i' and i[-3] == 'a']
    selected = eligible[randint(0, len(eligible)-1)]
    return render(request, "physics/interactiveTypeDragSelectMultiReveal.html", module_shortcut(selected))

def random_interactive_B_question(request):
    eligible = [i for i in modulesList() if i[-4] == 'i' and i[-2] == 'b']
    selected = eligible[randint(0, len(eligible)-1)]
    return render(request, "physics/interactiveTypeDragSelectMultiReveal.html", module_shortcut(selected))

for module in gx_nuclear_physics_logic.modulesList(): #generates every logic function as a view, depending on their required template
    exec(f"def {module}(request):\n\treturn render(request, 'physics/printablePaperMSRevealAB.html', ucf.view_builder('gx_nuclear_physics_logic', ucf.currentFuncName()))")
    

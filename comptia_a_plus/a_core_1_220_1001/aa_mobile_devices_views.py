from django.shortcuts import render
from random import randint
from . import aa_mobile_devices_logic
import sys
from comptia_a_plus import comptia_classes_functions as cf

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

def modulesList():#this list is used by views to automatically generate the names!
    return cf.moduleListGen(list_callable_functions(), 'a', 0, 1)

def groupModulesList():#this list is used by views to automatically generate the names!
    return cf.moduleListGen(list_callable_functions(), 'aq', 0,2)

def test(request):
    return render(request, "comptia_a_plus/comptiaSelectMultiDrag.html", cf.view_builder('aa_mobile_devices_logic', cf.currentFuncName()))

def type_test(request):
    return render(request, "comptia_a_plus/type.html", cf.view_builder('aa_mobile_devices_logic', cf.currentFuncName()))

for module in aa_mobile_devices_logic.modulesList():#generates every logic function as a view, depending on their required template
    exec(f"def {module}(request):\n\treturn render(request, 'comptia_a_plus/comptiaSelectMultiDrag.html', cf.view_builder('aa_mobile_devices_logic', cf.currentFuncName()))")

#I'm not sure what these do...
def aa_mobile_devices_random(request):
    question_list = aa_mobile_devices_logic.modulesList()
    selected_question = question_list[randint(0, len(question_list)-1)]
    template_dict = cf.view_builder("aa_mobile_devices_logic", selected_question)
    print(selected_question)
    return render(request, "comptia_a_plus/comptiaSelectMultiDrag.html", template_dict)

#b laptop screens
def aq_b_laptop_hardware(request):
    whole_list = aa_mobile_devices_logic.modulesList()
    question_list = [q for q in whole_list if q[3] == 'a' ]
    selected_question = question_list[randint(0, len(question_list)-1)]
    template_dict = cf.view_builder("aa_mobile_devices_logic", selected_question)
    print(selected_question)
    return render(request, "comptia_a_plus/comptiaSelectMultiDrag.html", template_dict)

#b laptop screens
def aq_b_mobile_device_screens(request):
    whole_list = aa_mobile_devices_logic.modulesList()
    question_list = [q for q in whole_list if q[3] == 'b' ]
    selected_question = question_list[randint(0, len(question_list)-1)]
    template_dict = cf.view_builder("aa_mobile_devices_logic", selected_question)
    print(selected_question)
    return render(request, "comptia_a_plus/comptiaSelectMultiDrag.html", template_dict)

#c laptop features
def aq_c_mobile_device_features(request):
    whole_list = aa_mobile_devices_logic.modulesList()
    question_list = [q for q in whole_list if q[3] == 'c' ]
    selected_question = question_list[randint(0, len(question_list)-1)]
    template_dict = cf.view_builder("aa_mobile_devices_logic", selected_question)
    print(selected_question)
    return render(request, "comptia_a_plus/comptiaSelectMultiDrag.html", template_dict)

#d types of devices
def aq_d_mobile_devices(request):
    whole_list = aa_mobile_devices_logic.modulesList()
    question_list = [q for q in whole_list if q[3] == 'd' ]
    selected_question = question_list[randint(0, len(question_list)-1)]
    template_dict = cf.view_builder("aa_mobile_devices_logic", selected_question)
    print(selected_question)
    return render(request, "comptia_a_plus/comptiaSelectMultiDrag.html", template_dict)

#e cables
def aq_e_cables(request):
    whole_list = aa_mobile_devices_logic.modulesList()
    question_list = [q for q in whole_list if q[3] == 'e' ]
    selected_question = question_list[randint(0, len(question_list)-1)]
    template_dict = cf.view_builder("aa_mobile_devices_logic", selected_question)
    print(selected_question)
    return render(request, "comptia_a_plus/comptiaSelectMultiDrag.html", template_dict)

#f connectivity
def aq_f_connectivity(request):
    whole_list = aa_mobile_devices_logic.modulesList()
    question_list = [q for q in whole_list if q[3] == 'f' ]
    selected_question = question_list[randint(0, len(question_list)-1)]
    template_dict = cf.view_builder("aa_mobile_devices_logic", selected_question)
    print(selected_question)
    return render(request, "comptia_a_plus/comptiaSelectMultiDrag.html", template_dict)

#g accessories
def aq_g_mobile_device_accessories(request):
    whole_list = aa_mobile_devices_logic.modulesList()
    question_list = [q for q in whole_list if q[3] == 'g' ]
    selected_question = question_list[randint(0, len(question_list)-1)]
    template_dict = cf.view_builder("aa_mobile_devices_logic", selected_question)
    print(selected_question)
    return render(request, "comptia_a_plus/comptiaSelectMultiDrag.html", template_dict)

#h connections
def aq_h_connections(request):
    whole_list = aa_mobile_devices_logic.modulesList()
    question_list = [q for q in whole_list if q[3] == 'h' ]
    selected_question = question_list[randint(0, len(question_list)-1)]
    template_dict = cf.view_builder("aa_mobile_devices_logic", selected_question)
    print(selected_question)
    return render(request, "comptia_a_plus/comptiaSelectMultiDrag.html", template_dict)

#i 
def aq_i_(request):
    whole_list = aa_mobile_devices_logic.modulesList()
    question_list = [q for q in whole_list if q[3] == 'i' ]
    selected_question = question_list[randint(0, len(question_list)-1)]
    template_dict = cf.view_builder("aa_mobile_devices_logic", selected_question)
    print(selected_question)
    return render(request, "comptia_a_plus/comptiaSelectMultiDrag.html", template_dict)

#j emails
def aq_j_emails(request):
    whole_list = aa_mobile_devices_logic.modulesList()
    question_list = [q for q in whole_list if q[3] == 'j' ]
    selected_question = question_list[randint(0, len(question_list)-1)]
    template_dict = cf.view_builder("aa_mobile_devices_logic", selected_question)
    print(selected_question)
    return render(request, "comptia_a_plus/comptiaSelectMultiDrag.html", template_dict)

#k synchronisation
def aq_k_Synchronisation(request):
    whole_list = aa_mobile_devices_logic.modulesList()
    question_list = [q for q in whole_list if q[3] == 'k' ]
    selected_question = question_list[randint(0, len(question_list)-1)]
    template_dict = cf.view_builder("aa_mobile_devices_logic", selected_question)
    print(selected_question)
    return render(request, "comptia_a_plus/comptiaSelectMultiDrag.html", template_dict)


'''
What the old views looked like, just in case you ever need them, you silly goose!
def a1qa_what_is_sql(request):
    return render(request, template(), view_builder(cf.currentFuncName()))

#selects a view function at random from moduleList generated list and returns everything needed to generate a view
def select_random(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))
'''
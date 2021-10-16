from django.shortcuts import render
from random import randint
from . import ab_networking_technology_logic
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

def modulesList():#this list is used by urls to automatically generate paths based on what's in this file
    return cf.moduleListGen(list_callable_functions(), 'a', 0, 1)

def groupModulesList():#this list is used by views to automatically generate the names!
    return cf.moduleListGen(list_callable_functions(), 'aq', 0,2)

for module in ab_networking_technology_logic.modulesList():#generates every logic function as a view, depending on their required template
    exec(f"def {module}(request):\n\treturn render(request, 'comptia_a_plus/comptiaSelectMultiDrag.html', cf.view_builder('ab_networking_technology_logic', cf.currentFuncName()))")

def ab_networking_technology_random(request):
    question_list = ab_networking_technology_logic.modulesList()
    selected_question = question_list[randint(0, len(question_list)-1)]
    template_dict = cf.view_builder("ab_networking_technology_logic", selected_question)
    print(selected_question)
    return render(request, "comptia_a_plus/comptiaSelectMultiDrag.html", template_dict)

#a IP basics and ports
def aq_a_IP_basics_and_ports(request):
    whole_list = ab_networking_technology_logic.modulesList()
    question_list = [q for q in whole_list if q[3] == 'a' ]
    selected_question = question_list[randint(0, len(question_list)-1)]
    template_dict = cf.view_builder("ab_networking_technology_logic", selected_question)
    print(selected_question)
    return render(request, "comptia_a_plus/comptiaSelectMultiDrag.html", template_dict)

# b network devices
def aq_b_network_devices(request):
    whole_list = ab_networking_technology_logic.modulesList()
    question_list = [q for q in whole_list if q[3] == 'b' ]
    selected_question = question_list[randint(0, len(question_list)-1)]
    template_dict = cf.view_builder("ab_networking_technology_logic", selected_question)
    print(selected_question)
    return render(request, "comptia_a_plus/comptiaSelectMultiDrag.html", template_dict)

#c SOHO network installation
def aq_c_SOHO_network_installation(request):
    whole_list = ab_networking_technology_logic.modulesList()
    question_list = [q for q in whole_list if q[3] == 'c' ]
    selected_question = question_list[randint(0, len(question_list)-1)]
    template_dict = cf.view_builder("ab_networking_technology_logic", selected_question)
    print(selected_question)
    return render(request, "comptia_a_plus/comptiaSelectMultiDrag.html", template_dict)

#d SOHO network configuration
def aq_d_SOHO_network_configuration(request):
    whole_list = ab_networking_technology_logic.modulesList()
    question_list = [q for q in whole_list if q[3] == 'd' ]
    selected_question = question_list[randint(0, len(question_list)-1)]
    template_dict = cf.view_builder("ab_networking_technology_logic", selected_question)
    print(selected_question)
    return render(request, "comptia_a_plus/comptiaSelectMultiDrag.html", template_dict)

#e 802.11 wireless networks   
def aq_e_wireless_networks(request):
    whole_list = ab_networking_technology_logic.modulesList()
    question_list = [q for q in whole_list if q[3] == 'e' ]
    selected_question = question_list[randint(0, len(question_list)-1)]
    template_dict = cf.view_builder("ab_networking_technology_logic", selected_question)
    print(selected_question)
    return render(request, "comptia_a_plus/comptiaSelectMultiDrag.html", template_dict)

#f cellular networks
def aq_f_cellular_networks(request):
    whole_list = ab_networking_technology_logic.modulesList()
    question_list = [q for q in whole_list if q[3] == 'f' ]
    selected_question = question_list[randint(0, len(question_list)-1)]
    template_dict = cf.view_builder("ab_networking_technology_logic", selected_question)
    print(selected_question)
    return render(request, "comptia_a_plus/comptiaSelectMultiDrag.html", template_dict)

#g network services     
def aq_g_network_services(request):
    whole_list = ab_networking_technology_logic.modulesList()
    question_list = [q for q in whole_list if q[3] == 'g' ]
    selected_question = question_list[randint(0, len(question_list)-1)]
    template_dict = cf.view_builder("ab_networking_technology_logic", selected_question)
    print(selected_question)
    return render(request, "comptia_a_plus/comptiaSelectMultiDrag.html", template_dict)

#h internet protocol     
def aq_h_internet_protocol(request):
    whole_list = ab_networking_technology_logic.modulesList()
    question_list = [q for q in whole_list if q[3] == 'h' ]
    selected_question = question_list[randint(0, len(question_list)-1)]
    template_dict = cf.view_builder("ab_networking_technology_logic", selected_question)
    print(selected_question)
    return render(request, "comptia_a_plus/comptiaSelectMultiDrag.html", template_dict)

#i internet connection types
def aq_i_internet_connection_types(request):
    whole_list = ab_networking_technology_logic.modulesList()
    question_list = [q for q in whole_list if q[3] == 'i' ]
    selected_question = question_list[randint(0, len(question_list)-1)]
    template_dict = cf.view_builder("ab_networking_technology_logic", selected_question)
    print(selected_question)
    return render(request, "comptia_a_plus/comptiaSelectMultiDrag.html", template_dict)

#j network types     
def aq_j_network_types(request):
    whole_list = ab_networking_technology_logic.modulesList()
    question_list = [q for q in whole_list if q[3] == 'j' ]
    selected_question = question_list[randint(0, len(question_list)-1)]
    template_dict = cf.view_builder("ab_networking_technology_logic", selected_question)
    print(selected_question)
    return render(request, "comptia_a_plus/comptiaSelectMultiDrag.html", template_dict)

#k network tools
def aq_k_network_tools(request):
    whole_list = ab_networking_technology_logic.modulesList()
    question_list = [q for q in whole_list if q[3] == 'k' ]
    selected_question = question_list[randint(0, len(question_list)-1)]
    template_dict = cf.view_builder("ab_networking_technology_logic", selected_question)
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
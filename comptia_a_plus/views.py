from django.shortcuts import render
from random import randint
import re
from . import comptia_classes_functions as cf

from .a_core_1_220_1001 import aa_mobile_devices_logic, ab_networking_technology_logic, ac_hardware_logic, ad_virtualisation_cloud_computing_logic, ae_troubleshooting_logic
from .a_core_1_220_1001 import aa_mobile_devices_views, ab_networking_technology_views, ac_hardware_views, ad_virtualisation_cloud_computing_views, ae_troubleshooting_views

def modulesList():#this list is used by urls to automatically generate paths based on what's in this file
    return cf.moduleListGen(list_callable_functions(), 'a', 0, 1)

def home(request):
    a_list = []
    for item in aa_mobile_devices_views.groupModulesList():
        link = item
        name = re.sub('_',' ',item[5:])#make name
        a_list.append({'link':link, 'name':name})
    
    b_list = []
    for item in ab_networking_technology_views.groupModulesList():
        link = item
        name = re.sub('_',' ',item[5:])#make name
        b_list.append({'link':link, 'name':name})
    
    context = {
        'mobile_list': a_list,
        'networking_list': b_list,
        }
    print(context)
    return render(request, "comptia_a_plus/home.html", context)

#selection screen views
def core_1_220_1001(request): 
    return render(request, "comptia_a_plus/core_1_220_1001_home.html")

def core_2_220_1002(request):
    return render(request, "comptia_a_plus/core_2_220_1002_home.html")


def core_1_220_1001_random(request):
    """
    collect a list of logic modules from all logic files and call one of them!
    how to collect list...
    make a list of everything in all logic files
    """
    modules = (
        (aa_mobile_devices_logic,"aa_mobile_devices_logic"),
        (ab_networking_technology_logic, "ab_networking_technology_logic"),
        (ac_hardware_logic, "ac_hardware_logic"),
        (ad_virtualisation_cloud_computing_logic, "ad_virtualisation_cloud_computing_logic"),
        (ae_troubleshooting_logic, "ae_troubleshooting_logic"),
    )
    selection = randint(0, len(modules)-1)
    module, module_name = modules[selection][0], modules[selection][1]
    module_list = module.modulesList()
    selected_function = module_list[randint(0, len(module_list)-1)]
    template_dict = cf.view_builder(module_name, selected_function)
    print(selected_function)
    return render(request, "comptia_a_plus/comptiaExamSelectMultiDrag.html", template_dict)


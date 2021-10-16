from django.shortcuts import render
from random import randint
import re
from gcsemaths import gcsemaths_classes_functions as cf

from gcsemaths.a_number import aa_ordering_and_comparative_logic, ab_ops_with_int_frac_dec_logic
from gcsemaths.a_number import aa_ordering_and_comparative_views, ab_ops_with_int_frac_dec_views

from gcsemaths.b_algebra import algebra_logic, algebra_views
from gcsemaths.e_geometry_and_measure import e_geometry_and_measure_logic, e_geometry_and_measure_views

def name_link_list_from(module_list):
    link_name = []
    for item in module_list:
        link = item
        name = re.sub('_',' ',item[5:])#make name
        name = name[:-2] + ' (level ' + name[-1] + ')'
        link_name.append({'link':link, 'name':name})
    return link_name

def home(request):#GCSE maths home page with access to other views
   

    return render(request,"gcsemaths/home.html")

def home_number(request):
    context = {
        'ordering_values': name_link_list_from(aa_ordering_and_comparative_views.a_modules_list()),
        'comparative_ops': name_link_list_from(aa_ordering_and_comparative_views.b_modules_list()),
        'odd_even_prime': name_link_list_from(aa_ordering_and_comparative_views.c_modules_list()),
        'basic_ops_whole_numbers': name_link_list_from(ab_ops_with_int_frac_dec_views.a_modules_list()), 
        'basic_ops_tens_units': name_link_list_from(ab_ops_with_int_frac_dec_views.b_modules_list()),
        'ops_neg_numbers': name_link_list_from(ab_ops_with_int_frac_dec_views.c_modules_list()), 
        'basic_ops_decimals': name_link_list_from(ab_ops_with_int_frac_dec_views.d_modules_list()),
        'basic_ops_fractions': name_link_list_from(ab_ops_with_int_frac_dec_views.e_modules_list()),
    }
    return render(request,"gcsemaths/a_number_home.html", context)

def home_algebra(request):
    context = {
        'basics': name_link_list_from(algebra_views.a_modules_list()),
        'brackets': name_link_list_from(algebra_views.b_modules_list()),
        'powers_indices':name_link_list_from(algebra_views.c_modules_list()),
        'advanced_powers_indices':name_link_list_from(algebra_views.d_modules_list()),
        'surds':name_link_list_from(algebra_views.e_modules_list()),
        'solving_equations':name_link_list_from(algebra_views.f_modules_list()),
    }
    return render(request,"gcsemaths/b_algebra_home.html", context)

def home_geometry(request):
    context = {
        #ea
        'angles_basics': name_link_list_from(e_geometry_and_measure_views.a_a_list()),
        'angles_around_lines':name_link_list_from(e_geometry_and_measure_views.a_b_list()),
        'angle_problems':name_link_list_from(e_geometry_and_measure_views.a_c_list()),
        #eb
        'polygons':name_link_list_from(e_geometry_and_measure_views.b_a_list()),
        'circles':name_link_list_from(e_geometry_and_measure_views.b_b_list()),
        'circle_problems':name_link_list_from(e_geometry_and_measure_views.b_c_list()),
        #ec
        'congruency':name_link_list_from(e_geometry_and_measure_views.c_a_list()),
        'similarity':name_link_list_from(e_geometry_and_measure_views.c_b_list()),
        'similarity_congruency_problems':name_link_list_from(e_geometry_and_measure_views.c_c_list()),
        #ed
        'area_triangles_quadrilaterals':name_link_list_from(e_geometry_and_measure_views.d_a_list()),
        'area_circles':name_link_list_from(e_geometry_and_measure_views.d_b_list()),
        'surface_area':name_link_list_from(e_geometry_and_measure_views.d_c_list()),
        'volume':name_link_list_from(e_geometry_and_measure_views.d_d_list()),
    }
    return render(request,"gcsemaths/e_geometry_home.html", context)

def home_exam_non_calc(request):
    return render(request, "gcsemaths/home.html")

def number_random(request):
    """
    collect a list of logic modules from all logic files and call one of them!
    how to collect list...
    make a list of everything in all logic files
    """
    modules = (
        (aa_ordering_and_comparative_logic,"aa_ordering_and_comparative_logic"),
        (ab_ops_with_int_frac_dec_logic, "ab_ops_with_int_frac_dec_logic"),
    )
    selection = randint(0, len(modules)-1)
    module, module_name = modules[selection][0], modules[selection][1]
    module_list = module.modulesList()
    selected_function = module_list[randint(0, len(module_list)-1)]
    template_dict = cf.view_builder(module_name, selected_function)
    print(selected_function)
    return render(request, "gcsemaths/gcsemathsPaperMarkschemeReveal.html", template_dict)

def algebra_random(request):
    """
    collect a list of logic modules from all logic files and call one of them!
    how to collect list...
    make a list of everything in all logic files
    """
    module, module_name = algebra_logic, 'algebra_logic'
    module_list = module.modulesList()
    selected_function = module_list[randint(0, len(module_list)-1)]
    template_dict = cf.view_builder(module_name, selected_function)
    print(selected_function)
    return render(request, "gcsemaths/gcsemathsPaperMarkschemeReveal.html", template_dict)

def geometry_random(request):
    """
    collect a list of logic modules from all logic files and call one of them!
    how to collect list...
    make a list of everything in all logic files
    """
    module, module_name = e_geometry_and_measure_logic, 'e_geometry_and_measure_logic'
    module_list = module.modulesList()
    selected_function = module_list[randint(0, len(module_list)-1)]
    template_dict = cf.view_builder(module_name, selected_function)
    print(selected_function)
    return render(request, "gcsemaths/gcsemathsPaperMarkschemeReveal.html", template_dict)

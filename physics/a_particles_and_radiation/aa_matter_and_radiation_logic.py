from django.shortcuts import render
from random import randint, randrange
from physics import physics_classes_functions as cf
from physics import variety_lists as vl

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

def module_path():
    return '/physics/particles_and_radiation/'

def generateAtom():
    table = [[1, 'n', 0], [1, 'H', 1], [4, 'He', 2], [7, 'Li', 3], [9, 'Be', 4], [11, 'B', 5], [12, 'C', 6], [14, 'N', 7], [16, 'O', 8], [19, 'F', 9], [20, 'Ne', 10], [23, 'Na', 11], [24, 'Mg', 12], [27, 'Al', 13], [28, 'Si', 14], [31, 'P', 15], [32, 'S', 16], [35, 'Cl', 17], [40, 'Ar', 18], [39, 'K', 19], [40, 'Ca', 20], [45, 'Sc', 21], [48, 'Ti', 22], [51, 'V', 23], [52, 'Cr', 24], [55, 'Mn', 25], [56, 'Fe', 26], [59, 'Co', 27], [59, 'Ni', 28], [64, 'Cu', 29], [65, 'Zn', 30], [70, 'Ga', 31], [73, 'Ge', 32], [75, 'As', 33], [79, 'Se', 34], [80, 'Br', 35], [84, 'Kr', 36], [85, 'Rb', 37], [88, 'Sr', 38], [89, 'Y', 39], [91, 'Zr', 40], [93, 'Nb', 41], [96, 'Mo', 42], [98, 'Tc', 43], [101, 'Ru', 44], [103, 'Rh', 45], [106, 'Pd', 46], [108, 'Ag', 47], [112, 'Cd', 48], [115, 'In', 49], [119, 'Sn', 50], [122, 'Sb', 51], [128, 'Te', 52], [127, 'I', 53], [131, 'Xe', 54], [133, 'Cs', 55], [137, 'Ba', 56], [139, 'La', 57], [140, 'Ce', 58], [141, 'Pr', 59], [144, 'Nd', 60], [145, 'Pm', 61], [150, 'Sm', 62], [152, 'Eu', 63], [157, 'Gd', 64], [159, 'Tb', 65], [162, 'Dy', 66], [165, 'Ho', 67], [167, 'Er', 68], [169, 'Tm', 69], [173, 'Yb', 70], [175, 'Lu', 71], [178, 'Hf', 72], [181, 'Ta', 73], [184, 'W', 74], [186, 'Re', 75], [190, 'Os', 76], [192, 'Ir', 77], [195, 'Pt', 78], [197, 'Au', 79], [201, 'Hg', 80], [204, 'Tl', 81], [207, 'Pb', 82], [209, 'Bi', 83], [209, 'Po', 84], [210, 'At', 85], [222, 'Rn', 86], [223, 'Fr', 87], [226, 'Ra', 88], [227, 'Ac', 89], [232, 'Th', 90], [231, 'Pa', 91], [238, 'U', 92], [237, 'Np', 93], [244, 'Pu', 94], [243, 'Am', 95], [247, 'Cm', 96], [247, 'Bk', 97], [251, 'Cf', 98], [252, 'Es', 99], [257, 'Fm', 100], [258, 'Md', 101], [259, 'No', 102], [262, 'Lr', 103], [261, 'Rf', 104], [262, 'Db', 105], [266, 'Sg', 106], [264, 'Bh', 107], [277, 'Hs', 108], [268, 'Mt', 109], [281, 'Ds', 110], [272, 'Rg', 111], [285, 'Cn', 112], [286, 'Nh', 113], [289, 'Fl', 114], [289, 'Mc', 115], [293, 'Lv', 116], [294, 'Ts', 117], [294, 'Og', 118]]
    nucleus = table[randint(0,118)]
    proton = nucleus[2]
    element = nucleus[1]
    mass = nucleus[0]
    neutron = nucleus[0] - nucleus[2]
    massNumber = str(mass)
    SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
    atom = f"{mass}{element}{proton}".translate(SUP)
    return atom, mass, element, proton

def electronCharge():
    return 1.6E-19

def nucleonMass():
    return 1.67e-27

'''
multiple questions?
we need to imitate how an exam paper looks. 

default is question base:
questiona
questionb
questionc
questiond

drag and drop (match)

type the answer?

multiple choice sections...

'''

def x_short_long_display():
    q = cf.Question()
    q.questionNumber = 1
    q.questionBase = 'stuff'
    #list of dictionaries containing: sub_number, sub_question, sub_answer, sub_mark
    q.questionPartList = [
        {'sub_number': 1, 'sub_question':'and another things', 'sub_answer':'is this', 'sub_mark':1},
        {'sub_number': 2, 'sub_question':'and another thingsadf', 'sub_answer':'is thisasdf', 'sub_mark':2},
        {'sub_number': 3, 'sub_question':'and another thingsgh', 'sub_answer':'is thisgh', 'sub_mark':3},
        {'sub_number': 4, 'sub_question':'and another thingfgh', 'sub_answer':'is thishgfhg', 'sub_mark':4},
    ]
    q.marksBase = 10
    q.answerBase = 'things'
    q.qtype = 'parts'
    return q.returnAll()

def x_multi_display():
    correct = ('correct1', 'correct2')
    incorrect = ('incorrect1', 'incorrect2', 'incorrect3', 'incorrect4')
    fillers = ('filler1', 'filler2')
    #qtype = multi|select|drag, correct = [], incorrect = [], pairs = [[]], fillers = [], marks, correctRequired, numOptions
    q = ucf.SelectMcDrag('multi', correct, incorrect, None, fillers, 1, 1, 4)
    q.questionNumber = 1
    q.questionBase = 'Pick the right one or you will be silly!'
    #list of dictionaries containing: sub_number, sub_question, sub_answer, sub_mark
    return q.returnAll()

'''
ab_cb_title_piab1
where
a indicates module
b indicates topic
c indicates sub-topic
d indicates question

the following can be either the named letter to indicate elligibility as a certain question type
OR x to indicate inelligibility

p - printable
i - interactive
a - section a question
b - section b question
a - number of marks the question is worth
'''

def aa_aa_Counting_protons_and_neutrons_pxax2():
    q = cf.Question(cf.currentFuncName())
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    atom, mass, element, proton = generateAtom()    
    q.questionBase = f"{atom}"
    question1 = "How many protons in the above nucleus?"
    answer1 = f"{proton}"
    question2 = "How many neutrons in the above nucleus?"
    answer2 = f"{mass-proton}"
    q.questionPartList = [
       {'sub_number': 1, 'sub_question': question1, 'sub_answer': answer1, 'sub_mark': 1}, 
       {'sub_number': 2, 'sub_question': question2, 'sub_answer': answer2, 'sub_mark': 1}, 
    ]
    return q.returnAll()

def aa_ab_Naming_parts_of_the_atom_piab1():
    q = cf.Question(cf.currentFuncName())
    q.qtype = 'type'
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    answers = [["neutron",["have zero charge", "has the largest mass", "when removed create a different isotope"]],
           ["proton", ["have positive charge", "has second to largest mass", " have the second to largest specific charge", "dictate what element an atom is"]],
           ["electron", ["have negative charge", "has the highest specific charge", "dictate whether the atom is an ion"]]]
    nuclide = randint(0, len(answers)-1)
    qu = randint(0, len(answers[nuclide][1])-1)
    q.questionBase = f'Name the sub-atomic particle in the atom which {answers[nuclide][1][qu]}.'
    q.answerBase= f'{answers[nuclide][0]}'
    q.constant = None
    return q.returnAll()

def aa_ac_Ionised_atoms_and_specific_charge_pxax6():
    q = cf.Question(cf.currentFuncName())
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    atom, mass, element, proton = generateAtom()   
    losesGains = "loses" if randint(0,1)==0 else "gains"
    electrons = randint(1,4)
    electron = -electrons if losesGains == "loses" else electrons
    q.questionBase = f"An {atom} atom {losesGains} {electrons} electrons."
    question1 = "What is the charge of the atom in Coulombs?"
    answer1= f"{(-electron * electronCharge())} C"
    question2 = "State the number of nucleons the atom contains."
    answer2 = f"{mass}"
    question3 = "Calculate its specific charge in Ckg-1."
    specificCharge = round((-electron * float(electronCharge())) / (mass * float(nucleonMass())), 2)
    if specificCharge < 0: specificCharge *= -1
    answer3 = f"{specificCharge}"
    q.questionPartList = [
       {'sub_number': 1, 'sub_question': question1, 'sub_answer': answer1, 'sub_mark': 2}, 
       {'sub_number': 2, 'sub_question': question2, 'sub_answer': answer2, 'sub_mark': 1}, 
       {'sub_number': 3, 'sub_question': question3, 'sub_answer': answer3, 'sub_mark': 3}, 
    ]
    return q.returnAll()
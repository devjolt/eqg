from django.shortcuts import render
from random import randint
from fractions import Fraction
from decimal import Decimal
from gcsemaths import gcsemaths_classes_functions as cf
#from gcsemaths import variety_lists as vl

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
    return '/gcsemaths/a_number/'

def ab_aa_add_units_tens_11():
    q = cf.QuestionInteger(cf.currentFuncName(),2,9,10,99,'+',1)
    q.answerBase = q.answer
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()

def ab_ab_subtract_units_tens11():
    q = cf.QuestionInteger(cf.currentFuncName(),2,9,10,99,'-',1)
    q.answerBase = q.answer
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()

def ab_ac_multiply_units_tens13():
    q = cf.QuestionInteger(cf.currentFuncName(),2,9,10,99,'*',1)
    q.answerBase = q.answer
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()

def ab_ad_divide_units_tens13():
    q = cf.QuestionInteger(cf.currentFuncName(),10,99,2,9,'/',1)
    q.answerBase = f"{q.x//q.y} remainder {q.x % q.y}"
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()

def ab_ae_random_integers13():
    q = cf.QuestionInteger(cf.currentFuncName(),10,100,10,100,'/',1)
    q.op = q.opSetup(0,3)
    q.answerBase = q.answer
    if q.op == '/': q.answerBase = f"{round(eval(q.questionBase))} remainder {q.x % q.y}"
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()

def ab_ba_add_tens_hundreds11():
    q = cf.QuestionInteger(cf.currentFuncName(),10,99,100,999,'+',1)
    q.answerBase = q.answer
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()

def ab_bb_sub_tens_hundreds_11():
    q = cf.QuestionInteger(cf.currentFuncName(),10,99,110,999,'-',1)
    q.answerBase = q.answer
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()

def ab_bc_add_sub_tens_hundreds_11():
    q = cf.QuestionInteger(cf.currentFuncName(),10,99,110,999,'-',1)
    q.op = q.opSetup(0,1)
    q.answerBase = q.answer
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()

def ab_bd_multiply_tens_hundreds13():
    q = cf.QuestionInteger(cf.currentFuncName(),100,999,10,99,'*',1)
    q.answerBase = q.answer
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()

def ab_be_divide_tens_hundreds13():
    q = cf.QuestionInteger(cf.currentFuncName(),100,999,10,30,'/',1)
    q.answerBase = f"{q.x//q.y} remainder {q.x % q.y}"
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()

def ab_bf_multiply_divide_ten_hundreds_random13():
    q = cf.QuestionInteger(cf.currentFuncName(),10,99,100,999,'-',1)
    q.op = q.opSetup(2,3)
    q.answerBase = q.answer
    if q.op == '/': q.answerBase = f"{q.x//q.y} remainder {q.x % q.y}"
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()

def ab_ca_negative_add_units_tens13():
    q = cf.QuestionInteger(cf.currentFuncName(),-9,-1,10,100,'+',1)
    q.answerBase = q.answer
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()

def ab_cb_negative_add_tens_hundreds13():
    q = cf.QuestionInteger(cf.currentFuncName(),100,999,-99,10,'+',1)
    q.answerBase = q.answer
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()

def ab_cc_negative_subtract_units_tens13():
    q = cf.QuestionInteger(cf.currentFuncName(),10,100,-9,-2,'-',1)
    q.answerBase = q.answer
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()

def ab_cd_negative_subtract_tens_hundreds13():
    q = cf.QuestionInteger(cf.currentFuncName(),100,999,-99,-10,'-',1)
    q.answerBase = q.answer
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()

def ab_ce_negative_add_sub_integers13(): 
    q = cf.QuestionInteger(cf.currentFuncName(),-999,999,-99,99,'-',1)
    q.op = q.opSetup(0,1)
    q.answerBase = q.answer
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()

def ab_cf_negative_multiply_units_tens13():
    q = cf.QuestionInteger(cf.currentFuncName(),2,9,-99,-10,'*',1)
    q.answerBase = q.answer
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()

def ab_cg_negative_multiply_tens_hundreds13():
    q = cf.QuestionInteger(cf.currentFuncName(),10,99,-999,-10,'*',1)
    q.answerBase = q.answer
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()

def ab_ch_negative_divide_units_tens13():
    q = cf.QuestionInteger(cf.currentFuncName(),-99,-10,2,9,'/',1)
    q.answerBase = f"{q.x//q.y} remainder {q.x % q.y}"
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()

def ab_ci_negative_divide_tens_hundreds13():
    q = cf.QuestionInteger(cf.currentFuncName(),-999,-100,10,99,'/',1)
    q.answerBase = f"{q.x//q.y} remainder {q.x % q.y}"
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()

def ab_da_add_sub_decimals24():
    q = cf.QuestionDecimal(cf.currentFuncName(),0,0,0,0,'-',1)
    q.op = q.opSetup(0,1)
    q.answerBase = q.answer
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()

def ab_db_multiply_decimals24():
    q = cf.QuestionDecimal(cf.currentFuncName(),0,0,0,0,'*',1)
    q.answerBase = str(round(float(q.answer), 2))
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()

def ab_dc_divide_decimals24():
    q = cf.QuestionDecimal(cf.currentFuncName(),0,0,0,0,'/',1)
    q.answerBase = str(round(float(q.answer), 2))
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()
    
def ab_dd_random_decimals24():
    q = cf.QuestionDecimal(cf.currentFuncName(),0,0,0,0,'*',1)
    q.opSetup(0,3)
    q.answerBase = str(round(float(q.answer), 2))
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()

def ab_ea_add_sub_fractions24():
    q = cf.QuestionFraction(cf.currentFuncName(),0,0,0,0,'*',1)
    q.opSetup(0,1)
    q.questionBase += " (Give your answer in decimal form)"
    q.answerBase = str(round(float(q.answer), 2))
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()

def ab_eb_multiply_fractions24():
    q = cf.QuestionFraction(cf.currentFuncName(),0,0,0,0,'*',1)
    q.questionBase += " (Give your answer in decimal form)"
    q.answerBase = str(round(float(q.answer), 2))
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()

def ab_ec_divide_fractions24():
    q = cf.QuestionFraction(cf.currentFuncName(),0,0,0,0,'/',1)
    q.divideQuestionAnswer()
    q.answerBase = q.answer
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()

def ab_ed_random_fractions24():
    q = cf.QuestionFraction(cf.currentFuncName(),0,0,0,0,'*',1)
    q.opSetup(0,3)
    if q.op =='/': q.divideQuestionAnswer()
    q.questionBase += " (Give your answer in decimal form)"
    q.answerBase = str(round(float(q.answer), 2))
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()

def ab_ee_add_sub_mixed_fractions24():
    q = cf.QuestionMixedFraction(cf.currentFuncName(),0,0,0,0,'*',1)
    q.opSetup(0,1)
    q.questionBase += " (Give your answer in decimal form)"
    q.answerBase = str(round(float(q.answer), 2))
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()

def ab_ef_multiply_mixed_fractions24():
    q = cf.QuestionMixedFraction(cf.currentFuncName(),0,0,0,0,'*',1)
    q.opSetup(0,1)
    q.questionBase += " (Give your answer in decimal form)"
    q.answerBase = str(round(float(q.answer), 2))
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()

def ab_ee_decimal_as_fraction24():
    q = cf.Question(cf.currentFuncName())
    denOptions = [2,4,5,6,8,10,12,15,20]
    den = denOptions[randint(0,len(denOptions)-1)]
    num = randint(1,den-1)
    decimal = round(num/den, 5)
    q.questionBase = (f"Write {decimal} as a fraction")
    q.answerBase = (Fraction(f"{num}/{den}"))
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()

def ab_ef_fraction_as_decimal24():
    q = cf.Question(cf.currentFuncName())
    denOptions = [2,4,5,6,8,10,12,15,20]
    den = denOptions[randint(0,len(denOptions)-1)]
    num = randint(1,den-1)
    decimal = round(num/den, 5)
    frac = Fraction(f"{num}/{den}")
    q.questionBase = (f"Write {frac} as a decimal")
    q.answerBase = f"{decimal}"
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()
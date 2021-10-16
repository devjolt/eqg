from django.shortcuts import render
from random import randint, randrange
from fractions import Fraction
from decimal import Decimal
import sys
import math

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
    return cf.moduleListGen(list_callable_functions(), 'e', 0, 1)

def module_path():
    return '/gcsemaths/e_geometry/'

def triangle():
    shape_list = ["https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fs-media-cache-ak0.pinimg.com%2F564x%2Fe4%2F33%2F53%2Fe433536f48dbb7624afe948d118a4bcd.jpg&f=1&nofb=1","https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fmemegenerator.net%2Fimg%2Finstances%2F75884024.jpg&f=1&nofb=1","https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fs-media-cache-ak0.pinimg.com%2Foriginals%2Fd7%2F3f%2F97%2Fd73f97d8d55c5f78027abc9c8af85971.jpg&f=1&nofb=1", "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.imgflip.com%2Fsdp60.jpg&f=1&nofb=1", "https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fi0.kym-cdn.com%2Fphotos%2Fimages%2Fnewsfeed%2F000%2F403%2F150%2Fb01.png&f=1&nofb=1", "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse2.mm.bing.net%2Fth%3Fid%3DOIP.Xdw7ITdnQcHst926igzqrgHaHa%26pid%3DApi&f=1", "http://undergrad.osu.edu/buckeyes_blog/wp-content/uploads/2015/10/1.jpg", "https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fwww.dumpaday.com%2Fwp-content%2Fuploads%2F2016%2F01%2Ffunny-pictures-144.jpg&f=1&nofb=1"]
    return shape_list[randint(0,len(shape_list)-1)]

def parallelogram():
    shape_list = ["https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fpics.onsizzle.com%2Fparallelogram-a-parallelogram-is-a-rectangle-that-just-cannot-today-18734770.png&f=1&nofb=1", "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fpics.me.me%2Fquadrilaterals-perimeter-name-the-quadrilateral-bo-on-name-hole-rectangle-7221385.png&f=1&nofb=1", "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fs-media-cache-ak0.pinimg.com%2F736x%2F23%2F51%2F16%2F23511668497135cace929da12fb69acf.jpg&f=1&nofb=1"]
    return shape_list[randint(0,len(shape_list)-1)]

def trapezium():
    shape_list = ("https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fi2.kym-cdn.com%2Fphotos%2Fimages%2Ffacebook%2F000%2F439%2F553%2F48f.png&f=1&nofb=1","https://img00.deviantart.net/4624/i/2006/115/3/5/quarrel_of_quadrilaterals_by_cynosura.jpg", "https://pics.me.me/applic-as-a-head-shaped-li-a-trapezoid-11050166.png","https://pics.onsizzle.com/improtant-don-t-spill-trapezoids-on-yorr-existence-cake-my-cousin-29574757.png","http://www.kappit.com/img/pics/201603_2331_ecidi_sm.jpg","https://pics.me.me/barber-what-do-you-want-supreme-leader-him-hit-me-16614478.png","https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fs-media-cache-ak0.pinimg.com%2F736x%2F4e%2F60%2F17%2F4e6017f46f6dbeeaa13db07c38ec1a51.jpg&f=1&nofb=1","https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fwww.kappit.com%2Fimg%2Fpics%2F19527281cdhaf_sm.jpg&f=1&nofb=1", "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fpics.onsizzle.com%2Fits-a-trapezoid-9001383.png&f=1&nofb=1")
    return shape_list[randint(0,len(shape_list)-1)]

def completePeopleGen():
    he = ["Bob", "Alfred", "Batman", "Borris Johnson", "Donald Trump", "Jeremy Corbyn", "Spongebob Squarepants", "Rick Astley", "Napoleon", "Bob Marley","Jacob Marley"]
    she = ["Madonna", "She-Ra", "Superwoman", "Applejack", "Theresa May", "Elsa", "Anna"]
    choice = randint(0,1)
    if choice == 0: return "he", he[randint(0,len(he)-1)]
    if choice == 1: return "she", she[randint(0,len(she)-1)]

def letterGen(low = 1, high = 26):
    return chr(randint(96+low, 96+high))

def eselect_random():
    modList = cf.moduleListGen("e",0, 1)
    print(modList)
    return eval(f"{modList[randint(0,len(modList)-1)]}()")

def egeometry_basics_random():
    modList = cf.moduleListGen("ea_a", 0, 4)
    print(modList)
    return eval(f"{modList[randint(0,len(modList)-1)]}()")

def egeometry_parallel_random():
    modList = cf.moduleListGen("ea_b", 0, 4)
    return eval(f"{modList[randint(0,len(modList)-1)]}()")

def egeometry_problems_random():
    modList = cf.moduleListGen("ea_c", 0, 4)
    return eval(f"{modList[randint(0,len(modList)-1)]}()")


#previousQ, nextQ, diagram, constant, questionBase, answer, pre, preans, marks, level, , video

def ea_aa_angles_in_triangle_no_diagram13():
    a = [letterGen(1,10), 40 + randint(0, 40)]
    b = [letterGen(11,18), 40 + randint(0, 40)]
    c = [letterGen(19, 26), 180 - a[1] - b[1]]
    questionBase = [
        f"'{a[0]}{b[0]}{c[0]}', '{c[0]}{a[0]}{b[0]}' and '{b[0]}{c[0]}{a[0]}' are three angles in a triangle.",
        f"If '{a[0]}{b[0]}{c[0]}' is {b[1]}\u00B0 and '{c[0]}{a[0]}{b[0]}' is {a[1]}\u00B0, what is the value of '{b[0]}{c[0]}{a[0]}'?"]
    answer = f"{c[1]}\u00B0"
    q = cf.Question(cf.currentFuncName())
    q.questionBase, q.answerBase = questionBase, answer
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()
    
def ea_ab_angles_in_triangle_diagram13():
    a = ['x', 40 + randint(0, 40)]
    b = ['y', 40 + randint(0, 40)]
    c = ['z', 180 - a[1] - b[1]]
    questionBase = f"Find the value of {c[0]} if {a[0]} = {a[1]}\u00B0 and {b[0]} = {b[1]}\u00B0"
    answer = f"{c[1]}\u00B0"
    q = cf.Question(cf.currentFuncName())
    q.questionBase, q.answerBase = questionBase, answer
    q.piclink = 'https://lh3.googleusercontent.com/rNITotcn9-R6bSbBjSU-IhDRigEyU2xgNN63TjKIe42CXNUoQNbFsXJoVEuPqXuGRPKZR7XehYbyGD4GY4UVPM7JuZJ_OBl5nOb_tYSc-2wzcpKxaFE6Mzv_GpT6F8OJpvPaS2N9T40ut1e6kT4bPDC4Gfk8kbmaEViZKCYIt_w69e8Wt7NOYb3f1UOpb9_CvIFDEhlh-sQG2ANXPpQq3D3cyF6PXmclJ1qEsQmwEpUor-xxe5OJT69NCko0gyELTwzDtCae8VISRLUq_E3FBdXsCe9nknZZLDRL_LseaWhdKv1LvGFNVb_AvAWHpUHJh6sKwOgng3gHKKQVuoN7GZWXtbIpbT1yhNaCCHbLZYEM0Rd1T-FkSmJlkEs7-ISblCN8IV3tk05cqukclGHpbUvQpuIBqE4NFUATvEQ5m0iuZn02T_pKEaoJqMJ270XeMY-GzUIE4jkUNDmO16LjcTenY2MldgOL3trsOiQKnWgWDTe8sdXHUJTaE20IAMm6zPzRtJLuZBYjKjVRsfYlMfVYMjkh5naSUJ-6v6kZUqAmvyztzAe1xD8XU9er-TNOKPWWFhmQlT_WkcrrbSEVeUruOz5k8PRgD81G2S_OBYBCZR8G_9Hxz6-vk8t7sipzd8Ko18CcrrA_daoNyTC7rIs1dvLiKxloAkABfFkmInmSR-weeRfPrgPWXgJfgG2E3nGf8zjisv0Niw8VSPdrLVfh=w1280-h720-no?authuser=0'
    #q.diagram = '/diagrams/gcsemaths/triangle_scalene_xyz.jpg'
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()
    
def ea_ac_angles_on_straight_line_diagram13():
    a = ['x', 40 + randint(0, 40)]
    b = ['y', 40 + randint(0, 40)]
    c = ['z', 180 - a[1] - b[1]]
    q = cf.Question(cf.currentFuncName())
    q.questionBase = f"Find the value of {c[0]} if {a[0]} = {a[1]}\u00B0 and {b[0]} = {b[1]}\u00B0"
    q.answerBase = f"{c[1]}\u00B0"
    q.piclink = 'https://lh3.googleusercontent.com/Q8Zv-46k68DguPA6TwV3rd-RwD9GEHFhDuX3pVWL-c2E7glq8zVkUyDMRrMIVcw3lZpqNQjs2YsC4EryJ4KFdUBz9I8yIaCT6GwugihSSjR4zKlk8iXUMHa8PxcdnSeozzZ4a3WndhtzmHd09weVvK8ppcbxcq_1hzjfM3-uKWvOQWl1mQEBH5IL-nvmqh0cq6L16NXQv2rjzR29XAbXOaiDH05jjs14RhE_OUi7CYWCQjGiuLSwkiFCQS7zVZoByS3dl8eUbt_m1BzZG_pWVQP05wWlzm8R3koxx6W4VjlPegShsthoLp6EDrVzzKgXDUKOnbVkEx5_U72cYzRL6FEFGPQpT9hM2MlzHbmsxC_8RbMZmlXQscMQwYZ5zX8yIBXU8_eLa2QZ3EKNaavHHyHwU4oP2Ps9E_bgfjuL5a1p2Tvmj5amd4TTHNdUT7J4o6ruKoqSGAijyDvxSirc4_gzw4goG9sZdPICDr_PgffngSvzJiylGzChmZwaAWrsLJC5TBsQx4izg6RzAixivWeSnYHJVJ1ZDHXyQu7_25TOBkTvfxO5k9c8M5176RY2iQJut4ezR-zCfdylMy1O4kfLNRPAeIIwm1xwLkhAGckwBONZsuOzPCQU77s3CKqjm0NMrGtjZ1RnyP1y06Q_ipIxrVcZMQqIiOC9L6ksFH_M-mpLu2F3-tfvrCzDGkn7ALgPajMJo7A7a3SssaPC_r7H=w1280-h720-no?authuser=0'
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()
    
def ea_ad_angles_in_quadrilateral_diagram13():
    a = ['k', 50 + randint(0, 40)]
    b = ['l', 50 + randint(0, 40)]
    c = ['m', 50 + randint(0, 40)]
    d = ['n', 360 - a[1] - b[1] - c[1]]
    q = cf.Question(cf.currentFuncName())
    q.questionBase = [f"{a[0]} = {a[1]}\u00B0, {b[0]} = {b[1]}\u00B0, {c[0]} = {c[1]}\u00B0.", "Find the value of the angle at x"]
    q.answerBase = f"{d[1]}\u00B0"
    q.piclink = 'https://lh3.googleusercontent.com/mCzhkLUkBe9Zw66SEYidH8DkMGFO5i1S6JL4idUhzzeLzqSpNeXnuswHwsjmDCbD8u5Ma5ayBuo86rVigvHrhPhieckupHu6I0kDOawC0OgUGRYyXu97YbeYlq_A0Qnp98mWeu51dbknswPdjeQ7NjpA4seni6wMweplQrTiXLYIbYq-VnH70tROoedaRcaomdgMPq6oeqjGHIvO4C3-lKZROGFcdiTiGXWTJaVwwTHWa162fYTzoW4s60zWuxUePhY6wm51hiEr2F8arbXCJ7bKgtt9cZGHcTFB6Ix5RAOfm2hIG1xuN-jb1TJH-5Lv8GKkIlbgtAEpaiw6sTIpe8hx0hwGzyPxOuaEN9RQFJBE2xt69P2DWEcYd9aCZomM8Bc55PjIx2ptpZzViXs_lAvL9gRHRETTUFxX0_b0QMF8JiFcpJhXgnUjyegBSXuJ38h8XyygDVaFpehhS15dNwl3J7E4YTRUlZr-853tI4nJleCH1DmEquNTcte5bgxONAfAgoeDTVtukmCeDz6KVS1rSmhWJ26cfvh2VDd0H0wJ6bUi7xq_Cx7OFmyjZS_7ASG920Iyrbm95cNaVltOATgNBy2nmWVHeNmvjqJDAh-XM40goas9bEGDhuO_9VV6D9RPtERqfs9rxTz_lNSDp6XEqPU5oWJtWNMq1g0uktwXODs5ASbXrdy_T0HQ56kC_gvBViT1RA7DHwXCx_wgRSUh=w773-h435-no?authuser=0'
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()
    
def ea_ae_angles_in_isosceles_triangle_diagram13():
    a = ['a', 40 + randint(0, 40)]
    b = ['b', a[1]]
    c = ['c', 180 - (a[1]*2)]
    q = cf.Question(cf.currentFuncName())
    q.questionBase = [f"{a[0]} = {a[1]}\u00B0, {b[0]} = {b[1]}\u00B0.","Find the value of the angle at c"]
    q.answerBase = f"{c[1]}\u00B0"
    q.piclink = 'https://lh3.googleusercontent.com/Mk-Tkw1Gyt_iZ-TaR0If_-OxuBMoU_c1G3geYIyTyRZZPiTBrFt_EL4EaPQnzfQUspJgLgWo01Pe6OL4WlEz9ziWHb28n3rCvoq8tP3mfzXoz3H06iqmPvv-oCJ9DeFWo7mt10fFw7VFOGrwIQHrEOjnKVpxzUG6WrNcG_OzjkLlssprBkgtCyhj8GpMZSdSQSjpo9G7ieJvnUpuCgeErGPg8VO5TbyOX8zrdllt3OvcLLTzAx0cG1rcdMY5pl0jeJCHPT08KwRH29O53IShcShxXSGflaCJZ4K082EjSVrmLLl8E3S9wglNK2CWhli0jM5GAjKUQ9jRwLlg7QcT8Jj2PKsgfqPGNVhZ5v1rdNt9Z4e9sWDulea5z3_aSGYni6pcYj67Ih7USBT_0whm2saW4Caj0amI6eH4HCZ8SoDuEPOobuWjV5wb-2Rh_J8K3QDPS3YJ867EtNLeIB3YFcyNQ3_MVEo8nloF3pHP_HyU_sLpz7jd-RqtF_-ScMIozDLH8Uf6xqRL9-6LByrXoZDrYzd-PGfw4Fya8ap4KW5THZfkbWoV6bxBUU1P18IhrpErahJ9692B77SLXKRbuPt9F4p1BZzmq7zxWa-3AI-r8olYJjuPh__7Cooh2lkFkyYuVDATwD3sYycq7M8nkevhodReOaP0c_7usIHJikry9IeoicuIxtvDTGLIIqMKNVC4iEEeqzyyedM_PGdytwuR=w1280-h720-no?authuser=0'
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()
    
def ea_af_isosceles_triangle_pair_known_diagram13():
    a = ['a', 40 + randint(0, 40)]
    b = ['b', a[1]]
    c = ['c', 180 - (a[1]*2)]
    angle = [a,b,c]
    choice = randint(1,2)
    q = cf.Question(cf.currentFuncName())
    q.questionBase = [f"Angle {a[0]} is {a[1]}\u00B0.",f"What is the value of angle {angle[choice][0]}?"]
    q.answerBase = f"{angle[choice][1]}\u00B0"
    q.piclink = 'https://lh3.googleusercontent.com/Mk-Tkw1Gyt_iZ-TaR0If_-OxuBMoU_c1G3geYIyTyRZZPiTBrFt_EL4EaPQnzfQUspJgLgWo01Pe6OL4WlEz9ziWHb28n3rCvoq8tP3mfzXoz3H06iqmPvv-oCJ9DeFWo7mt10fFw7VFOGrwIQHrEOjnKVpxzUG6WrNcG_OzjkLlssprBkgtCyhj8GpMZSdSQSjpo9G7ieJvnUpuCgeErGPg8VO5TbyOX8zrdllt3OvcLLTzAx0cG1rcdMY5pl0jeJCHPT08KwRH29O53IShcShxXSGflaCJZ4K082EjSVrmLLl8E3S9wglNK2CWhli0jM5GAjKUQ9jRwLlg7QcT8Jj2PKsgfqPGNVhZ5v1rdNt9Z4e9sWDulea5z3_aSGYni6pcYj67Ih7USBT_0whm2saW4Caj0amI6eH4HCZ8SoDuEPOobuWjV5wb-2Rh_J8K3QDPS3YJ867EtNLeIB3YFcyNQ3_MVEo8nloF3pHP_HyU_sLpz7jd-RqtF_-ScMIozDLH8Uf6xqRL9-6LByrXoZDrYzd-PGfw4Fya8ap4KW5THZfkbWoV6bxBUU1P18IhrpErahJ9692B77SLXKRbuPt9F4p1BZzmq7zxWa-3AI-r8olYJjuPh__7Cooh2lkFkyYuVDATwD3sYycq7M8nkevhodReOaP0c_7usIHJikry9IeoicuIxtvDTGLIIqMKNVC4iEEeqzyyedM_PGdytwuR=w1280-h720-no?authuser=0'
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()
    
def ea_ag_isosceles_triangle_single_known_diagram13():
    a = ['a', 40 + randint(0, 40)]
    b = ['b', a[1]]
    c = ['c', 180 - (a[1]*2)]
    angle = [a,b,c]
    choice = randint(0,1)
    questionBase = [f"Angle {c[0]} is {c[1]}\u00B0.", "What is the value of angle b?"]
    answer = f"{a[1]}\u00B0"
    q = cf.Question(cf.currentFuncName())
    q.piclink = 'https://lh3.googleusercontent.com/Mk-Tkw1Gyt_iZ-TaR0If_-OxuBMoU_c1G3geYIyTyRZZPiTBrFt_EL4EaPQnzfQUspJgLgWo01Pe6OL4WlEz9ziWHb28n3rCvoq8tP3mfzXoz3H06iqmPvv-oCJ9DeFWo7mt10fFw7VFOGrwIQHrEOjnKVpxzUG6WrNcG_OzjkLlssprBkgtCyhj8GpMZSdSQSjpo9G7ieJvnUpuCgeErGPg8VO5TbyOX8zrdllt3OvcLLTzAx0cG1rcdMY5pl0jeJCHPT08KwRH29O53IShcShxXSGflaCJZ4K082EjSVrmLLl8E3S9wglNK2CWhli0jM5GAjKUQ9jRwLlg7QcT8Jj2PKsgfqPGNVhZ5v1rdNt9Z4e9sWDulea5z3_aSGYni6pcYj67Ih7USBT_0whm2saW4Caj0amI6eH4HCZ8SoDuEPOobuWjV5wb-2Rh_J8K3QDPS3YJ867EtNLeIB3YFcyNQ3_MVEo8nloF3pHP_HyU_sLpz7jd-RqtF_-ScMIozDLH8Uf6xqRL9-6LByrXoZDrYzd-PGfw4Fya8ap4KW5THZfkbWoV6bxBUU1P18IhrpErahJ9692B77SLXKRbuPt9F4p1BZzmq7zxWa-3AI-r8olYJjuPh__7Cooh2lkFkyYuVDATwD3sYycq7M8nkevhodReOaP0c_7usIHJikry9IeoicuIxtvDTGLIIqMKNVC4iEEeqzyyedM_PGdytwuR=w1280-h720-no?authuser=0'
    q.questionBase, q.answerBase = questionBase, answer
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()
    
def ea_ba_angles_around_parallel_lines13():
    y = 10 + randint(10, 60)
    x = 180 - y
    values = [['a', x],['d', x], ['e', x],['h', x], ['b',y], ['c',y],['f',y], ['g',y]]
    choice1 = randint(0,7)
    choice2 = choice1
    while choice2 == choice1: choice2 = randint(0,7)
    questionBase = [f"Angle {values[choice1][0]} is {values[choice1][1]}\u00B0.",f"What is the value of angle {values[choice2][0]}?"]
    answer = f"{values[choice2][1]}\u00B0"
    q = cf.Question(cf.currentFuncName())
    q.piclink = 'https://lh3.googleusercontent.com/exTseqX6IrlSSVR3tbmz1dyYyPOTzZstpJpPEnzMDGMkpJ_B9wxDI69ug9uAGHFU89woOIOwwKgmIHDwZ5U4ZlfNoOF0dOhcjp2jGXJEcWhk3BFHny7GDWryqJHQvHVA0uKjbBOQtQr3y4tpubDpJZOmBtA8FSoxYkbQqmCtw1wg0ttTw0bv8uj-xlmRfaQZZNotd2VrQl_t9Kx7LV0BGO-jeltf7ZpmPwqqynGjvCxwln4ERAKzdZ_dKTjewzp9Z2goLllruD1YzJDp7ZRT2pgtONz0p_1TeMgwWc-92cYXUT1oaBoxgzdRuPc7WmPco83toaCPHheoLxwsW8nN_IWiczyTAecf14h_m-NiYLmRC__8yQvVq_tGzJ_rzZy6Me9YSXZ3sHMFMidXs-DZmjIptw_MjSxSbkqG8hcAgWVvp0n8-swCCyZMKP45pXhOtrIaMcqs_yAhmLXAtE_2YJiP9CD_ZDYsXm3meZNzO8fKntqTVeriIiOk0tuxMpVGgLX1leYsFU4qPdENhb5MDJWunokyVqqRUPi4A-uHGjIoI3UIql8aPpmvHTvNOtprLO_orPKGOt0JKizbMIJmiWYVEna80Sg1MLci8l5espVATuKbqYpKCwyBI3UIESm0cn-nXozrvYDnfVyS_man2uohSbuHRCCqyYNb9h5wXdrPw4p9hxfq9O8NOCDy05xQUXU-a8Vkl-sicqgzv11abr2D=w1280-h720-no?authuser=0'
    q.questionBase, q.answerBase = questionBase, answer
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()
    
def ea_bb_alternate_angles_parallel_lines13():
    x = 10 + randint(10, 60)
    y = 180 - x
    values = [['a', x],['z', x]]
    questionBase = [f"Angle a is {x}\u00B0.","What is the value of angle z?"]
    answer = f"{x}\u00B0"
    q = cf.Question(cf.currentFuncName())
    q.piclink = 'https://lh3.googleusercontent.com/ztTnhRbuPSmdAEqSfymbrN5xAz99vUYzZo3eQkNwCpVsrLZCzdfhg_Nkz6Pni0S21HqubZ9bJ_zHQ3NDcYx3XR-BQgsUWQQQMCRsiZ27pyswtbICn9o_DMNxhD6XrvLk2JlQvvydF7j5MnQ_c6ohfybENhFXsGOBODS0sJCOicda4NqYmF8jHAb9XL47fD2sj3f1-rmZSX5oWpAeTZTtVnX01zxpyH4fApPN63G5rjp-YJRHS9J8pLh7TmDNcbkWXMb8s6K2zs9WtV6xJH4Wk6HguLcbBB3zHdxFrPuev3O1NaWTOfp9nw7XnCYtRwgKLHKlWu4qev_-roE_6i_-Px4wG-KFWc7xskmYLvMTCoLk9oFGaGSaKucp6sSpAb6rUz7AoUmvAWWLxaog4z7MUVZ28kw3od8tXbTh2kzZ6-5UZV6htVjOaPOYY9mTtGwDAegrFRo3RfygrHQnIFMzgtiAb4aTh75l2BEGV7kmPPppCvU3cJUIwQW4DxgJerjd_mCot-uR9nLD7tuBbfCRicJZbKRN0UErQzzIPM0JRYbSy_LxkeIL4qLokHvCLptKFLlBawEl9ue70acYNe4b0uumXmGT2rI9v-FH8pwRy8TYu94sJA_GgE2CIKyitOA6TFHyzGZ_C38h-GcjiATklD4ayCiXOrVou6tw-VnoaDGcxiGAcky5HZglkNfCRHOQ4G8s4mmONngldNOXFtEAlBZm=w1280-h720-no?authuser=0'
    q.questionBase, q.answerBase = questionBase, answer
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()
    
def ea_bc_allied_angles_parallel_lines13():
    x = 10 + randint(10, 60)
    y = 180 - x
    values = [['a', x],['z', x]]
    q = cf.Question(cf.currentFuncName())
    q.questionBase = [f"Angle a is {x}\u00B0.","What is the value of angle z?"]
    q.answerBase = f"{y}\u00B0"
    q.piclink = 'https://lh3.googleusercontent.com/ErGo-GxelNDqZ50qSFvX9zxS5kF7gGwx1nYGiACvepcfnFloJb1YfSbsoF1FAWkdwLpBiTOH-PRN5zPOPjO3oidDyhBONaCU10chucr557duLiOje5Iz_IP3BW644378QHxgPvGWWR-ZfZFO-rHPq3zAA9WYCRsY39xZYmXSiLmbULhdlRQP7xj2DdwCi98PmmDWiGasMjsXd1SZ5h2tr0SSvReY042QFbthqS1VyyCCNoC4xFzu0oTGP6lKBaY4cJEtDSXb0gCkIWnY-hiW42bWIIEmOZtKCW2uSgk_ka1vHfVw3GVy7tuGRBKxbKBr42mBkstswdiKJmpU74AXQgiyoojH51cpARmGL9V6UlgKOmRhYiZpCRQHzoYlq-5UJGN3LpnCnncbO0dK9E1ctu82QdKP3_NyvpBWbbmg89tnv5f4rwovIwdW7Fp5o-Zbw9n8JSKEOwEIqy5XqgTsxsWpPrRUQuhgBJSc9vr7zc9RfnwPF9fXbYUwX_mznqTKq2RZNzjlzwdMYj6464CR7Bu_Sc0sjR7RGfhhY-Mq8y5c-SENuKkDwI5P5HpTVX89zBpsexI9pcYmFsw-FW6_zW5FCiG4MoFoOK6F6M9H-Iolkb4qvCEvp0yBLFV83Q3RqRGkBuUT_zgTqVrtRyIYecZPhHntBHbYIuwebjCQ854Y8UO-sOgRtnwQvu4fd7Unc8brXzsOWCaICrgCLPCF1b2d=w1280-h720-no?authuser=0'
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()
    
def ea_bd_corresponding_angles_parallel_lines13():
    x = 10 + randint(10, 60)
    y = 180 - x
    values = [['a', x],['z', x]]
    q = cf.Question(cf.currentFuncName())
    q.questionBase = [f"Angle a is {x}\u00B0.","What is the value of angle z?"]
    q.answerBase = f"{x}\u00B0"
    q.piclink = 'https://lh3.googleusercontent.com/jbwVRGLsg_gHLx9imMUXtnLaO6mULBOsC8sHgIpwRSj5i8AgNtikqp_4av56OUz316AuviyTl8U_Vcwe6GSdFYgMLBzXHbcsR-mnL_XRBo5XeyIFkvfBimHUVN8ykHN8NNan5FobAI5MchZ_CqTBPcCjWJgXPT8zpT7lYsNYU65wfeYxqkT1rkPWr3I9rBwQYr4rAOfJ6ejI24vvsrr_xwPpPl5JerqvPnQno9YQ_pCZLni1NjhH7Xn24C6YC546d9U_-0iGF0_2lg4faXRORWWqnkU5eIA3m2Rp952cpJ0AlDE8WLlZUf_KXfe-UBQWuJpbVCCjhtJ_C-Fhun9ITwwtW4Edjl-vV84rJBgplZwUGS7hChft9Z0GG1OniJ8RhQVx6m3oJ-Fu3P5dKyO7B7UKrj1egVkHJHD9NUtANFNyMRjSX92bHMuGKr3n64mzggQx-KyD5GtQhnGukxsNCpW_40hGzknYajMjyVBuGucueneIZw50DvRZaz303sIIT62fQZyN1kls7BBte0wtlHxbXyUcqDQmDgTx0JhkLIIgS9lZSaRbgAKPTFUy3lVgB5uJXVz497AjYy_vFdJJ9Uqn9boDnf-1CgvWyyTx1JZSds-k6KlgDWlWf90w2k37EUe9JDL02-Tgo-wBbLrfe9JcsjNRKDaEV28IFsQtG5EZeZ0mssE4h-VU6Xg3QOHoOlqvFFx3wWA1sWx0P48ITI7f=w1280-h720-no?authuser=0'
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()
    
def ea_ca_problem213():
    a = randint(30, 80)
    b = a
    c = 180 - (a*2)
    d = 180 - a
    e = 180 - c
    answers = [["a", a],["b", b],["c",c],["d",d],["e",e]]
    choice1 = randint(0,4)
    choice2 = choice1
    while choice2 == choice1:
        choice2 = randint(0,4)
    q = cf.Question(cf.currentFuncName())
    q.questionBase = [f"On the diagram above, angle {answers[choice1][0]} = {answers[choice1][1]}\u00B0.",f"What is the value of angle {answers[choice2][0]}?"]
    q.answerBase = f"{answers[choice2][1]}\u00B0"
    q.piclink = 'https://lh3.googleusercontent.com/poh_kvINtQb8xtk6cty9DKknEsTESMC2SGbyhnFU1AaJAKbFkNrylAWUdpsNFprAb1NMPEWqynIa_ozB74-wlmDBm-FD45upYJJ9kfjX1MUGICWokixhlWcj9Pg_Iwl3RIKs0XnWHHpS-HjKXjNKLK7590RZkdaTOPkGaE0TPQDA_Z3kAWNhFvEaNoI-Q8Uuzahm9PEvb3LmINZubfOVPYVHiItz-g5XLIzLxYKSn-6Ejcj99fd3Vr724bKFErXeDxCc9mt0U_x0hiX3bxS3qDQH0mICgbQjALWwji6gDF6PM8p_l-9ASTHwpZpZOu5wN4XOcSyzvKQIKOGmk_WI1NwIE0J89uWa-OJU2VU04ejTHz0vUpp5z3ukJVoXV9L784UUJ1jHGDHJPQ6SXs-s53o-zFrD5pvKGVNmaghxiYnezgVRvNn4hdLj1BoY-w1gX5aZKUFWKF8W0zi91LGqBCdJslHaCygF3kjb_gCLMyiSSmcBoNn3N_G5wmsPYqLyFUnDxlAQNuDfro_MJIgZ4MFPjOoWLjYZU7vBm7I8QqmCbmfN8IUHJEotYRiaXZVr0DdJ8HSQUHTFCPnU4VHl5vIp91R-rsirkiLsB7gD23Qk38RwrKk0TS4pfZPhW1sUpT8r3VTC4rFwMJrEf2Oxg15a5n7NGMe_UTMMk7P4FqOnDOEIqfFNF0g9XRpY60W_jMK8_2rGYE8-G0At3jpls7JT=w1280-h720-no?authuser=0'
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()
    
def ea_cb_problem333():
    dab = randint(45, 85)
    bcd = randint(45, 85)
    y = 360 - 90 - dab - bcd
    x = 90 - (180 - (dab + dab))
    questionBase = [f"On the diagram above, DAB = {dab}\u00B0 and BCD = {bcd}\u00B0.","Find the values of x and y."]
    answer = f"x = {x}\u00B0, y = {y}\u00B0"
    q = cf.Question(cf.currentFuncName())
    q.piclink = 'https://lh3.googleusercontent.com/n2CkeMbjMMknokD7oZlywTlaA_0XyVkC5qP1QJxhfKz45CrNwn3nUqpI99i9kjJnHxNPq7HcHLJyfvBAh1y3cMY5GOwOhwr13yEwq-6xm-bh0sGR--qaj1bqJ_fy3S9JSn4xcQcJCVuQb-DTtCMGHaRaWxnVRU-56nDXUjYjM1qljOL5N2dEfo2rz568Y63-p5TatDPPRwvQztF6yYKs0K0PgZG1qI9tdYatRwaPM1836VXHIni8I7AyxQyYG6AsSFECmKi8XN1arpe1ofd1HwNDJT8RX2Iv3diHcM3Eox3hk9lcA0iGVDeIAPPExXp_49vHt81EQ5JCghDx5My_A11ExhyBB0pCuG7m7LrZEXb7MSljYwJFRE_0rc6D4dDyrXoYYbNjRMlHaLzYVr6K04AK5MEJSoiPojTCIANiGaYZMGmsR4Z7AfjYQEseGlAE3Qq265zaLIjZ7-DUhOXe_pupx1B8aDICsR3yeAjyXeaG1nEEzlDEHwBmmHm-lJyMDV1LxtRevO-Apc_FJ6ZPRwiSQ9CBlKUjvqrb1H4FOv2rNQvzvU0diYTqN6KuAYANQFQFslBw12ih92hmrZt2DL3jMriK9h3gYAkhRvs5mdIAOLEmxLj5zOLskwyLvB9vpjru2ZTAXF53-F61rRFowAB_cChobJdOLqYl75XaFJ9StNVCNmwUxTSSxIEJ3nBn7EX5AQHS2wKCy6ZtQoBJj-KI=w959-h540-no?authuser=0'
    q.questionBase, q.answerBase = questionBase, answer
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()
    
def ea_cc_problem433():
    fde = randint(10, 40)
    x = randint(10, 30)
    dEf = fde
    efd = 180-fde-fde
    w = dEf
    z = dEf
    bcd = 180 - x - z
    answers = [["FDE", fde],["x", x],["DEF",dEf],["EFD",efd],["w",w],["z",z],["BCD",bcd]]
    nope = []
    choice1 = randint(0,len(answers)-1)
    nope.append(choice1)
    choice2 = choice1
    while choice2 in nope:
        choice2 = randint(0,len(answers)-1)
    nope.append(choice2)
    choice3 = choice2
    while choice3 in nope:
        choice3 = randint(0,len(answers)-1)
    questionBase = [f"On the diagram above, angle {answers[choice1][0]} = {answers[choice1][1]}\u00B0 and {answers[choice2][0]} = {answers[choice2][1]}\u00B0.",f"What is the value of angle {answers[choice3][0]}?"]
    answer = f"{answers[choice3][1]}\u00B0"
    q = cf.Question(cf.currentFuncName())
    q.piclink = 'https://lh3.googleusercontent.com/lLNIbWxP_AqyrT5T6e0j0a_xA1cYcAHSEFcu6LRk2nfifEd5OPDRxYvgLM4n89m43HBFlM2g4TcVA9cTZ59DIP3JieDCPUdgtd_TAWa4Bx20YK8qT72gFK3iRKC3danqc7XggVZa0LyYJOIRjnOfyFZaDPDasffPa7pDmhnZj9ep92Z8ceYlJE1KdJ8mpGUktHw51FHnuC6bViI5GKoM0z4imGh276I08nqd06qS6gBE-iO5JPOZVNojmNbh6NNZ77RJkAuW1wospLEKGGsDvqAj1tqCsXA04DV_iMHzp6XTrV_q_ZKeTRTq-pMjigrATJaWdp_zK5klGcViceOd112p5nQs4x2La8ya3SAY8bptBE7aW5pMWoTKK8KstTa4MhPMu_tdiyGksL5CEMnERxSlmMmzvQfWjfmAY3TwpcHf6ORF63Mk_9PrMFCEG5FbTFUo-SP74oHfS_8QgfU63hEqdlXuq7r_7r3AhjARmGPsdZJ1r2UL4IafRAdReEwam8p1QVR-tWOs74Dbq97F0lCL8zJIqxoSWXfj6IGLO-nTew65JHIhGydE_lAWiT7C6aEr1qgUme7B08SPRAfoW2_Z0tJqI4D15Sbn-SCjpgmZzXBARFB7XH_P8QEicsb3ovew5m012oNS3nD5ZdkhzL6tpbAuNtBalvNMg5fCdqQAso7STgk3CPn7hjJw90I8g7tXuDi7CNcFW9jJkh8YZ2IC=w959-h540-no?authuser=0'
    q.questionBase, q.answerBase = questionBase, answer
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()
    
def ea_cd_problem533():
    n = randint(120, 160)
    o = 180 - n
    z = randint(10,30)
    r = 180 - o - z
    p = 180 - r
    q = r
    s = p
    t = o
    u = 180 - t
    v = p
    w = q
    x = n
    y = s
    answers1 = [["n",n],["o",o],["t",t],["u",u],["x",x]]
    answers2 = [["r",r],["p",p],["q",q],["s",s],["v",v],["w",w],["y",y]]
    nope = []
    choice1 = randint(0,len(answers1)-1)
    choice2 = randint(0,len(answers2)-1)
    choice3 = z
    questionBase = [f"On the diagram above, angle {answers1[choice1][0]} = {answers1[choice1][1]}\u00B0 and z = {z}\u00B0.",f"What is the value of angle {answers2[choice2][0]}?"]
    answer = f"{answers2[choice2][1]}\u00B0"
    q = cf.Question(cf.currentFuncName())
    q.piclink = 'https://lh3.googleusercontent.com/wRDH1Wej5eWo0Tt36noH9Eb3PpldVwfhd_Z9qy7zCg73y2Qc7pjap0aAG626ldQuCHNUNCbIVnER2ccVor_EwtVBdT_2u0pnDc-sM_pTFVESwf59T4xCZ3E3YzlOMQfnXdykQUP_U0kiPDvFBoU8hon7IXQEuA9bM0Ls-9DF6ZiwvQfiAJvkHnDNRQpjiDWC0fmSU8y0Hxh7pFPdurkR2e_YwFEJHeXs3gOU0m1THe0N4RnXXzyxdINWkFgVtJgJdy3gr_bjqjCjWn0IxDUrBIgvSNAluI1SKuADS1njjTNp0O5KV3ayXCwoXsR2IrZZK3mhhbePWJ0e5MMIslPtYSSJixQPE8BDREyWBtIcomMn6LONKkO76ZApH8dLyfdByAKjojMfKRkGW3EIF1wdT-5bRfT51MY9G4gFpahB3FJ5s0DZWvCAASj6FszS5Tk0sNbuMv-Za4zfRp515GY8QN4339hrySLvbZNP8QOXvahT9a9pmncl3TVeD3ukCl_BbrQx_iHWVENchYjYw_pI3fipKthvxENnihUzMgZjJXbD-7d4j0zQwsD-47bri1a57hQBuKQskV2G3Fr4jbtWOfLhOWo__4Rl-BDZXJDyTpESEazUs-rM_l1IfxyBMNEKpS0j87Y3_PZWmHaxMWaFC8jLgcTeybyNVh7Vy_w6K0EjjIGrPmWP4Zs6wXif2lgJRIZ9F8mbsv5e3GoxuzNi-tUm=w959-h540-no?authuser=0'
    q.questionBase, q.answerBase = questionBase, answer
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()
    
def ea_ce_alternate_allied_corresponding13():
    angleTypes = [['/diagrams/gcsemaths/parallel_alternate_side_az.jpg', "alternate"],['/diagrams/gcsemaths/parallel_allied_az.jpg',"allied"],['/diagrams/gcsemaths/parallel_corresponding_az.jpg',"corresponding"]] 
    choice = randint(0,2)
    questionBase = "What is the name given to angles such as the pair (a and z) in the diagram above?"
    answer = f"{angleTypes[choice][1]} angles"
    q = cf.Question(cf.currentFuncName())
    q.diagram = f'{angleTypes[choice][0]}'
    q.questionBase, q.answerBase = questionBase, answer
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()
        
def ea_cf_problem613():
    x = randint(3,7)*5
    print(x)
    timesX = randint(3, 5)
    print(timesX)
    print(x*timesX)
    print(180 - x*timesX)
    plus = randint(10, 50)
    group1 = ["e","h"]
    group2 = ["f","g"]
    x1 = (f"{timesX-1}x")
    y1 = (f"x + {int(180 - (x*timesX))}")
    questionBase = [f"{group1[randint(0,1)]} = {x1} and {group2[randint(0,1)]} = {y1}.","Calculate x."]
    answer = f"x = {x}"
    q = cf.Question(cf.currentFuncName())
    q.piclink = 'https://lh3.googleusercontent.com/yB184kU-g8w_K4HpNIPpkV3mjjjo8TpO2cTPSW2Rfn4JzFWvVVyQOt2Fs-AgoPz4UsVYRPY2dIi5Xg2A580pNwyHBlhPYHmLPN02a-QIIfal1b_sl7fdY3XChnKUjAE2OjRupigUbeQeGlnMghwDSjsO3M8TXfsUFRmm6u7n_0tWmZYrzjlHM4cXkYXHge4yUUJZt4PS74OWX1dfqAPUzEDGzCuAunCCSxA30MvnYGioc_rVF-eBdB9XX6zGJiAoUVoIAAVmyjTa1tSI3PX0Lgd_JRGl-om7-518Rj3cCkSjvpr-jCwH7x4XT1M-zw5lC_0yezqNU5F6vIDwwp5Ya7WHPVubBKAsUAQyv5VI3B1NYry86A1BJEhfZYA_9SkaZGCKOpNK8KjTbW1tXqjFnRHqCKbGZZpsQg0XeoBbMUTZxzJSJlvNQOalLpTbSKwOk7iaYQQQb19myVy4WP1BS1C9c8GTUFUXFLZD3dBwh6u-NBgU2WIxKkrgliA5nSI5veE5BYI1A6kl4qpcjNwx4pn7fl0hSKoJJoCuuse9OlBVXk3D-HNDUR0YpH5Ydswvy3aWDCvulUmErUGVAry-DkdNqk7_GJIePfsor_I17J6l0dvBFhM3nAs57bv6R4jZbYZSqkNF4N4bXtfsggZiHeohirapcHYzel2OEmdNrgm60Wt2SSVQbpe4wlrG2JU2HzPCFIezNnubBFFcOuB71b5Z=w959-h540-no?authuser=0'
    q.questionBase, q.answerBase = questionBase, answer
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()
    
def ea_cg_problem724():
    e = randint(50, 80)
    f = randint(110, 160)
    missing1 = f - e 
    h = randint(30, 60)
    missing2 = 180 - f - h
    g = 180 - missing1 - missing2
    questionBase = [f"e = {e}, f = {f}, h = {h}.","Calculate g."]
    answer = f"g = {g}"
    q = cf.Question(cf.currentFuncName())
    q.piclink = 'https://lh3.googleusercontent.com/NWZNsyyPuKX8PWLanrQCvTR-YtuipZkkq0RrDh0QdLjreVeykqMuNFQcnhNwa8o2GLNTK_jRFgMJrn-ClNSqk56AbA0Gbwi_V9VZr7WfUhxGw4G29meRCo952QG92eAIV3Ll1p42yVqQ8jRgkNxKdX6N2VrLd6zRMbYSIMUPQvBNKKXsk-EAOizbokpwMnCPqTPZYd_90tXDYiftPrtSwnLxtUNJFh-0F0RzcVK2uPJgkodrFGEqdDtz9fYfz60nF0CnfEZME5in0ex7ospYF1N5MzFluSFhmjI3k2nI9Gg8unD1O7pIPpZivx9ZdT5MOci2-qzXMZVQKU-Y_Bp1pyzzpDAdDddHvtXBUkFePK5oAv5XfqGBx2z-O7MjOwOooEHQ3TvdGSkvYCzUeqywHoWJhctZIoXqxhelZpO1jmLYENJwijZsPF4gl5OZEMLX7z8omUfxwJ-0CGXJVkmv_wQ6QCfYMp2DQfiGG7gUw1CqhRkQcBt4RhGh-S7uYituUQADxOkahokzh7m-awmPKN9xsUK_fjsgnuhcpqpkb9YdjPDAMgxL37xITEzRRMnRzYeiKsCws6c5Syy5x3mTF5dFcLVOr1PfWnzRk1rovEy_EYcZ626h0qZEtPLnbla-zIj1Dh6LeNjtHdmCJPL1HGfIIEpaB11W5YO9xquzCm_6VwZArZqyeCdHBZCqJ1yKMFsx0UBXBcH0mauosJLYq_WT=w959-h540-no?authuser=0'
    q.questionBase, q.answerBase = questionBase, answer
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()
    
def ea_ch_problem813():
    x = randint(40, 70)
    questionBase = [f"Angle x in the triangle above is {x}.",f"Bob says that angle y is also {x} because the base angles in isoceles triangles are the same.","Bob is wrong. Why?"]
    answer = "An isoceles triangle is defined by two of its sides and angles being equal. The two equal angles do not have to be at the base of the triangle"
    q = cf.Question(cf.currentFuncName())
    q.piclink = 'https://lh3.googleusercontent.com/EHl6rvVZC8hNyvaDH_Mn-Ce2CZcAB8vWULHW9F7jlWOI72iMRQ4HPJGbBCgR61rM59WMCwZ-EY-oIy0MprGfb8jT3L2vhKVzQ_o1A085I3C9mxQi7GpXjDtqljkOBmMjhd3TTl4YpW382SmWfnYJSYzQoWSkwCw3UuQoWN5mYNLRf0JusEZIYfadkiEJuXt2G7WFAx_WKd1SZhuFRabiOn-TnRwD3nCrz045hPsuSlqvK50LvzBORBLTfTH8yws_Mq-b1fTBj7AlftWnkGG3E9aeW5c14u6JPA3mUrgiYSW5x83N17QNGqgwU-Offma8XFpw2sGNkdykATawt6tUUoddWY6Edtv2mMeH-o01vT4KWrambSFMm-Ik-TpY9aSaooYPTv3HJ7M4PBXiQcwHG_AhjSytKTM0AjGCRX259ZufVUdGq0ATIrY3WWwWCt7goUUI3Fd-y8QiXAI8pHn37so5yI2t1yGJEEIUlXXW8cRjI85yr96qGcLuB5QuiIizdhRGySP8PY4TzF872f3KGoDNdIjRasOK742tJDFxvt87BmcXTJsTe9jDVkgEMrUP9hGe0sChZSwtGi4-tnIl5iGaWcg9AO42tYQQWW7MDDW25h98gTJKN_EAfF5yzfLh704m14y_bsikMGwYCvArn4x84DSeJJ_mIxh61Zbt3LOZ9swUaTZ47JAYX7ZkwLi7MR2Jr8AHH87PV4g-coo03t1T=w959-h540-no?authuser=0'
    q.questionBase, q.answerBase = questionBase, answer
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()
    
def ea_ci_problem923():
    statements = [["e = 180 - f because both angles are on a srtaight line", "e = f because both angles are on a straight line"],
                  ["e = h because they are alternate angles", "e = h because they are allied angles"],
                  ["h = 180 - f because they are allied angles", "g = f because they are allied angles"]]
    choice1 = randint(0,len(statements)-1)
    choice2 = choice1
    while choice1 == choice2: choice2 = randint(0,len(statements)-1)
    choice1, choice2 = statements[choice1], statements[choice2]
    wrong = randint(0,1)
    right = 1 if wrong == 0 else 0
    questionBase = [f"One of these statements is incorrect: '{choice1[0]}', '{choice2[1]}'.",f"Correct the incorrect statement."]
    answer = f"{choice2[0]}"
    q = cf.Question(cf.currentFuncName())
    q.piclink = 'https://lh3.googleusercontent.com/yB184kU-g8w_K4HpNIPpkV3mjjjo8TpO2cTPSW2Rfn4JzFWvVVyQOt2Fs-AgoPz4UsVYRPY2dIi5Xg2A580pNwyHBlhPYHmLPN02a-QIIfal1b_sl7fdY3XChnKUjAE2OjRupigUbeQeGlnMghwDSjsO3M8TXfsUFRmm6u7n_0tWmZYrzjlHM4cXkYXHge4yUUJZt4PS74OWX1dfqAPUzEDGzCuAunCCSxA30MvnYGioc_rVF-eBdB9XX6zGJiAoUVoIAAVmyjTa1tSI3PX0Lgd_JRGl-om7-518Rj3cCkSjvpr-jCwH7x4XT1M-zw5lC_0yezqNU5F6vIDwwp5Ya7WHPVubBKAsUAQyv5VI3B1NYry86A1BJEhfZYA_9SkaZGCKOpNK8KjTbW1tXqjFnRHqCKbGZZpsQg0XeoBbMUTZxzJSJlvNQOalLpTbSKwOk7iaYQQQb19myVy4WP1BS1C9c8GTUFUXFLZD3dBwh6u-NBgU2WIxKkrgliA5nSI5veE5BYI1A6kl4qpcjNwx4pn7fl0hSKoJJoCuuse9OlBVXk3D-HNDUR0YpH5Ydswvy3aWDCvulUmErUGVAry-DkdNqk7_GJIePfsor_I17J6l0dvBFhM3nAs57bv6R4jZbYZSqkNF4N4bXtfsggZiHeohirapcHYzel2OEmdNrgm60Wt2SSVQbpe4wlrG2JU2HzPCFIezNnubBFFcOuB71b5Z=w959-h540-no?authuser=0'
    q.questionBase, q.answerBase = questionBase, answer
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()
    
def ea_cj_problem1023():
    efd = randint(20, 50)
    bcd = randint(60, 80)
    baf = bcd
    afb = efd
    abf = 180 - baf - afb
    fed = abf
    answer = [["FED", fed], ["ABF", abf]]
    choice = randint(0, len(answer)-1)
    questionBase = [f"Angle EFD = {efd}. Angle BCD = {bcd}.",f"Find the value of {answer[choice][0]}."]
    answer = f"{answer[choice][1]}"
    q = cf.Question(cf.currentFuncName())
    q.piclink = 'https://lh3.googleusercontent.com/2k8k7vJjouhB05McsnrZudgDTEGnJIAx3_20rFIjtLrZ4b-6RqaJdVnVWXMhfEK1z3VN6Y0hzfxsBsJExvo2Z8-PRj-EvVlGB_HdRwHWmnzoh0tvxkMoZzZ0aIkbpY44SjrxPpml6cYQPGwbgxE4Zlx4Svv2KxGyHK_MI6TSEjtWiochis4sLhTvY99ofxfZA2lMVBYyCu0408H1Wgn-P1US4Yqu9sC-etVsjmulzn4isZSqj2-QWXjrlZkU8Kf2wYwc1YcytfEETm-J1AwSHe4aaSyUZ58tsP0tZ50Ljn8f4xRP9VatZOh4bv568gDWM2sS1jf45AJ5-s4fYBl9gR72oYAB51aS6xJZXq0ny9DQOEUDHUX3R6eSCQwgzbBkBFNaGDNxTv9eBUoiFBQAJn95wSPsaP3nmGgeDXnKLsk2FcPK6QXVJo8KY1gG7aK8m6K0XG7T85Zq46AdY6wjf2YkHhcNDQoyYijA4isykcpkFOOdktl342AOPBxe2gZfdQ4viQ1zWVxVktcV_uPXnppmsKTxKxmcvZgYyz8w8h95bxWc7RABuo1MUkfpE1GsWkeL5lGtHq0bymZX472HrdP6GrfK5zClMzp1DUf-DAG0SAEESxVnI7cU7XYMoQSESaQ5S-wqeQl9VEJXpS5NbDo-MMlShyEkmUSQYMHy2-m8NTLHHjXOLkmMNf7ND42ZQrnmeBVZJNRNUWoLm0e5edoj=w959-h540-no?authuser=0'
    q.questionBase, q.answerBase = questionBase, answer
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()
    
def polygons():
    return ("triangle","square","pentagon","hexagon","heptagon","octagon","nonagon","decagon")

def sides():
    return [i+3 for i in range(len(polygons()))]

def eb_aa_polygon_attributes13():
    polygonList, sidesList = polygons(), sides()
    choice = randint(0, len(polygonList)-1)
    attribute = ("sides", "interior angles", "exterior angles")
    choice2 = randint(0, len(attribute)-1) 
    questionBase = f"How many {attribute[choice2]} does a {polygonList[choice]} have?"
    answer = f"{sidesList[choice]}"
    q = cf.Question(cf.currentFuncName())
    q.questionBase, q.answerBase = questionBase, answer
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()
    
def eb_ab_polygon_intext_angles13():
    polygonList, sidesList = polygons(), sides()
    choice = randint(0, len(polygonList)-1)
    attribute = ("interior angles", "exterior angles")
    choice2 = randint(0, len(attribute)-1)
    ans = (sidesList[choice]-2)*180 if choice2 == 0 else 360
    questionBase = f"What the sum of {attribute[choice2]} in a {polygonList[choice]}?"
    answer = f"{ans}"
    q = cf.Question(cf.currentFuncName())
    q.questionBase, q.answerBase = questionBase, answer
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()
    
def eb_ac_regular_polygon_attributes13():
    polygonList, sidesList = polygons(), sides()
    choice = randint(0, len(polygonList)-1)
    article = "an equilateral" if choice == 0 else "a regular"
    if choice == 1: article = "a"
    attribute = ("What is the order of rotational symmetry", "How many lines of symmetry", "What is the value of an exterior angle")
    choice2 = randint(0, len(attribute)-1)
    questionBase = f"{attribute[choice2]} in {article} {polygonList[choice]}?"
    answer = f"{sidesList[choice]}"
    if choice2 == 2: answer = f"{360 / sidesList[choice]}"
    q = cf.Question(cf.currentFuncName())
    q.questionBase, q.answerBase, q.diagram = questionBase, answer,None
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()
    

def eb_ad_regular_polygon_exterior_angles13():
    polygonList, sidesList = polygons(), sides()
    choice = randint(0, len(polygonList)-1)
    article = "an equilateral" if choice == 0 else "a regular"
    if choice == 1: article = "a"
    q = cf.Question(cf.currentFuncName())
    q.questionBase = f"What is the value of an exterior angle in {article} {polygonList[choice]}?"
    q.answerBase = f"{int(360 / sidesList[choice])}"
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()
    

def eb_ae_triangle_attributes13():
    #equal sides, equal angles of 60, lines of, rotational
    trilist = ("an equilateral", "a right angled", "an isosceles", "a scalene")
    answerList = ((3, "3 equal angles of 60 degrees", 3, 3),
                  ("Up to 2 equal sides. Right angled triangles may be isosceles or scalene", "1 angle of 90 degrees", "1 if isosceles, 0 if scalene (right angled triangles can be either)", 0),
                  (2, "2 angles are the same", 1, "No rotational symmetry"),
                  ("All three sides are different", "All three angles are different",0,"No rotational symmetry"))
    choice = randint(0, len(trilist)-1)
    attribute = ("How many equal sides", "For a given triangle, how do its internal angles make it","How many lines of symmetry are", "What is the order of rotational symmetry")
    choice2 = randint(0, len(answerList)-1)
    questionBase = f"{attribute[choice2]} in {trilist[choice]} triangle?"
    answer = f"{answerList[choice][choice2]}"
    q = cf.Question(cf.currentFuncName())
    q.questionBase, q.answerBase, q.diagram = questionBase, answer,None
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()
    

def eb_af_quadrilateral_attributes13():
    #sides, parallel, angles, lines of, rotational, diagonal
    polyList = ("a square", "a rectangle", "a rhombus", "a parallelogram", "a trapezium", "an isosceles trapezium", "a kite")
    answerList = (("4 sides of equal length", "2 pairs of parallel sides", "4 equal angles of 90 degrees", 4, 4, "Diagonals are the same length and are at right angles"),
                  ("2 pairs of sides of equal length", "2 pairs of parallel sides", "4 equal angles of 90 degrees", 2, 2, "Diagonals are the same length"),
                  ("4 sides of equal length", "2 pairs of parallel sides", "2 pairs of equal angles, where opposite angles are equal and neighbouring angles add up to 180 degrees", 2, 2),
                  ("All three sides are different", "2 pairs of parallel sides", "2 pairs of equal angles, where opposite angles are equal and neighbouring angles add up to 180 degrees",0,2),
                  ("No sides are the same length", "1 pair of parallel sides", "All angles may be different", 0,0,"diagonals have no relationship"),
                  ("Sloping sides are the same length", "1 pair of parallel sides", "Two pairs of identical angles", 1, 0, "diagonals are the same length"),
                  ("2 pairs of equal sides","No parallel sides", "1 pair of equal angles", 1, 0, "Diagonals cross at right angles"))
    choice = randint(0, len(polyList)-1)
    attribute = ("How are the length of the sides related in", "How many sides are parallel in", "How are the internal angles related in","How many lines of symmetry are in","What is the order of rotational symmetry in", "How are the diagonals related in")
    choice2 = randint(0, len(attribute)-1)
    questionBase = f"{attribute[choice2]} {polyList[choice]}?"
    answer = f"{answerList[choice][choice2]}"
    q = cf.Question(cf.currentFuncName())
    q.questionBase, q.answerBase, q.diagram = questionBase, answer,None
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()
    

def peopleGen():
    people = ("Donald Trump", "Stalin", "Jeremy Corbyn", "Madonna", "Posh Spice", "Justajolt", "An intelligent gorilla", "Boris Johnson", "Some pleb", "A man with a dry cough", "An unwilling kung fu student")
    return people
'''
def eb30_tangent_radius_diameter_chord():
    people = peopleGen()
    true_tuple = ("line a is a tangent", "line b is a radius", "line c is a diameter", "line d is a chord", "line b will always be half line c", "line a will only ever touch the circumference at one point", "line c always passes through the centre of the circle", "line b meets the cetre of the circle at one end and the circumference at the other end", "lines c and d both touch the circumference at two points", "line c meets the circumference at two points", "line d meets the circumference at two points")
    false_tuple = ("line a is a radius", "line a is a diameter", "line a is a chord", "line c will always be half line b", "line a will only ever touch the circumference at two points", "line c never passes through the centre of the circle", "line d meets the cetre of the circle at one end and the circumference at the other end", "lines b and d both touch the circumference at two points", "line a meets the circumference at two points", "line b meets the circumference at two points","line b is a tangent", "line b is a diameter", "line b is a chord", "line c is a tangent", "line c is a radius", "line c is a chord", "line d is a tangent", "line d is a radius", "line d is a diameter")
    choice = randint(0,1)
    answer = "Correct" if choice == 1 else "Incorrect"
    statement = true_tuple[randint(0,len(true_tuple)-1)] if answer == "Correct" else false_tuple[randint(0,len(false_tuple)-1)]
    questionBase = f"In the diagram above, line abc is a tangent and touches the circumference at the same point as radius r at point b. {people[randint(0,len(people)-1)]} says that {statement}. Is this statement correct or incorrect?"
 = "A tangent always makes an angle of exactly 90\u00b0 with the radius it meets at this point."
    print(questionBase)
    print(answer)
    diagram, constant, marks = f'/diagrams/gcsemaths/.jpg', None, 1
    previousQ, nextQ = previousNext("eb", 0, 2, currentFuncName())
    pre, preans, marks, level = None, None, 1, 3
, video = None, None
    return previousQ, nextQ, diagram, constant, questionBase, answer, pre, preans, marks, level,   , video
'''

def eb_ba_circle_radius_tangent13():
    people = peopleGen()
    true_tuple = ("the angle xba will always be 90\u00b0", "xba is a right angle", "xbc is a right angle", "line abc will never touch the circle again after point b","joining x, b and c makes a right angled triangle")
    false_tuple = ("angle xba and xbc are not the same", "joining points x, b and c can make an equilateral triangle", "angle xbc is the only right angle on the diagram")
    choice = randint(0,1)
    q = cf.Question(cf.currentFuncName())
    q.answerBase = "Correct" if choice == 1 else "Incorrect"
    statement = true_tuple[randint(0,len(true_tuple)-1)] if q.answerBase == "Correct" else false_tuple[randint(0,len(false_tuple)-1)]
    q.questionBase = [f"In the diagram above, line abc is a tangent and touches the circumference at the same point as radius r at point b.",f"{people[randint(0,len(people)-1)]} says that {statement}.","Is this statement correct or incorrect?"]
    q.hint = "A tangent always makes an angle of exactly 90\u00b0 with the radius it meets at this point."
    q.piclink = 'https://lh3.googleusercontent.com/ddMqyJr6ar23b0uQ0BVFvWxBnIrz6FXnTGK88R-4Fw73blne1T5qNkNB-D0AqU0GeZ7IjDRRdfc4nsb2RSl7qvA1zS485BP4VGP1L0yddd43d2ldJ5HbPMsSKssgtqaUYuyhEEADwmGU_SKf_MHsLBfbhslHBbJMm72VAbnxr1s4lnLEi9NZHtdEsUHD2ozS8fGGlJX8RcRj4yL_1b3cQNg2ps02XoOEE6QG3xnusItcdbYwmfjYVdk53lKsfPZAGf_EzhUYhhkWwJhdfHhS1QiZwZdQTr014lUU94VDZdnMOT2ePxo4OstCtlZ0brzrJ5c21V6s8dfMtQ3j4ds9rn8Fy_k_nq0ngcKnPNsVUd0sAF799_5j8njZEHhzOJD-loYu4KCc5-8mYdZMdjpohL-CXhiFqO55lExbiSaOdxeVBLEFySX5cjf0qH9G_TH1rAqiXEr6DMSm3UKRsUOYcNh1kb0vh92V8eLCCj5SYFOIbNZR_z4GhsHbeLFZ9DHW8JvGX5B3RawMSGe_pPZbi4epSfCn1ouYbvkNBhn_-O3K6GKE0P84SthKqBtSTr6XnNTVzObmK9MN6XTL0aSxUwSd8FI0jaN6PxLFRfB8P6tngHqQPsC0sRm-CT8BbzwKLt2aZoX8nZoagQlXgbeimSlBMqQh1xZvypDsPv4kGkw_8K5tk43C3K4U6K5Z6HLm-JcadfjHzN4DAVp61smho_IN=w1280-h720-no?authuser=0'
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()
    

def eb_bb_circle_two_radi_isosceles13():
    people = peopleGen()
    true_tuple = ("angles xba and xab are the same", "the triangle in the diagram has one line of symmetry", "two of the angles in the triangle made by radi r1 and r2 are the same", "two of the angles in the triangle made by r1 and r2 are the same","the triangle made by r1 and r2 has no rotational symmetry","any other two other radi would make another isoceles triangle")
    false_tuple = ("angle xba and xab are not the same", "joining points x, b and a can make an equilateral triangle", "the triangle made by r1 and r2 has rotational symmetry order 2","the triangle made by r1 and r2 is scalene", "the triangle made by r1 and r2 has three different angles",)
    choice = randint(0,1)
    q = cf.Question(cf.currentFuncName())
    q.answerBase = "Correct" if choice == 1 else "Incorrect"
    statement = true_tuple[randint(0,len(true_tuple)-1)] if q.answerBase == "Correct" else false_tuple[randint(0,len(false_tuple)-1)]
    q.questionBase = [f"Radi r1 and r2 meet the circumference are joined by a chord to make a triangle.",f"{people[randint(0,len(people)-1)]} says that {statement}.","Is this statement correct or incorrect?"]
    q.hint = "Two radi formed from the ends of a chord which meet in the centre of a circle form an isosceles triangle."
    q.piclink = 'https://lh3.googleusercontent.com/GtQtSNyBR7aK4cBli6bbEKbxWInLE1GezbhpafzyGdMqUts4EOESCyfBe1WANRBnytwNg1xOtlpvbUcqZoZNmc4yFs420OJnpC-lwDKQeSlDyT9jzCf4TyWU7y6U-kZUF_8qP1bn3vl0T9STBMKrzZHLq6gZsADrILLr23ZiNExJkILfgjGSXUO5-WYUmxPgdOC5YXwckGZovAuf01Qgk8TbKqvhiu2rQZ_HECOYZfJNwOxmG9BCkkMJvAsdoroZhqa9crbiCRpzGmbBkKtyZ83-hRm-RMRESoqg6wZI2scdVP8Gz-W_SDYAhfcd3hXdOm02GaJkVuHq-GOwMEWlEoRIvRFgVGliSBm8YooxE4_8C56EY0MqLASIGAmGR7HqlIWv90_LcT9o6qrihBD-pYgypS9RWktjD4JxsOt9C-r-RUldvB05DBZpaAJvl-V3wuleWm22Lf4Uv7GJ9vcKWFZWxfyO0l_O5S8NirIkdpKDz1Re731wGiXKEx9FGuc8A9U5gIUR4MsvbjXmh0jma_KK0_Z6V7YZBWpwVyNhq5Y1B_hpDLm26TxzUzj3JpNO4oG2RRteCZ7m58EPXOprITxUx5TyU5VMSTX5DsHHq8qnejMrZK8TFmqCiexMuGausq2jQUcYf0VsxcAwQm9bSMaQFasuQIN1SdZ4x8smr0nAuc08IBTsth-GeliWXGYc-e-emxtkpLXES80Gev76nB_X=w1280-h720-no?authuser=0'
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()
    

def eb_bc_perpendicular_bisector_chord13():
    people = peopleGen()
    true_tuple = ("xy passes directly through the centre of the circle", "the angles around the point where ab and xy cross are all right angles", "the angles around the point where ab and xy cross are all equal", "the lengths of ab on either side of xy are equal")
    false_tuple = ("xy does not pass through the centre of the circle", "the angles around the point where ab and xy interect are not equal", "the two pairs of angles around the point where ab and xy intesect are not the same","the lengths of ab on either side of xy will never be equal")
    choice = randint(0,1)
    answer = "Correct" if choice == 1 else "Incorrect"
    statement = true_tuple[randint(0,len(true_tuple)-1)] if answer == "Correct" else false_tuple[randint(0,len(false_tuple)-1)]
    questionBase = [f"In the diagram above, xy bisects the chord ab exactly.",f"{people[randint(0,len(people)-1)]} says that {statement}.","Is this statement correct or incorrect?"]
    q = cf.Question(cf.currentFuncName())
    q.piclink = 'https://lh3.googleusercontent.com/elCVggnrYHpOq7MN-d4Cnna8Pl0RHlqhW7GAY0ViIti-DLdLt89Mei1AElezgm-a0gI4StC3HftxU9NlLEz6Uo7VMfFczev7tU4n5fJjUeJ2w2kU3r5JqQx20bHCdMsDRtYyjxifSOilPWZp0x1FDfkzzN5zDT9a7O9KYRC3xSAjIKNY1bg8PVzKWlfrU7MLkP7i3bCh-8NtH3WfELOzTZzzCP_tkboeYYpQQ8A91fUfrEYYvUzbyrF2SeryeOHBPHsX4g_Uv_Yujof2uMeco06SPUWnTxDdVX1qkLQpf5wMzIEwhcz7GxAn5pm86TpPSx5lOj7iA3N0bgvOsNoGcG8OAjT1h0EMge_OSgqAV0thE6a9gFWm0hJjEiqB5VLMjQj0v8jeeyuKzFylVwKY56LCuAOFhb0Tifs1uNIysk-mI19nGnJH1cjAUX4OvuJ1_ENQey1WGX4vEevKv7lrR4p1zsaTbEO4TxgncYAg9zMOfDbw8h_WMgGSqtWwVxLxn2orqjWNxwNj5I0sUeUziKGj8pZh3mApqHkFjKlMYN6UaSd8RmU_vrkalM7_1u0KX2hqH1nT922UdueLPcmrjZnBFHYplJREMq5MbuAOssczOMAlREVvMb_SUs5VATjClSVM8efV5Ho_2i-Tonk04o4ljjgcGpLlrL7_EB_HYuyieD7VygZ4ho_14c7Bwv-KzTyh39fksMroIWic-JJy9ag0=w1280-h720-no?authuser=0'
    q.questionBase, q.answerBase= questionBase, answer
    q.hint ="The perpendicular bisector of a chord passes through the centre of the circle."
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()
    

def eb_bd_angle_centre_twice_circumference13():
    people = peopleGen()    
    true_tuple = ("angle y is double angle x", "and x is half angle y", "if angle x were {number}\u00b0, angle y would be{number*2}\u00b0", "the lengths of ab on either side of xy are equal", "if you know one of the angles at the base of the small triangle, you can calculate angles x and y", "There is one isosceles triangle in the diagram","if you know angle x, you can calculate angle y", "if you know angle y, you can calculate angle x", "if you know either angle x or y, you can calculate all of the angles in the smaller triangle", "The smaller triangle in the diagram is isosceles")
    false_tuple = ("angle y is half angle x", "angle x is double angle y", "even if you knew one of the angles, the other would be impossible to caclulate", "if angle x were {number}\u00b0, angle y would be{number*2}\u00b0 the two pairs of angles around the point where ab and xy intesect are not the same","both triangles are isosceles", "both triangles in the circle are scalene", "if one angle is {number} degrees, the other will be too", "if you know angle x or y, you can calculate the angles in both of the triangles", "the smaller triangle is scalene", "it's impossible to calculate the angles in the smaller triangle if you only know x or y" )
    choice = randint(0,1)
    answer = "Correct" if choice == 1 else "Incorrect"
    statement = true_tuple[randint(0,len(true_tuple)-1)] if answer == "Correct" else false_tuple[randint(0,len(false_tuple)-1)]
    questionBase = [
        f"In the diagram above, z is a chord.",
        f"Angle y is made with lines directly from the ends of chord z, which meet at the centre of the circle.",
        f"Angle x is also made with lines originating at the ends of chord z which meet at the circumference.",
        f"{people[randint(0,len(people)-1)]} says that {statement}.",
        f"Is this statement correct or incorrect?"]
    q = cf.Question(cf.currentFuncName())
    q.hint ="The angle made at the centre of a circle is exactly double the angle at the circumference of the circle from the same two points at the ends of a chord."
    q.piclink = 'https://lh3.googleusercontent.com/i4xTLa64o_HL9UUtzLP_vNHIeibgT0wfvB32E818zEgSfj7Sgz8uuV5agzCHg0vwa0mPJMDGjd66rWyFEzKJf5c63su4Pni3uFYc7C0DkWooF0KYZ5zv3kOrPcOmr0uYgQYbbjOnJe5f9sYJzmeaRhOmOt6GIh8BxwbBj5JwSAqOyhn16KGdCCP4RLPH-RINRxP_FiUt5R0xCuwmmqV8v7m-4dTs7pubbM223hdFSN2No4NggOQ-9cRU8e91FjetKB9XUAJIG3eXP9C0GhFt7-JjpfVWC6IMtbrAGPqtmooHVfbmFLW4ujuWYnG-xembLJYWlBM5lwI_cbij5nX3oIX9IgFuvG8GR-Oo55hA2YFx-Ea9vajyV-lQX447pFFLZC7jfKWKoYjG8HjBwdd-W9PjheENTYdIeRRofNyfYZgiBpM7xxu0aDSij0wHbG1gDS9oC9Fn7wCB18ssPVYx685axg7Vfku4kP6nmFLieMBg8Rxwcr5HivzgTonnq1s-NLuFMUCQqUbB0SZ8W6r90jSUAS6-112OmLl_XIsqQNR1Wy4RuyvU7ZZK8edvSk9U_IaqueVwVIQZ3U1I7PE6g0Ru0_E4n__d17AEzvJHkZ0oI1fQedZSUQ-mc_dxd97FINJjpJNkXefnWS7UqX8ekAHNRcjRXhSYwezDct870T0W0nWvJKpnSYyzdanhIsGFe72EbHswTlUTDArTe5IccPNt=w1280-h720-no?authuser=0'
    q.questionBase, q.answerBase= questionBase, answer
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()
    
def eb_be_angle_semi_circle13():
    people = peopleGen()    
    true_tuple = ("angles at points c and d are both right angles", "angles at points c and d are both equal", "the triangle between points a, b and d is a right angled triangle", "the triangle between points a, b and c is a right angled triangle", "the triangle between the points a, b and c has no lines of symmetry", "the triangle between the points a, b and c has no rotational symmetry","the triangle between the points a, b and d has no lines of symmetry", "the triangle between the points a, b and d has no rotational symmetry")
    false_tuple = ("angles at points c and d are both greater than 90 degrees", "angles at points c and d are not equal", "the triangle between points a, b and d is an equilateral triangle", "the triangle between points a, b and c is equilateral", "the triangle between the points a, b and c has one line of symmetry", "the triangle between the points a, b and c has rotational symmetry order 1","the triangle between the points a, b and d has 1 lines of symmetry", "the triangle between the points a, b and d has rotational symmetry order 1")
    choice = randint(0,1)
    answer = "Correct" if choice == 1 else "Incorrect"
    statement = true_tuple[randint(0,len(true_tuple)-1)] if answer == "Correct" else false_tuple[randint(0,len(false_tuple)-1)]
    questionBase = [
        f"In the diagram above, line ab is the diameter.",
        f"Points c and d are where lines originating at the ends of the diameter meet the circumference.",
        f"{people[randint(0,len(people)-1)]} says that {statement}.",
        f"Is this statement correct or incorrect?"]
    q = cf.Question(cf.currentFuncName())
    q.hint ="The angle made at the centre of a circle is exactly double the angle at the circumference of the circle from the same two points at the ends of a chord."
    q.piclink = 'https://lh3.googleusercontent.com/T9JkN8cvwz6bZyO-Gza9_p6bvAg3PSu_w5h5oTu0FJ_S_7wjdf1JNrpCkqOMiek-oQdCtnl5xQWebOsW-WIbjVTGzq4ydxmCM4R4cBt4WA7iDAyPHMTNUDRFwTCArxTvJo9cfE0kLOl6UK98UuDtKZtO8vitdm6DWwZkGxMZyIVxPtyYRkMcIVM9hFRt_83YwcMiwfVx1ezwMQBPrBTXRx3JH1zqlakvSXNTIoHg9pvFhTN0vv5CLqeu3rV0P3DV0zohTty28itz8ZSWjNa41kxHilkx4AlbupJmi7w5Kv2eZdqFqK__v1TRqxUVG16nfJALObYlBppNe1u3upClf2oBsltT-iroLc4Ek3TrRpqpBnVG6MUTBKaEeNrhoDnRuP8HNqGu98I4560TED8Pg2nUvlQrayNaIpRm5VuRdqH3riJ4sRZyZ0E0IrrN5y3XvTwPAmbzjEIeZp48pDdNIRun7FWW9i5GybUqXtr7Utm0QpHysCxltUca_gXP_sK-nnVfOhx25bEmN-IzPiUk474JlU25uB2dUYqHUjhpGaMKDy8sf2Kbt_ASUEbQUKz1AA7OFoXHa0DXN9E6jhRobL-r_o_m4lWfq0Kdh48zYfpJ2om_3a6RwaphWTVVARh2ep_g5Emwb86uhyZg2tP8IM1JBib3xjVSLMi5NABD3UOEzv5Oq_mTnZlPWRsdGz4pDdYAfigAlPo_EJ7S2JBhGkNB=w1280-h720-no?authuser=0'
    q.questionBase, q.answerBase = questionBase, answer
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()
    
def eb_bf_angle_same_segment_equal13():
    people = peopleGen()
    num = randint(30, 60)
    true_tuple = ("angles at points c and d are the same", "angles at points e and f are the same", "if you know the angles at points c or d, you can calculate the angles at points e or f", "angle c plus angle e equals 180 degrees", "angle c plus angle f equals 180 degrees", "angle d plus angle e equals 180 degrees", "angle d plus angle f equals 180 degrees", "if the angle at point c were {num} degrees, the angle at point e or f would be {180-num} degrees", "if the angle at point e were {180-num} degrees, the angle at point c or d would be {num} degrees")
    false_tuple = ("angles at points c and d are different", "angles at points e and f are not the same", "if you know the angles at points c or d, you can't calculate the angles at points e or f", "angle c plus angle e equals 90 degrees", "angle c plus angle f equals 270 degrees", "angle d plus angle e equals 270 degrees", "angle d plus angle f equals 90 degrees", "if the angle at point c were {num} degrees, the angle at point e or f would be {90-num} degrees", "if the angle at point e were {270-num} degrees, the angle at point c or d would be {num} degrees", "the angles at points c and f are the same", "the angles at points d and f are the same", "the angles at point c and e are the same", "the angles at points d and e are the same")
    choice = randint(0,1)
    answer = "Correct" if choice == 1 else "Incorrect"
    statement = true_tuple[randint(0,len(true_tuple)-1)] if answer == "Correct" else false_tuple[randint(0,len(false_tuple)-1)]
    questionBase = [
        f"In the diagram above, line ab is a chord.",
        f"Points c, d, e and f are where lines originating at the ends of the chord meet the circumference.",
        f"{people[randint(0,len(people)-1)]} says that {statement}.",
        f"Is this statement correct or incorrect?"]
    q = cf.Question(cf.currentFuncName())
    q.hint ="The angle made at the centre of a circle is exactly double the angle at the circumference of the circle from the same two points at the ends of a chord."
    q.piclink = 'https://lh3.googleusercontent.com/tmMgkzlScopCWTzUmFuqIK_tX2ik2Svof6vzdEc82fI9ylg7_qxeuzM14c8eIPBJrRflgK5mByd7Ny50vUfMpLEAMR7AhKXu1X1H46LU8sIUdaAjw8dpLxy8c_FkGZSxA1365QlZXNLXp5egtyG-ZsNPEgWGuLxDylIGS_jpZ6UZgDutTkmLjMPjdgjXLYl9eqTYUfrSq3pd6ZpYS9za6NbPHpo0BtTqfC67ysAxhggMzkQAH7uWtLcrHJRNYSrXxJqpORhW6eFWYGiDt2w-Zo6b9OrN0tYV54pyvtcHlSuD7LvOJ3FAQpzeaJ9GqxraR9NPzySGCd7JbttHa-za-tRloHrenvnIlCR_2zsqjgTMv4yNyT5DZcBbKisweuZLbZ9nkkzdroiH15RJwOjwDdaZiw_FXFEN8WpvvWKJAV_o2MKoq8cK2C5zMCO6dS4qJD3kih-uuVJH0ysW9sypzBZUkwBkmm0o1ATBBNO6hGVkVUvIIWpkksLLJ5Nn6Du1Hq7HhxhpJMsIlxxD9Y0uYaoQJr6bDUTD5RujgXqNqq7Rhcw6Ex79Dk88md_gnTmDPButS-MjpkKBHx8FkGJVkeTUiYDAYydyPx8vXGu1VERXqsAwN-DcKceaMuXsdShQYdXA9d6C8A3FfxlWtm8kp90h17ikJRes_W9-jk57Y6BrNIX0T4t7YhLfeJ0aZOgfNJvxg9H8VAA9muzoCpQyEPsn=w1280-h720-no?authuser=0'   
    q.questionBase, q.answerBase = questionBase, answer
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()
    
def eb_bg_opposite_cyclic_quadrilateral13():
    people = peopleGen()
    num = randint(30, 60)
    true_tuple = ("angles at points a and d add up to 180 degrees", "angles at points c and b add up to 180 degrees", "if you know angle at point a, you can work out angle at point d", "knowing point a won't help in calculating point b", "knowing point c won't help in calculating point d")
    false_tuple = ("angles at point a and d are equal", "angles at points c and d are equal", "angles a and b add up to 180 degrees", "angles c and d add up to 180 degrees", "if you know point a, you can calculate point b", "if you know point c, you can calculate point d")
    choice = randint(0,1)
    answer = "Correct" if choice == 1 else "Incorrect"
    statement = true_tuple[randint(0,len(true_tuple)-1)] if answer == "Correct" else false_tuple[randint(0,len(false_tuple)-1)]
    questionBase = [
        f"In the diagram above, points a, b, c and d make a cyclic quadrilateral.",
        f"{people[randint(0,len(people)-1)]} says that {statement}.",
        f"Is this statement correct or incorrect?"]
    q = cf.Question(cf.currentFuncName())
    q.hint ="The angle made at the centre of a circle is exactly double the angle at the circumference of the circle from the same two points at the ends of a chord."
    q.piclink = 'https://lh3.googleusercontent.com/4DGd1ZgsNDYPnpVCfbDpx3e_a-wLSJb2fdcK2zAiQhha7OegWOIKMCWovOZ7F7YbSPd2r4XMZSyls2tr_YRlBc5E5VThRatnZo8Gh59OwPdA7fmvlfIlHAUs1wzgpdsjcVsRJD5DBLuO3F4t7z47V5w2r-Gy1gF986a6o7M_M0bkWsTGjAviwg1HGN_D0POhhEK7auaXcYJ67M8rC4egCZE51ZiopFdMMGZw_EMNFf83wBHTRT1s5C35-istdjeZLJXeXWgBzqsbfZOqwcXXaR1-KxvqBLXbzUdll2FliWeUjtmH-u2HmGbdJ9HODl0PUiDbBoDiGiOkNQpl-myhsVTcIWBTGoAotXbvoXN-DyLBe-I3Gu4YUxwmGMX6a-15h-CWR3SFdeAkFfw-neRtB8cp8C9KNJ7l2bS1FLgAZoLJgVlRz1vtLNdMQIViM3-r79uZaZe_lsewj3H_pvIwCkY3CE9XlsqW3MP4bXIP1Ee2ncWF0Red0mVuIDlL9bRwd8ARH96fnN-JPySiIUHWdC4x9Ba1NBbvZSuOIccEHDI29DARWSLIbINAqCWijsjSGcn4l9szsIRy9FXhZ--VMK27DYv9_R13Tjayx5A8aPNqIAgZlU9Z5G5tjFGCR5RqhAZktxLaVJlw32fz3C5REubSHv-14df-Q1Jps9_N3aDId3FllW6NhhAQX8F_uVjxrdLDg70oTjoxFranMqnQ-cY6=w1280-h720-no?authuser=0'
    q.questionBase, q.answerBase = questionBase, answer
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()
    
def eb_bh_tangents_point_same_length13():
    people = peopleGen()
    num = randint(30, 60)
    true_tuple = ("the two triangles in the diagram above are congruent", "line cb is the same length as line db", "line ac is the same length as line ad", "angle acb is a right angle", "angle adb is a right angle", "triangle acb is a right angled triangle", "triangle abd is a right angled triangle", "both of the triangles are right angled triangles", "both of the angles at point a are the same", "both of the angles at point b are the same")
    false_tuple = ("the two triangles in the diagram above have different dimensions", "line cb is the same length as line ab", "line ac is the same length as line ab", "angle acb is not a right angle", "angle adb is not a right angle", "triangle acb is an equilateral triangle", "triangle abd is not a right angled triangle", "both of the triangles are slightly different", "the angles at point a the same as points c and d", "the angles at point b are different")
    choice = randint(0,1)
    answer = "Correct" if choice == 1 else "Incorrect"
    statement = true_tuple[randint(0,len(true_tuple)-1)] if answer == "Correct" else false_tuple[randint(0,len(false_tuple)-1)]
    questionBase = [
        f"In the diagram above, lines bc and bd are tangents drawn from the same point.",
        f"{people[randint(0,len(people)-1)]} says that {statement}.",
        f"Is this statement correct or incorrect?"]
    q = cf.Question(cf.currentFuncName())
    q.hint ="The angle made at the centre of a circle is exactly double the angle at the circumference of the circle from the same two points at the ends of a chord."
    q.piclink = 'https://lh3.googleusercontent.com/T9JkN8cvwz6bZyO-Gza9_p6bvAg3PSu_w5h5oTu0FJ_S_7wjdf1JNrpCkqOMiek-oQdCtnl5xQWebOsW-WIbjVTGzq4ydxmCM4R4cBt4WA7iDAyPHMTNUDRFwTCArxTvJo9cfE0kLOl6UK98UuDtKZtO8vitdm6DWwZkGxMZyIVxPtyYRkMcIVM9hFRt_83YwcMiwfVx1ezwMQBPrBTXRx3JH1zqlakvSXNTIoHg9pvFhTN0vv5CLqeu3rV0P3DV0zohTty28itz8ZSWjNa41kxHilkx4AlbupJmi7w5Kv2eZdqFqK__v1TRqxUVG16nfJALObYlBppNe1u3upClf2oBsltT-iroLc4Ek3TrRpqpBnVG6MUTBKaEeNrhoDnRuP8HNqGu98I4560TED8Pg2nUvlQrayNaIpRm5VuRdqH3riJ4sRZyZ0E0IrrN5y3XvTwPAmbzjEIeZp48pDdNIRun7FWW9i5GybUqXtr7Utm0QpHysCxltUca_gXP_sK-nnVfOhx25bEmN-IzPiUk474JlU25uB2dUYqHUjhpGaMKDy8sf2Kbt_ASUEbQUKz1AA7OFoXHa0DXN9E6jhRobL-r_o_m4lWfq0Kdh48zYfpJ2om_3a6RwaphWTVVARh2ep_g5Emwb86uhyZg2tP8IM1JBib3xjVSLMi5NABD3UOEzv5Oq_mTnZlPWRsdGz4pDdYAfigAlPo_EJ7S2JBhGkNB=w1280-h720-no?authuser=0'
    q.questionBase, q.answerBase = questionBase, answer
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()
    
def eb_bi_alternate_segment_theorem13():
    people = peopleGen()
    num = randint(30, 60)
    true_tuple = ("angles a and e are the same", "angles b and d are the same", "angles c and f are the same", "angles c, b and e add up to 180 degrees", "angles d, f and a add up to 180 degrees", "if you know angles f and a , you can calculate all angles in the triangle in the diagram", "if you know angles d and e, you can calculate all angles in the triangle")
    false_tuple = ("angles a and e are not the same", "angles b and d are not the same", "angles c and f are not the same", "angles c, b and e add up to 360 degrees", "angles d, f and a add up to 90 degrees", "if you know angle f, you can calculate all angles in the triangle in the diagram", "if you know angles e, you can calculate all angles in the triangle")
    choice = randint(0,1)
    answer = "Correct" if choice == 1 else "Incorrect"
    statement = true_tuple[randint(0,len(true_tuple)-1)] if answer == "Correct" else false_tuple[randint(0,len(false_tuple)-1)]
    questionBase = [
        f"In the diagram above, lines bc and bd are tangents drawn from the same point.",
        f"{people[randint(0,len(people)-1)]} says that {statement}.",
        f"Is this statement correct or incorrect?"]
    q = cf.Question(cf.currentFuncName())
    q.hint = "The angle made at the centre of a circle is exactly double the angle at the circumference of the circle from the same two points at the ends of a chord."
    q.piclink = 'https://lh3.googleusercontent.com/jC9ogzmxloCgk3MLbRg0vBoDtcc2IQJtraHoORMu93Mf4iotbSPKnozqJnT3tjGAuune1uZLXkGY550LYs9xsFt72ejtkPdiy830B1Oynqx7AbGn8GFrdjcXjUQUSjZJnPA343T8YPROYeizwcNK4kJKce-3TgMOn297arr21spHAv6SXiba9YoaAXTEomK32xmILxlPwnKf1gUbWBVP-4Q5VZ_fjm27DNfLOyUCdZ3oEgkDhxd7lNi2GM8B2vBFEU-n5JdwbrDTCD20Q__Hef3hyMQmpHqea2A45SocGIvdMaNuAtHJhEfjFpNEH_hxWciP13u2BtzsFFpUvN2TzK-f9D154Rgz-5o5B3Nzk0hSVxBHpebSZoCMDHHznAvGehQ7YxuNJzW0R4nyG50WunQSpNbWOwK57S8XpbDwH9e1Ql5RLUUTKH2RUf8HdNuN3k3texdL7opo0pMiMmBP9r21kqarwx5saJRd6KWFtM6qI9RanJVDXvCwdKQcm2dtxHJ0B_Vyt2I9FKJxSTP--7iaINPjWBIariWsrKN4G-IQ4ucxbozbC0yPPeI8UGWzxhTxFel7wNbTBOYF5hMqymWCbRG0JNpHUQv3nP6x_BwAJl5vxoGLqJA06aAoSMqcTUPgqwCv5BX0lvEzCJQcHk8uZkdf9euB5D-3qwd5lSKQFBhEt4s-fOrYujrVjicScqZR4sf00-FPsx594VWR_k1w=w1280-h720-no?authuser=0'
    q.questionBase, q.answerBase = questionBase, answer
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()
    
def eb_ca_circle_problem113():
    abc = randint(30, 80)
    aoc = abc * 2
    adc = 180 - abc
    answer = [["ABC", abc], ["AOC", aoc], ["ADC",adc]]
    choice = randint(0, len(answer)-1)
    choice2 = choice
    while choice2 == choice:
        choice2 = randint(0, len(answer)-1)
    questionBase = [
        f"A,B,C and D are points on the circumference of the circle in the diagram and O is the centre.",
        f"Angle {answer[choice][0]} = {answer[choice][1]}\u00B0. Find the value of {answer[choice2][0]}."
    ]
    answer = f"{answer[choice2][1]}\u00B0"
    q = cf.Question(cf.currentFuncName())
    q.piclink = 'https://lh3.googleusercontent.com/e277k9U_U99WYWhhg8h0IksOAPUM1WbVlzEjmvFgJkwHEUMfMBVA3RvTRiY20n0c0Rd0O5f17TNnAE0IJjsSbEtM1LHRp_tkr0e7rAw16DL5sLcKQbhWOBwOgpYIE0uakQiXgEnUKbV7hBsmiFqbQPpGd4QT8Jq_QRr2R0UfSPtTc61elJhPnaEW9x5SULMQLcOQU8SpqQexIRqfuzEjojiBb3K2-koYcVz1fHe6n8f3yX4UXONJ2k1Ad4tFl8eqdaSIuDyEiY07Wctf4goBY2f2RtPg06pOQP1Mb-asTwxY1_hwBuJzBMxXuocWqxsbYObFtxKDg1TguPGTqzXfw2Ym9xEWYBoJk_xQAReJShBk0mEFVN1hZq9wzmXkSiBlVXTZw2qypBEWPeVhYmBFjtCgpy8DSm8mfa59U-92AOGsiWdzz5OrXKuB8f8qHC8O_1aQIpAsO_hb71Q7X36CgDfNZz1Sgki6gZufdGH987Qq48lSD_6RNuMwAqt5cOu72mJwaCpsf4UIuAOgTb54h4z6gMppJ7AvcXPUrrtOvkHJNQryUpQR8MatrvWy7AGVDKplV_PRD81MejhMZLpWaqN6gsU0Vpsq672CBv4xAjVAsXfTNk8incLAcDPRjdBNfKw4wW-A7yWG_w8Ml0S2o6SQWEpp4g47d_kxEvhq_ksleLblXaFWr2H_PvydC6eSHrPpxmjyFV0voDBp9bIr4qfK=w1280-h720-no?authuser=0'
    q.questionBase, q.answerBase = questionBase, answer
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()
    
def eb_cb_circle_problem213():
    abd = randint(30, 80)
    acd = abd
    adf = abd
    aed = 190 - abd
    answer = [["ABD", abd], ["ACD", acd], ["ADF",adf], ["AED",aed]]
    choice = randint(0, len(answer)-1)
    choice2 = choice
    while choice2 == choice:
        choice2 = randint(0, len(answer)-1)
    questionBase = [
        f"A,B,C,D and E are points on the circumference of the circle in the diagram.",
        f"Line FDG is a tangent and O is the centre.",
        f"Angle {answer[choice][0]} = {answer[choice][1]}\u00B0.",f"Find the value of {answer[choice2][0]}."
    ]
    answer = f"{answer[choice2][1]}\u00B0"
    q = cf.Question(cf.currentFuncName())
    q.piclink = 'https://lh3.googleusercontent.com/t9t82WwurVtpU85f4bdvSZTzO-PGqqoeyyTSLOjDm1HTHOunt6BJqH4qPHaqWyD7tAxKU7b1C_jLM6m5QOHThZ2t-3R1mL8bHuouGU6lZ6IoKZWtOEwhgZv2tYEsBSTzCyqJFVDhMwExTHJmECJTCt0KwVMPv2neKv8u6erpsDIqi_4urSYxQ064jQ1XC7zp_quPmJ10qJlz-taZthdTj9PtqwM6T0S2RVoHbMS2kyLr97GataNdbk8ZW3sJI0azaSXRJBYsw08iSzNPOTOeV6Ydtf9ePVcBV6f1jRvgUeg9t6owO7m9-_mppN79Mat-nvim_orkMk4PlLOdqApVRIEZSXH7UhqvLpH6JtBfz5FVHoW_66wo6oefsEf4SU76yShJjSKsJaNIfFMvDoacpJrCF4jhiRvUBYelO1NN8iI6l2xF2nq4YT5EeH8mXpZbCJ1KPfw82ok_wqsLlFLViQjOxAFUlK5JF_ohNM6DXENm1Vei1FLS0x270CXNVe8PFklz_glLQlY5zQkdmG8Mn-n6eNy9UmwlIfSeQJabZgXmCKj3HbblDk2h8gUo_jUuxo_aMYeLVVWhkJKR-lWdW5LxUmhuAJOa6EVEVj1VdpHTo0yKL_5QS0yLuCOZy1gDTnpKCBxxYyxpEtxAN92YFY2lf1nrjzynsbvTq4ICxHph_Vcv1gSq5Uw2SxtRw2OdDY8HDVR-anjchgl34XfEUhDX=w1280-h720-no?authuser=0'
    q.questionBase, q.answerBase = questionBase, answer
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()
    
def ec_aa_congruent_similar14():
    people = peopleGen()
    true_tuple = ("congruent means the same size and the same shape", "Similar means the same shape, but a different size", "in a congruent shape, all sides are the same length", "in a similar shape all angles are the same", "both congruent and similar shapes can be reflected or rotated", "similar shapes can be rotated or reflected", "congruent shapes can be rotated or reflected") 
    false_tuple = ("congruent and similar mean the same thing", "congruent means the same shape, but a different size", "similar means exactly the same shape", "in a similar shape, all sides are the same length", "in a congruent shape, all angles are the same but sides are different lengths", "neither congruent nor similar shapes can be reflected or rotated", "similar shapes cannot be rotated or reflected", "congruent shapes cannot be rotated or refelcted")
    choice = randint(0,1)
    answer = "Correct" if choice == 1 else "Incorrect"
    statement = true_tuple[randint(0,len(true_tuple)-1)] if answer == "Correct" else false_tuple[randint(0,len(false_tuple)-1)]
    questionBase = [
        f"{people[randint(0,len(people)-1)]} says that {statement}.",
        f"Is this statement correct or incorrect?"]
    q = cf.Question(cf.currentFuncName())
    q.hint ="Congruence means two shapes are the same size and shape. Similarity means that two shapes are the same shape, containing the same angles, but a different size"
    q.questionBase, q.answerBase = questionBase, answer
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()
    
def ec_ab_congruent_similar_diagrams14():
    people = peopleGen()
    congruent_tuple = ("congruent_circles", "congruent_squares", "congruent_pentagons", "congruent_lightning", "congruent_mouse") 
    similar_tuple = ("similar_circles", "similar_squares", "similar_pentagons", "similar_lightning", "similar_mouse") 
    neither_tuple = ("neither_pentagons", "neither_lightning", "neither_mouse") 
    choice = randint(0,2)
    if choice == 0:
        answer,diagram_choice = "Congruent",f"{congruent_tuple[randint(0,len(congruent_tuple)-1)]}"
    if choice == 1:
        answer,diagram_choice = "Similar",f"{similar_tuple[randint(0,len(similar_tuple)-1)]}"
    if choice == 2:
        answer,diagram_choice = "Neither",f"{neither_tuple[randint(0,len(neither_tuple)-1)]}"
    questionBase = f"In the diagram above, do the shapes appear to be congruent, similar or neither?"
    q = cf.Question(cf.currentFuncName())
    q.hint="Congruence means two shapes are the same size and shape. Similarity means that two shapes are the same shape, containing the same angles, but a different size. This is true even if the congruent or similar shape is rotated or reflected"
    q.diagram = f'/diagrams/gcsemaths/ec1_{diagram_choice}.jpg'
    q.questionBase, q.answerBase = questionBase, answer
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()
    
def ec_ac_congruent_triangle_rules24():
    people = peopleGen()
    true_tuple = ("two triangles are congruent if three sides are the same", "two triangles are congruent if two angles and a corresponding side match up", "two triangles are congruent if two sides and the angle between them match up", "two triangles are congruent if a right angle, the hypotenuse and one other side all match up", "two triangles are congruent if one rule out of SSS, AAS, SAS and RHS apply", "two triangles can be congruent if they are rotated", "two triangles can be congruent if they are reflected") 
    false_tuple = ("two triangles are congruent if two sides are the same", "two triangles are congruent if all three angles match up", "two triangles are congruent if all three sides are proportional", "two triangles are congruent if they are both right angled triangles", "two triangles are congruent if they are both equilateral", "two triangles cannot be congruent if one of them is rotated", "two triangles cannot be congruent if one of them is reflected") 
    choice = randint(0,1)
    answer = "Correct" if choice == 1 else "Incorrect"
    statement = true_tuple[randint(0,len(true_tuple)-1)] if answer == "Correct" else false_tuple[randint(0,len(false_tuple)-1)]
    questionBase = [
        f"Congruent means the same shape and size.",
        f"{people[randint(0,len(people)-1)]} says that {statement}.",
        f"Is this statement correct or incorrect?"]
    q = cf.Question(cf.currentFuncName())
    q.hint ="Congruence means two shapes are the same size and shape. Similarity means that two shapes are the same shape, containing the same angles, but a different size"
    q.questionBase, q.answerBase, q.diagram = questionBase, answer, None
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()
    
def ec_ad_congruent_triangle_rules_diagrams24():
    people = peopleGen()
    diagram_tuple = (["ec1_congtruent_triangle_sss1","Three sides are the same (SSS)"],["ec1_congtruent_triangle_sss2","Three sides are the same (SSS)"],
                     ["ec1_congtruent_triangle_aas1","Two angles and a corresponding angle are the same (AAS)"],["ec1_congtruent_triangle_aas2","Two angles and a corresponding angle are the same (AAS)"],
                     ["ec1_congtruent_triangle_sas1","Two sides and the angle between them match up (SAS)"],["ec1_congtruent_triangle_sas2","Two sides and the angle between them match up (SAS)"],
                     ["ec1_congtruent_triangle_rhs1","A right angle, the hypotenuse and one other side all match up (RHS)"],["ec1_congtruent_triangle_rhs2","A right angle, the hypotenuse and one other side all match up (RHS)"])
    choice = randint(0, len(diagram_tuple)-1)
    answer,diagram_choice = diagram_tuple[choice][1],diagram_tuple[choice][0]
    questionBase = f"The triangles above are congruent. What condition proves that this is the case?"
    q = cf.Question(cf.currentFuncName())
    q.hint ="A triangle is congruent if: three sides are the same OR two angles and a corresponding side match up OR two sides and the angle between them match up OR a right angle, the hypotenuse and one oter side all match up."
    q.diagram = f'/diagrams/gcsemaths/{diagram_choice}.jpg'
    q.questionBase, q.answerBase = questionBase, answer
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()
    
def ec_ba_similar_congruent14():
    people = peopleGen()
    true_tuple = ("congruent means the same size and the same shape", "Similar means the same shape, but a different size", "in a congruent shape, all sides are the same length", "in a similar shape all angles are the same", "both congruent and similar shapes can be reflected or rotated", "similar shapes can be rotated or reflected", "congruent shapes can be rotated or reflected") 
    false_tuple = ("congruent and similar mean the same thing", "congruent means the same shape, but a different size", "similar means exactly the same shape", "in a similar shape, all sides are the same length", "in a congruent shape, all angles are the same but sides are different lengths", "neither congruent nor similar shapes can be reflected or rotated", "similar shapes cannot be rotated or reflected", "congruent shapes cannot be rotated or reflected")
    choice = randint(0,1)
    answer = "Correct" if choice == 1 else "Incorrect"
    statement = true_tuple[randint(0,len(true_tuple)-1)] if answer == "Correct" else false_tuple[randint(0,len(false_tuple)-1)]
    questionBase = [
        f"{people[randint(0,len(people)-1)]} says that {statement}.",
        f"Is this statement correct or incorrect?"]
    q = cf.Question(cf.currentFuncName())
    q.questionBase, q.answerBase = questionBase, answer
    q.hint ="Congruence means two shapes are the same size and shape. Similarity means that two shapes are the same shape, containing the same angles, but a different size"
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()
    
def ec_bb_similar_congruent_diagrams24():
    people = peopleGen()
    congruent_tuple = ("congruent_circles", "congruent_squares", "congruent_pentagons", "congruent_lightning", "congruent_mouse") 
    similar_tuple = ("similar_circles", "similar_squares", "similar_pentagons", "similar_lightning", "similar_mouse") 
    neither_tuple = ("neither_pentagons", "neither_lightning", "neither_mouse") 
    choice = randint(0,2)
    if choice == 0:
        answer,diagram_choice = "Congruent",f"{congruent_tuple[randint(0,len(congruent_tuple)-1)]}"
    if choice == 1:
        answer,diagram_choice = "Similar",f"{similar_tuple[randint(0,len(similar_tuple)-1)]}"
    if choice == 2:
        answer,diagram_choice = "Neither",f"{neither_tuple[randint(0,len(neither_tuple)-1)]}"
    questionBase = f"In the diagram above, do the shapes appear to be congruent, similar or neither?"
    diagram = f'/diagrams/gcsemaths/ec1_{diagram_choice}.jpg'
    q = cf.Question(cf.currentFuncName())
    q.hint="Congruence means two shapes are the same size and shape. Similarity means that two shapes are the same shape, containing the same angles, but a different size. This is true even if the congruent or similar shape is rotated or reflected"
    q.questionBase, q.answerBase, q.diagram = questionBase, answer, diagram   
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()
    
def ec_bc_similar_triangle_rules24():
    people = peopleGen()
    true_tuple = ("two triangles are similar if all three angles match up", "all sides in one triangle are proportionalto the other", "any two sides are proportional and the angle between them is the same","two triangles can be similar if they are also rotated", "two triangles can be similar if they are also reflected") 
    false_tuple = ("two triangles are similar if all two angles match up", "all sides are the same length in both triangles", "any two sides are proportional","two triangles cannot be similar if they are also rotated", "two triangles cannot be similar if they are also reflected") 
    choice = randint(0,1)
    answer = "Correct" if choice == 1 else "Incorrect"
    statement = true_tuple[randint(0,len(true_tuple)-1)] if answer == "Correct" else false_tuple[randint(0,len(false_tuple)-1)]
    questionBase = [
        f"Similarity means the same shape, but different size.",
        f"{people[randint(0,len(people)-1)]} says that {statement}.",
        f"Is this statement correct or incorrect?"]
    q = cf.Question(cf.currentFuncName())
    q.hint ="Similarity means shapes are exactly the same shape, but can be different sizes as well as rotated or reflected."
    q.questionBase, q.answerBase, q.diagram = questionBase, answer, None
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()
    
def ec_be_all_angles_match_up14():
    a = randint(30, 50)
    b = randint(40, 60)
    c = 180 - a - b
    questionBase = [
        f"In the diagram above:",
        f"all angles a are {a} degrees,",
        f"all angles b are {b} degrees and",
        f"all angles c are {c} degrees.",
        f"Are these triangles similar, congruent or neither?"]
    answer = "Similar"
    q = cf.Question(cf.currentFuncName())
    q.piclink = 'https://lh3.googleusercontent.com/LoyaCmsdHDCDITElNwnDNSmTSbjifyX3H1p2k3Nhu16c284v95N_JdClb4OWUv8JHO3GLbLVyAf44Zowhx30YUwlgKVPmGPN8OBL9aYXBUglNi_Urp-6Nminppul9vpXiTHD5NCTXoNqzKkr6hb1NBu3ghBqvqSXVGS7v-4T8ZLj5M53P_WEhmJpqsDo3H4Bp9K8wHVTAAUWBFHaWbhmP4mjbfLQTN6Y1VsXA28kqjJdn07NmJ6Q7ReoJUwhVg1-pVH_1YViDZeAXYyfNgbQqj5vX_axDRNl-ZKljBqBwFFmkZmaX2dA7z-QjZh7hONSbfCZyKLXgCo2ighcU_54buI_mK76kxrFyNrLpBL8WAFdDf8wKZQL_5uDOFvwYStAm1XKEu7WOZdAN3KRQJwnrpxBMEgfLUED0eg9XbvoDz5A2gs023Sbre-XhYQab1Fa4j3iadfBkeMY0vV5WltNggDgujcZOZNBbZ07B-v9HeIpBsH_IAAZpAqN7T67JMJl0TQAUm0WGjBQ0Es_8Glby-cufI7tdc0TTwOnVLKX3E7x8cS0Dv__eFl0wuDn-_TpcEjypcPYke0hEkqUcuNIs9MqAsGzS-Ldx0t8zladHoDAt7_nRNIU9ghhxFNrhjHG_4SMR9dCw6BEytif8_QIOgJTfIcQWy2pSPLxzhRl6TEw_ISvYIfePiAKRnCTvFr7oorQ-aZVhDVErITvZVsVhtVG=w1280-h720-no?authuser=0'
    q.questionBase, q.answerBase= questionBase, answer
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()
    
def ec_bf_all_sides_match_up16():
    a = randint(8, 10)
    b = randint(6, 7)
    c = randint(3,5)
    y = a * 2
    x = b * 2
    z = c * 2
    questionBase = [
        f"In the smaller triangle above side a is {a}cm",f"side b is {b} and side c is {c}cm.",
        f"In the larger triangle, side y is {y}cm, side x is {x}cm and side z is {z}cm",
        f"Are these triangl similar, congruent or neither?"]
    answer = "Similar"
    q = cf.Question(cf.currentFuncName())
    q.piclink = 'https://lh3.googleusercontent.com/o0crrXesl_Qh9ldg3JQZKB83KP4UDUqb6oBDVXZNhOVT7lKZ4lynUB-0lwRgzKCgrh-kIoGZ8Uq9vIYzyE6vEKm9vwNyYkbmjUu1WGUlhM8XJdOSBZmNl00H_N-QqUNSjoIjtPiIBQke9fT4n1_jnX2_fyBCV_C-Dk1vOoWfs7iv-yModEEoqOfBc2gqqUzfSaX1UG9L1L_I01dPy2nIjgIp7hyhcvt6m9ylqmnITB0CjsCHUUFsEvqjIOD9Bi8XQ1zEs2bX2Cv3TIM-CY5FeK35mHnQErTaS6BtDn-pYcvNl3oh1noJch7808F2EjOd86Bv1siu1e9t0_YEoSnJHqXkAvdd_z-ADwNV3eQuWSHPpk9YVWuvIRZntYSooffohgnLKI0rcKIlMdz85nCLKndIyzL_JFcpCzs9V5uEZWi66j7OT0TPqWSa4aAVXBJgj7Cw7U3D8GtSKO-_g6SXdSY7nAegOfdupJzxq-u4AUxAhOhfJLLRufk2wQx_ygFEBkleBJyx7FWGnhfxzcWdj2lxr2t8NJbJEpia7uLHkbtA2lPWzDXr-RSBWIPwWogcZlFy43glHRMRgw4iFflpti85zArIMFluOXZE2hqumjTBG0XsqULy06lE9CWBC7Nds3lYJcyAQuWW-jq4GmzdkHel4Is5n5NuLklobFdSp-eX7gj7L0Iy0yI-OUNemHndliTOkalxQ1d3VtVPGYVZT7Mx=w1280-h720-no?authuser=0'
    q.questionBase, q.answerBase = questionBase, answer
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()
    
def ec_bg_two_sides_one_angle16():
    n = randint(20,50)
    a = randint(15, 20)
    b = randint(10, 14)
    y = a*2
    x = b*2
    questionBase = [
        f"In both triangles above, angle n is {n} degrees. Side a is {a}cm, side b is {b}cm, side y is {y}cm and side x is {x}cm.",
        f"Are these triangles similar, congruent, or neither?"]
    answer = "Similar"
    q = cf.Question(cf.currentFuncName())
    q.questionBase, q.answerBase = questionBase, answer
    q.piclink = 'https://lh3.googleusercontent.com/utoj7fHjf6hyADXOpBAcY8G6ky07wiW9AUWThi3zmoND0iFA51KMv9Gij_CXRtLMI7fS6txCRDmMKH6O9XeZM-dLigkkTIlAjGWT3BTfIpQzToniLWpIOKo3qNDyyDgtDm4anAgL1YsTf8yq7fFMOvLwUv7pDn_w1-WIZOxRYb3daEJxJ0KR6Sedg-_gKsWuPT7qe0gIDNniJ2PbvkV-Y8-8ZbWdIjhN6ldgBqmgZasItcwpTqPP5NXv0p0YB8NtFEqoyLeyRnypTL4S9Tbg0WwN-tyY9Kfz1fSPfEKz5wYoE2Zwm_qwz4HmhHE6WBD_KBmX62amMX8v3epoVR2mOZYhP_yRu9Ib17DvxOIZI9WNAG7YriSynSoRrJfW3cx-u2Xy7l0SZwix8F2aLPr7-Cts9dyjrj4k9cLSinYXHBpUM5KZRCr7h6WPzBbHqYkSTT3egs7FoBROVRlPkFu21tOYirygPCHaZS2NwqfZxQ7RKWYrWhVp0y7vtFOtzLrL6U3A7h1SjUm382F7UV4AgrlYdfKOZAC64BT872SKEx2hD3ce_Rv2KIh_UIMZGcJ8nih_lOmWpBdryKcdG1viREC_Yxe7GHf7pISyS3297p7_xOycpzHsKzqrrQ0ZA6VRca4fJ8nWbVgaYL0TLVxfnmDGHPvg363WfyfMCJMIMzyz7YSCdzC4LxLjN6YWoqz-XJzpJnxPTN0A7q4UUpqSfT39=w1280-h720-no?authuser=0'
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()
    
def ec_bh_all_angles_match_up_proof16():
    a = randint(30, 50)
    b = randint(40, 60)
    c = 180 - a - b
    questionBase = [
        f"In the diagram above, all angles a are {a} degrees, all angles b are {b} degrees and all angles c are {c} degrees.",
        f"How do you know these triangles are similar?"]
    answer = "All three angles match up"
    q = cf.Question(cf.currentFuncName())
    q.questionBase, q.answerBase = questionBase, answer
    q.piclink = 'https://lh3.googleusercontent.com/LoyaCmsdHDCDITElNwnDNSmTSbjifyX3H1p2k3Nhu16c284v95N_JdClb4OWUv8JHO3GLbLVyAf44Zowhx30YUwlgKVPmGPN8OBL9aYXBUglNi_Urp-6Nminppul9vpXiTHD5NCTXoNqzKkr6hb1NBu3ghBqvqSXVGS7v-4T8ZLj5M53P_WEhmJpqsDo3H4Bp9K8wHVTAAUWBFHaWbhmP4mjbfLQTN6Y1VsXA28kqjJdn07NmJ6Q7ReoJUwhVg1-pVH_1YViDZeAXYyfNgbQqj5vX_axDRNl-ZKljBqBwFFmkZmaX2dA7z-QjZh7hONSbfCZyKLXgCo2ighcU_54buI_mK76kxrFyNrLpBL8WAFdDf8wKZQL_5uDOFvwYStAm1XKEu7WOZdAN3KRQJwnrpxBMEgfLUED0eg9XbvoDz5A2gs023Sbre-XhYQab1Fa4j3iadfBkeMY0vV5WltNggDgujcZOZNBbZ07B-v9HeIpBsH_IAAZpAqN7T67JMJl0TQAUm0WGjBQ0Es_8Glby-cufI7tdc0TTwOnVLKX3E7x8cS0Dv__eFl0wuDn-_TpcEjypcPYke0hEkqUcuNIs9MqAsGzS-Ldx0t8zladHoDAt7_nRNIU9ghhxFNrhjHG_4SMR9dCw6BEytif8_QIOgJTfIcQWy2pSPLxzhRl6TEw_ISvYIfePiAKRnCTvFr7oorQ-aZVhDVErITvZVsVhtVG=w1280-h720-no?authuser=0'
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()
    
def ec_bi_all_sides_match_up_proof16():
    a = randint(8, 10)
    b = randint(6, 7)
    c = randint(3,5)
    y = a * 2
    x = b * 2
    z = c * 2
    questionBase = [
        f"In the smaller triangle above, side a is {a}cm, side b is {b}cm and side c is {c}cm.",
        f"In the larger triangle, side y is {y}cm, side x is {x}cm and side z is {z}cm.",
        f"How do you know these triangles are similar?"]
    answer = "All three sides are proprtional"
    q = cf.Question(cf.currentFuncName())
    q.questionBase, q.answerBase = questionBase, answer
    q.piclink = 'https://lh3.googleusercontent.com/o0crrXesl_Qh9ldg3JQZKB83KP4UDUqb6oBDVXZNhOVT7lKZ4lynUB-0lwRgzKCgrh-kIoGZ8Uq9vIYzyE6vEKm9vwNyYkbmjUu1WGUlhM8XJdOSBZmNl00H_N-QqUNSjoIjtPiIBQke9fT4n1_jnX2_fyBCV_C-Dk1vOoWfs7iv-yModEEoqOfBc2gqqUzfSaX1UG9L1L_I01dPy2nIjgIp7hyhcvt6m9ylqmnITB0CjsCHUUFsEvqjIOD9Bi8XQ1zEs2bX2Cv3TIM-CY5FeK35mHnQErTaS6BtDn-pYcvNl3oh1noJch7808F2EjOd86Bv1siu1e9t0_YEoSnJHqXkAvdd_z-ADwNV3eQuWSHPpk9YVWuvIRZntYSooffohgnLKI0rcKIlMdz85nCLKndIyzL_JFcpCzs9V5uEZWi66j7OT0TPqWSa4aAVXBJgj7Cw7U3D8GtSKO-_g6SXdSY7nAegOfdupJzxq-u4AUxAhOhfJLLRufk2wQx_ygFEBkleBJyx7FWGnhfxzcWdj2lxr2t8NJbJEpia7uLHkbtA2lPWzDXr-RSBWIPwWogcZlFy43glHRMRgw4iFflpti85zArIMFluOXZE2hqumjTBG0XsqULy06lE9CWBC7Nds3lYJcyAQuWW-jq4GmzdkHel4Is5n5NuLklobFdSp-eX7gj7L0Iy0yI-OUNemHndliTOkalxQ1d3VtVPGYVZT7Mx=w1280-h720-no?authuser=0'
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()
    
def ec_bj_two_sides_one_angle_proof16():
    n = randint(20,50)
    a = randint(15, 20)
    b = randint(10, 14)
    y = a*2
    x = b*2
    questionBase = [
        f"In both triangles above, angle n is {n} degrees.",
        f"Side a is {a}cm, side b is {b}cm, side y is {y}cm and side x is {x}cm.",
        f"How do you know these triangles are similar?"]
    answer = "Any two sides are proportional and the angle between them is the same"
    q = cf.Question(cf.currentFuncName())
    q.questionBase, q.answerBase = questionBase, answer
    q.piclink = 'https://lh3.googleusercontent.com/utoj7fHjf6hyADXOpBAcY8G6ky07wiW9AUWThi3zmoND0iFA51KMv9Gij_CXRtLMI7fS6txCRDmMKH6O9XeZM-dLigkkTIlAjGWT3BTfIpQzToniLWpIOKo3qNDyyDgtDm4anAgL1YsTf8yq7fFMOvLwUv7pDn_w1-WIZOxRYb3daEJxJ0KR6Sedg-_gKsWuPT7qe0gIDNniJ2PbvkV-Y8-8ZbWdIjhN6ldgBqmgZasItcwpTqPP5NXv0p0YB8NtFEqoyLeyRnypTL4S9Tbg0WwN-tyY9Kfz1fSPfEKz5wYoE2Zwm_qwz4HmhHE6WBD_KBmX62amMX8v3epoVR2mOZYhP_yRu9Ib17DvxOIZI9WNAG7YriSynSoRrJfW3cx-u2Xy7l0SZwix8F2aLPr7-Cts9dyjrj4k9cLSinYXHBpUM5KZRCr7h6WPzBbHqYkSTT3egs7FoBROVRlPkFu21tOYirygPCHaZS2NwqfZxQ7RKWYrWhVp0y7vtFOtzLrL6U3A7h1SjUm382F7UV4AgrlYdfKOZAC64BT872SKEx2hD3ce_Rv2KIh_UIMZGcJ8nih_lOmWpBdryKcdG1viREC_Yxe7GHf7pISyS3297p7_xOycpzHsKzqrrQ0ZA6VRca4fJ8nWbVgaYL0TLVxfnmDGHPvg363WfyfMCJMIMzyz7YSCdzC4LxLjN6YWoqz-XJzpJnxPTN0A7q4UUpqSfT39=w1280-h720-no?authuser=0'
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()
'''
def ec_ca_prove_congruency37():
    questionBase = "AB and AC are tangents to the circle with centre O and touch the circumference at points C and B. Prove that triangles ABO and ACO are congruent."
    answer = "Sides OB and OC are the same length as they are both radii. Both triangles have a right angle because the radii meet tangents AB and AC at right angles. OA is the hypotenuse of both triangles. Therefore, both triangles have a right angle, a matching hypotenuse and one other matching side. the RHS rule holds and triangles ABO and ACO are congruent."
    q = cf.Question(cf.currentFuncName())
    q.questionBase, q.answerBase = questionBase, answer
    q.piclink = ''
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()
'''
def ec_cb_prove_congruency37():
    questionBase = "Prove that triangles ABD and BCD are congruent."
    answer = "Side BD is the same in both triangles. Angles DAB and DCB are the same im both triangles, because opposite angles in a parallelogram are the same. Angles ABD and CBD are the same because they are made from an angle which is bisected by line BD. ADB and CDB are likewise the same. Therefore, SSS, AAS and SAS rule are all true"
    q = cf.Question(cf.currentFuncName())
    q.questionBase, q.answerBase = questionBase, answer
    q.piclink = 'https://lh3.googleusercontent.com/j5zrNx0TuvPoRcxKsrTNU576Jv5368UKxdQo6KxP3EaWUmKtLNOocIdvxbsEAld-wfUtEJAaWIrid7gt-onXYuEs8322Yu_vk1thZtruhTiExEDohUOIhf5MD1ui5D-uq_p5K1Gr_l4ZEPyqI2y29ym8P8WvEeOfg86Dw5OPXKcSGCRFfJNSGmbHVByN3vsJbLAjmTcVZLdjc9C2pqIP67icwf4QbHofMq-re_SofjN3LW0Cz5c4p4c9fQtPL9z_1k2XISUhu8pxqxa5rM-OIHXuOlYFknnUE9PLnSRK_0PH3GaPkO0kOhVJ4qsRxzVaItuCjV1cNB-A73GKdRcR_grq0-G14vDaVceDF1CzKvr3jc3ahwG1PjzBJf7UH4Rv9q4rJ_6t-QjEfWHBhD3sreaJmhNi55YRHlKtiy_Mg8ealnImyME_xFKx5IMly1SwH9uiXaxcl07HV1-bgR1QmjW321H_U4rKM3qsjQ4bWSCPsAZJVa00L7X5JbqFsQOaH_1bsz4qBnriCI2d3Wk3fK3OpEUHe5PhZh9V-pErtYqeEnMwxFM61YzE5d1Mv4lipB6QdTGgnSx41BdDJOohkaYZ00bnq-zkHNDNbEihIIJTURV9BplBR2tvmtaUtsUgblD2Ffq700ppJOJsXYAGfY-1ojzhVFBxzloLsKz9ZKRVe4j0hQrXtSMeY6YyeaCifjSbtgAPf-ZCfsXiGIZK-qRA=w1280-h720-no?authuser=0'
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()
    
def ec_cc_prove_similarity26():
    questionBase = "Prove that triangles ABC and AED are similar."
    answer = "Angles ABC and ADE are alternate angles. BCA and AED are also alternate angles. Third angle in each triangle around point A will be 180 minus the other two angles. Therefore all the angles match up and the triangles are similar"    
    q = cf.Question(cf.currentFuncName())
    q.questionBase, q.answerBase = questionBase, answer
    q.piclink = 'https://lh3.googleusercontent.com/be_oqwDqww7uUQvd_HREOZT01Q3lktcMg8kJrVX0IoDyyjOZ0qDy1oz2yAHDgjxDw5tQ7bElWwueFUyCGPUvpvxebxE_U2jy4dRgUIjmz3OO5fZKr_LeU4Yd4YTBGvyvi5H_eU0xMPUYxndFPorWXo3T89iLs-4-b9HcFCa0R7rFHGzSAda8e44IV3RY8VmCwGc8JPZkPstkBBru0V1uqtyB6ZiOVNWGXq7AQzpdFGY4SRQhqCO4KQsyTvhKKDPyscF5EXe4sCdEKhB9aV6SDy_bSVCFgoAz6f6fpuKmeSh1Xu5pRTpiU5PLOQLEcSKqBlyqb807SduwbH8TJOyPF0XjkBP14UqL7l0mtwwEAuX8eGR-XqLSZ5EsPbs3UVtDMk2PQsYe9-aLGMDrHi75W_cPvGEKqLE_PX9bRBGCL_7qXNakzyZdsZyoliU5MnI4Z4qeMK9qPcCgFgNYU2JKwSzqAwjztinjB1-NyWsPMq8hRFkkqYcJTvMTFJJ6XtdKBEqPp1IwiqU9mLtWzROVVleqx1I8lucvg_BYPuRL-gh-F6cRFGr2K0moiYy-RFNB63k3otB-yxCxWEfWQtkKutuZarOxetAZ-2V1yXTTy4SK4KORsSClWuuJI8xP9PKPiq3WhSGdH4O3m9pO4H0cq4Xtv6k-cPV2d_GLl1muRaPUmtifAk3mXaMRrpx2u33LgCoGxzhcn3ZIn1ZkRyuKAkq2=w1280-h720-no?authuser=0'
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()
    
def ec_cd_use_similarity26():
    pronoun, people = completePeopleGen()
    action = ("lying down", "rolling around", "pretending to swim")
    place = ("sea", "park", "houses of parliament", "antarctic", "deasert", "shopping centre")
    object1 = ("rather tall cactus", "rose bush", "rather large dog", "statue of David Beckham", "large ice cream stand", "rather large kebab van", "rock", "large cabage")
    object1height = randint(2, 8)
    object1dist = randint(10, 20)
    object2 = ("lighthouse", "block of flats", "decorative column", "flag pole", "helter skelter", "dinosaur skeleton")
    object2dist = randint(25, 40)
    object2height = (object2dist / object1dist) * object1height
    action = action[randint(0,len(action)-1)]
    place = place[randint(0,len(place)-1)]
    object1 = object1[randint(0,len(object1)-1)]
    object2 = object2[randint(0,len(object2)-1)]
    questionBase = [
        f"The diagram above shows {people} {action} in the {place}.",
        f"Currently, {pronoun} is {object1dist}m (length Y) from a {object1} at A, the top of which is {object1height}m above the ground.",
        f"There is a {object2} {object2dist}m (length Y) from {people} that is directly behind the {object1}.",
        f"To them, the top of the {object2} is in line with the {object1}.",
        f"Find the height of the {object2} (length B)?"]
    answer = f"{round(object2height, 2)}m"
    q = cf.Question(cf.currentFuncName())
    q.questionBase, q.answerBase = questionBase, answer
    q.piclink = 'https://lh3.googleusercontent.com/DOj9es65zDXn-1VEizFDrAxYlUnEbyxxbu2-jugFnddaMjN8tIO5x5eqv1G5BFEK5F3q0oTbNgnP3esanDg1GMVO6M6T89fiHm0EAaOtVpL7y5KEeHiRx5YqQUeunWEpUoDfiZFPOaDc9YxBCQfYW7U2OOFlxT8Iy4wF4CTLEIaWPz0qchSjN28fkHb00Hnm6b6MTmiiNmPbMJipv5IA3Pc5MiI0ChR765z6S79njh5bylduRQ6BCVnPUfEwCk443Xn0VfMxmi54h4hzTfub58fupierbFlEn7XY62VqG8A-N-aHifhZurRxhm-84z4ZULeNcmbVwpQDGgrjw2nutoqWIp9o9LPAujtLG8MEkDQj1lZM9IW7y3ykb6KVfBouaVR0IsfS30ZCZa0WeqIN0tV5bEjh7V2vTI0EPKVEtjdqnUL4Ulg1cQ6jO4qL1LqDdWfXguy4vVizTVHRX8UjPSM5QqjYPlH7nSePjJoWdUeVNPFzPClWAhhuKpsqEp-Jq5lCoCEuj923-q5EldV1_FAnJ1pe-NLowOWOnynrtjG81c9LZKxRQY95_65nj5uW28uW-Xzm-EA98x6M1FEGu5rpCzxSBCe5P-B6cik45FVL-F1xiX8zkP9QwOpAujy9pLZ838mpMgJz7SlyBL2xCkjIKb3KsJQKmYZtlu1nlqeKcJ6Ri5KhCxY1kyw4VC4crENCTeRqgMlfEeE_NVx_Df8I=w1280-h720-no?authuser=0'
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()
    
def ec_ce_use_similarity26():
    de = randint(15, 20)
    bc = randint(8, 12)
    ab = randint(17, 23)
    ad = round(de/bc*ab, 2)
    lengths = ((de,"DE"),(bc,"BC"),(ab,"AB"),(ad,"AD"))
    choices = []
    num = randint(0, len(lengths)-1)
    for i in range(len(lengths)):
        while num in choices:
            num = randint(0, len(lengths)-1)
        choices.append(num)
    questionBase =[
        f"In the diagram above:",
        f"{lengths[choices[0]][1]} = {lengths[choices[0]][0]}cm,",
        f"{lengths[choices[1]][1]} = {lengths[choices[1]][0]}cm",
        f"and {lengths[choices[2]][1]} = {lengths[choices[2]][0]}cm.",
        f"Find the length of {lengths[choices[3]][1]}."]
    answer =f"{lengths[choices[3]][0]}cm"
    q = cf.Question(cf.currentFuncName())
    q.questionBase, q.answerBase = questionBase, answer
    q.piclink = 'https://lh3.googleusercontent.com/be_oqwDqww7uUQvd_HREOZT01Q3lktcMg8kJrVX0IoDyyjOZ0qDy1oz2yAHDgjxDw5tQ7bElWwueFUyCGPUvpvxebxE_U2jy4dRgUIjmz3OO5fZKr_LeU4Yd4YTBGvyvi5H_eU0xMPUYxndFPorWXo3T89iLs-4-b9HcFCa0R7rFHGzSAda8e44IV3RY8VmCwGc8JPZkPstkBBru0V1uqtyB6ZiOVNWGXq7AQzpdFGY4SRQhqCO4KQsyTvhKKDPyscF5EXe4sCdEKhB9aV6SDy_bSVCFgoAz6f6fpuKmeSh1Xu5pRTpiU5PLOQLEcSKqBlyqb807SduwbH8TJOyPF0XjkBP14UqL7l0mtwwEAuX8eGR-XqLSZ5EsPbs3UVtDMk2PQsYe9-aLGMDrHi75W_cPvGEKqLE_PX9bRBGCL_7qXNakzyZdsZyoliU5MnI4Z4qeMK9qPcCgFgNYU2JKwSzqAwjztinjB1-NyWsPMq8hRFkkqYcJTvMTFJJ6XtdKBEqPp1IwiqU9mLtWzROVVleqx1I8lucvg_BYPuRL-gh-F6cRFGr2K0moiYy-RFNB63k3otB-yxCxWEfWQtkKutuZarOxetAZ-2V1yXTTy4SK4KORsSClWuuJI8xP9PKPiq3WhSGdH4O3m9pO4H0cq4Xtv6k-cPV2d_GLl1muRaPUmtifAk3mXaMRrpx2u33LgCoGxzhcn3ZIn1ZkRyuKAkq2=w1280-h720-no?authuser=0'
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()
    
def ed_aa_area_triangle_quadrilateral_formulas11():
    formulas = (("triangle", "\u00bd \u00d7 base \u00d7 height OR \u00bdab sin (angle between a and b)"),
                ("paralellogram", "base \u00d7 height"),
                ("trapezium", "\u00bd ( top + base ) \u00d7 height"))
    choice = randint(0, len(formulas)-1)
    if randint(0,1) == 0:
        questionBase = f"What is the formula for the area of a {formulas[choice][0]}?"
        answer = f"{formulas[choice][1]}"
    else:
        questionBase = [
            f"The following formula will find the area for which shape:",
            f"{formulas[choice][1]}"]
        answer = f"{formulas[choice][0]}"
    q = cf.Question(cf.currentFuncName())
    q.questionBase, q.answerBase = questionBase, answer
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()
    
def ed_ab_area_triangles13():
    base = randint(4,12)
    height = randint(4,12)
    area = 0.5*base*height
    questionBase = [
        f"The triangle in the diagram (not to scale) has",
        f"a base of {base}cm and",
        f"a height of {height}cm.",f"Find the area."]
    answer = f"{area}cm\u00b2"
    q = cf.Question(cf.currentFuncName())
    q.questionBase, q.answerBase = questionBase, answer
    q.piclink = triangle()
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()
    
def ed_ac_area_parallelogram13():
    base = randint(4,12)
    height = randint(4,12)
    area = base*height
    questionBase = [
        f"The parallelogram in the diagram has",
        f"a base of {base}cm and",
        f"a height of {height}cm.",
        f"Find the area."]
    answer = f"{area}cm\u00b2"
    q = cf.Question(cf.currentFuncName())
    q.questionBase, q.answerBase = questionBase, answer
    q.piclink = parallelogram()
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()
    
def ed_ad_area_trapezium23():
    a = randint(3, 12)
    b = randint(3, 12)
    while b == a: b = randint(3, 12)
    h = randint(3, 10)
    area = 0.5*(a+b) * h
    questionBase = [
        f"The trapezium in the diagram has a base of {b}cm and a height of {h}cm.",
        f"Find the area."]
    answer = f"{area}cm\u00b2"
    q = cf.Question(cf.currentFuncName())
    q.questionBase, q.answerBase = questionBase, answer
    q.piclink = trapezium()
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()
    
def ed_ae_area_triangles23():
    base = randint(4,12)
    height = randint(4,12)
    area = 0.5*base*height
    values = (("base", base, "cm"),("height", height, "cm"),("area", area, "cm\u00b2"))
    choices = []
    num = randint(0, len(values)-1)
    for i in range(len(values)):
        while num in choices:
            num = randint(0, len(values)-1)
        choices.append(num)    
    questionBase = [
        f"The triangle in the diagram has",
        f"a {values[choices[0]][0]} of {values[choices[0]][1]}{values[choices[0]][2]} and",
        f"a {values[choices[1]][0]} of {values[choices[1]][1]}{values[choices[1]][2]}.",
        f"Find the {values[choices[2]][0]}."]
    answer = f"{values[choices[2]][1]}{values[choices[2]][2]}"
    
    q = cf.Question(cf.currentFuncName())
    q.questionBase, q.answerBase = questionBase, answer
    q.piclink = triangle()
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()
    
def ed_af_area_parallelogram24():
    base = randint(4,12)
    height = randint(4,12)
    area = base*height
    values = (("base", base, "cm"),("height", height, "cm"),("area", area, "cm\u00b2"))
    choices = []
    num = randint(0, len(values)-1)
    for i in range(len(values)):
        while num in choices:
            num = randint(0, len(values)-1)
        choices.append(num)
    questionBase = [
        f"The parallelogram in the diagram has",
        f"a {values[choices[0]][0]} of {values[choices[0]][1]}{values[choices[0]][2]} and",
        f"a {values[choices[1]][0]} of {values[choices[1]][1]}{values[choices[1]][2]}.",
        f"Find the {values[choices[2]][0]}."]
    answer = f"{values[choices[2]][1]}{values[choices[2]][2]}"
    q = cf.Question(cf.currentFuncName())
    q.questionBase, q.answerBase = questionBase, answer
    q.piclink = parallelogram()
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()
    
def ed_ag_area_trapezium24():
    a = randint(3, 8)
    b = randint(5, 12)
    while b == a: b = randint(3, 12)
    h = randint(3, 10)
    area = 0.5*(a+b) * h
    values = (("the top length", a, "cm"),("the bottom length",b, "cm"),("height",h, "cm"),("the area", area, "cm\u00b2"))
    choices = []
    num = randint(0, len(values)-1)
    for i in range(len(values)):
        while num in choices:
            num = randint(0, len(values)-1)
        choices.append(num)
    questionBase = [
        f"In the trapezium above,",
        f"{values[choices[0]][0]} = {values[choices[0]][1]}{values[choices[0]][2]},",
        f"{values[choices[1]][0]} = {values[choices[1]][1]}{values[choices[1]][2]} and",
        f"{values[choices[2]][0]} = {values[choices[2]][1]}{values[choices[2]][2]}.",
        f"Find the {values[choices[3]][0]}."]
    answer = f"{values[choices[3]][1]}{values[choices[3]][2]}"
    q = cf.Question(cf.currentFuncName())
    q.questionBase, q.answerBase = questionBase, answer
    q.piclink = trapezium()
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()
    
def ed_ai_area_trapezium_problem25():
    x = randint(3,9)
    area = x * x * 2
    values = (("x", x, "cm"),("the area", area, "cm\u00b2"))
    choices = []
    num = randint(0, len(values)-1)
    for i in range(len(values)):
        while num in choices:
            num = randint(0, len(values)-1)
        choices.append(num)
    questionBase = [
        f"The shape above shows a square with sides of length x cm drawn inside an isosceles trapezium",
        f"The base of the trapezium is three times as long as one side of the square.",
        f"If {values[choices[0]][0]} = {values[choices[0]][1]}{values[choices[0]][2]},",
        f"find the value of {values[choices[1]][0]}."]
    answer = f"{values[choices[1]][1]}{values[choices[1]][2]}"
    q = cf.Question(cf.currentFuncName())
    q.piclink = 'https://lh3.googleusercontent.com/SVGg0xYnj-H0g0UE5VAVsPVlc4J7KoNCHpjCANJgLp-DcP17IkN4RcRJUhA30VFnFqgoKY9x1IlRGGzOm6CKNl2kNz_mFykPrlJleY3bPa6oRm-ECo9gps8GDl8veVKrDjqrvp5CGEtoOoq3ZZPvNHN4mEwrl_0d_ToQBLpiP3_cVFMJxDUwiGNvRXmjts9is5im2DmXnr-8gYQFtmWdxHplmgNKSJd--zJ5ysgNpf7cuEoEiaW1gF1Lm-xBYEmx6yplYa2MIO_sr-s5X0JbHI42ygU3RSAvyUYK5ljvWRbRONaej7zmXUOP6HYPwka5JfJ6LxTPM6cB6qPwNRHJiO617QhG6yFhWQuJ5SD2LjQznDHn9mD1ZkzmuJr6ECmqg_02BMyKHVjc7P1INQ9XW3glYR6z5_chEbUto4t_oa4v6BOIPzXTmJ-40vUHW8Bvc6EHo-czEorOceYz0VBglv-REmvE9DhQJIQlSDa88IFlorYu_oE2OyqW0aLQMgERJCNvd2i4Br0aCMeW9YUPHFA6kHnL2L6stqcdnWzqUP89cn9Q293wL9TURM3FLRhraINHHqd0OOLyvl1BLP0CTu0Nv0zzoMNOSpe5wfWBYkBtIHGOcTpdRt5vJX3Z-KPOMzUllgpcXHcv7rTquhvESfJ4Mj3BfijNzpBWnXPfUtyxp9O2Ni5oQxbPv--PptTqfTmzm-dE5r_DDsdZMFwi1PiO=w1280-h720-no?authuser=0'
    q.questionBase, q.answerBase = questionBase, answer
    q.piclink = parallelogram()
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()
    

def ed_aj_area_triangle_rectangle24():
    h = randint(3,8)
    b = randint(8, 20)
    area_tri = 0.5*h*b
    y = randint(3, 10)
    x = round(area_tri / y, 2)
    values = (("h", h), ("b", b), ("y", y), ("x", x))
    choices = []
    num = randint(0, len(values)-1)
    for i in range(len(values)):
        while num in choices:
            num = randint(0, len(values)-1)
        choices.append(num)
    questionBase = [
        f"The triangle and rectangle above have the same area.",
        f"{values[choices[0]][0]} = {values[choices[0]][1]}cm,",
        f"{values[choices[1]][0]} = {values[choices[1]][1]}cm and",
        f"{values[choices[2]][0]} = {values[choices[2]][1]}cm.",
        f"Find the value of {values[choices[3]][0]}"]
    answer = f"{values[choices[3]][1]}cm"
    q = cf.Question(cf.currentFuncName())
    q.piclink = 'https://lh3.googleusercontent.com/p1Nsyf4_0xziVqPUEyKPSePnl4R20i2b1iY62tQCFPrLPUf7PgtjsLK5viVXF-iW8mbccB7yScIH8cS-P7O21t9QTHyGJnR_5Wcw1b6D9lG0LVRf8iBSbrCROVJ5DKZvwUYZ6N-C_mFwQNmU8KS5zrymkjAuaRyvpwXpNSWImvzQ7mJFBagWPjUrSCB1hGtStA45IgvnW3Prrw77wPesbb3TvoPaYVsqiDnviAqBhIOfjPizR_ZdmTlbAZYOMqbcVwODs0V2e6X8x9-mVE4w1gIg2CvtyY_BnbpHZO11yaQh5gvbr2P49iJfZhGjmBktZg-tNItSU1FSXkHTSZphts2zRcCu2zxFBecQDQN-zrF6JjW7ua3BE3SrgA4cIm23JMlHZhYueOVmHMeEwjyz0zIJ_Z7uTnLywJGFWaonOeV6zvXL5sMw96g148Gh9fqhjziMM5mpCR9paDfHpHSn5Z57CmH9fXvaZXA29xjJfGGSSwkjOt0iiE3vSf4M9uzIpFDJXKPuudwlnwGQzm-vR766ueOtsZe85hjyhM44b4uI6kFhZ5AputpVwxjfPN9TXYc3HAxn3h7XHZCYkLjZkycbqjHLxpfFJrg35f4Dw339Xo_mxsitDUod64CDnnKhM_--_-tue-3umXmDpgJCuIk7VhGKl_-CgaFVAllmDCm0OSVxRcvqfZj3J6ZameThW1kGQzaAYJAa6xuN9tXsjFgV=w1280-h720-no?authuser=0'
    q.questionBase, q.answerBase = questionBase, answer
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()
    
def list_mangle(values):
    order, num = [], randint(0, len(values)-1)
    for i in range(len(values)):
        while num in order:
            num = randint(0, len(values)-1)
        order.append(num)
    return order   

def ed_ba_circumference_radius_and_diameter_12():
    values = (("a", "circumference"),("b","radius"),("c","diameter"))
    choice = randint(0,len(values)-1)
    if randint(0,1) == 0 :
        questionBase, answer = f"On the diagram above, what does {values[choice][0]} represent?", f"{values[choice][1]}"
    else: questionBase, answer = f"On the diagram above, which letter represents the {values[choice][1]}?", f"{values[choice][0]}"
    hint = "The circumference is the outside of the circle. The radius is a line from the centre of the circle to the circumference. The diameter is the line which passes through the middle of a circle and touches opposide sides of the circumference. It is like two radi going in opposite directions."
    video, website = None, "https://www.emathzone.com/tutorials/geometry/the-circle-and-parts-of-a-circle.html"
    q = cf.Question(cf.currentFuncName())
    q.piclink = 'https://lh3.googleusercontent.com/jRlx8Ljgw0jx-Ie1XzuRYGSx5cBIntZNxEv_GINalEbfVG_dnQDo_tw3ul9WTnaJyCnSRCyggL12_ns36ZvOQ-tsubM2Lg5-3ndLe1svj88OA0xWPv53fs9xfBBN46ebtKq-6cgrIKfKy3uHnD9n4J86e4Xm5dFrrvRdHE4aWuC4A_28nKl0uxzIg9fn_AN1GOLKTvHJZUUF6riHAuqDLMazhNOAeUxshej9GdpbEuykbWwf2SYyNPJTp8kTG1triy_VYwHI5JJmWKOvMrfe2BXZ1XuAwkKWOClhZpTYNkDA8gwH6fBA4oQwT9Dfd5EkdvdxDc3iiGDHYA4zrqFWWXBJl8ieIkRaOEec6Zvh0LQdJDQUy9yvNTayBLaf6vzv4Xw8enzyQ-Ab5Kdo9dRTF6CVssZkECWqJxKFjlFL7CJMrPHOlGZgWVKtO49rQTRz2YTgvei6sGDOYNevzeFJcJzIHCjWT7Sgx6QIVN6C4R4DXAHvhELEekWluWbux7QfJGBzMDNXNcvNlwKXq8nX5AtClYg4UO8dh4V05Vhy1KMsMnVZlaAU_0Kbf_ne9FzwBRysgmYJJZghFz4dS8EvgDMVW-4vEqntmWlurwGQg4J5G4X_Xo5WXw5zaE9_XH5Ia0-BXDV81Lp98LqjmbKd_EDGG_KKQOUQBGkvoxvTzKN78K_GzyHlJeS0ueHxpdnk6vztvKSl8xpVaGkzcUFYU4YL=w1280-h720-no?authuser=0'
    q.questionBase, q.answerBase, q.hint, q.website = questionBase, answer,hint, website
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()
    
def ed_bb_formulas_for_area_circumference_arcs_sectors_and_segments13():
    formulas = (("the area of a circle", "\u03c0r\u00b2"),("the circumference of a circle","2\u03c0r or \u03c0d"),("the area of a sector","(sector angle \u00f7 360) \u00d7 area of circle"),("the length of an arc","(arc angle \u00f7 360) \u00d7 circumference"),("area of a segment","area of sector - (\u00bdr\u00b2sin(angle of sector"))
    choice = randint(0, len(formulas)-1)
    if randint(0,1) == 0:
        questionBase = f"What is the formula for {formulas[choice][0]}?"
        answer = f"{formulas[choice][1]}"
    else:
        questionBase = [
            f"The following formula will find the area for what:",
            f"{formulas[choice][1]}"]
        answer = f"{formulas[choice][0]}"
    q = cf.Question(cf.currentFuncName())
    q.questionBase, q.answerBase, q.diagram, q.hint, q.website = questionBase, answer, None, None, None
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()
    

def ed_bc_area_of_a_circle_23():
    pi = 3.1415835898
    b = randint(2,10)
    c = b*2
    area = round(pi * b * b, 2)
    values = (("b", b, "cm"),("c",c,"cm"),("the area",area,"cm\u00b2"))
    order = list_mangle(values)
    questionBase = [
        f"On the diagram, {values[order[0]][0]} = {values[order[0]][1]}{values[order[0]][2]}.",
        f"Find {values[order[1]][0]}."]
    answer = f"{values[order[1]][0]} = {values[order[1]][1]}{values[order[1]][2]}"
    hint = "Area of a circle = \u03c0r\u00b2."
    video, website = None, "https://www.mathsisfun.com/geometry/circle-area.html"
    q = cf.Question(cf.currentFuncName())
    q.piclink = 'https://lh3.googleusercontent.com/jRlx8Ljgw0jx-Ie1XzuRYGSx5cBIntZNxEv_GINalEbfVG_dnQDo_tw3ul9WTnaJyCnSRCyggL12_ns36ZvOQ-tsubM2Lg5-3ndLe1svj88OA0xWPv53fs9xfBBN46ebtKq-6cgrIKfKy3uHnD9n4J86e4Xm5dFrrvRdHE4aWuC4A_28nKl0uxzIg9fn_AN1GOLKTvHJZUUF6riHAuqDLMazhNOAeUxshej9GdpbEuykbWwf2SYyNPJTp8kTG1triy_VYwHI5JJmWKOvMrfe2BXZ1XuAwkKWOClhZpTYNkDA8gwH6fBA4oQwT9Dfd5EkdvdxDc3iiGDHYA4zrqFWWXBJl8ieIkRaOEec6Zvh0LQdJDQUy9yvNTayBLaf6vzv4Xw8enzyQ-Ab5Kdo9dRTF6CVssZkECWqJxKFjlFL7CJMrPHOlGZgWVKtO49rQTRz2YTgvei6sGDOYNevzeFJcJzIHCjWT7Sgx6QIVN6C4R4DXAHvhELEekWluWbux7QfJGBzMDNXNcvNlwKXq8nX5AtClYg4UO8dh4V05Vhy1KMsMnVZlaAU_0Kbf_ne9FzwBRysgmYJJZghFz4dS8EvgDMVW-4vEqntmWlurwGQg4J5G4X_Xo5WXw5zaE9_XH5Ia0-BXDV81Lp98LqjmbKd_EDGG_KKQOUQBGkvoxvTzKN78K_GzyHlJeS0ueHxpdnk6vztvKSl8xpVaGkzcUFYU4YL=w1280-h720-no?authuser=0'
    q.questionBase, q.answerBase, q.constant, q.hint, q.website = questionBase, answer, "\u03c0 = 3.14159", hint, website
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()
    
def ed_bd_circumference_of_a_circle_23():
    pi = 3.1415835898
    b = randint(2,10)
    c = b*2
    circumference = round(pi * 2 * b, 2)
    values = (("b", b, "cm"),("c",c,"cm"),("the circumference",circumference,"cm"))
    order = list_mangle(values)
    questionBase = [
        f"On the diagram, {values[order[0]][0]} = {values[order[0]][1]}{values[order[0]][2]}.",
        f"Find {values[order[1]][0]}."]
    answer = f"{values[order[1]][0]} = {values[order[1]][1]}{values[order[1]][2]}"
    diagram, constant = f'/diagrams/gcsemaths/area_volume/ed20_circumference_radius_and_diameter_12.jpg', "\u03c0 = 3.14159"
    video, website = None, "https://www.wikihow.com/Calculate-the-Circumference-of-a-Circle"
    q = cf.Question(cf.currentFuncName())
    q.piclink = 'https://lh3.googleusercontent.com/jRlx8Ljgw0jx-Ie1XzuRYGSx5cBIntZNxEv_GINalEbfVG_dnQDo_tw3ul9WTnaJyCnSRCyggL12_ns36ZvOQ-tsubM2Lg5-3ndLe1svj88OA0xWPv53fs9xfBBN46ebtKq-6cgrIKfKy3uHnD9n4J86e4Xm5dFrrvRdHE4aWuC4A_28nKl0uxzIg9fn_AN1GOLKTvHJZUUF6riHAuqDLMazhNOAeUxshej9GdpbEuykbWwf2SYyNPJTp8kTG1triy_VYwHI5JJmWKOvMrfe2BXZ1XuAwkKWOClhZpTYNkDA8gwH6fBA4oQwT9Dfd5EkdvdxDc3iiGDHYA4zrqFWWXBJl8ieIkRaOEec6Zvh0LQdJDQUy9yvNTayBLaf6vzv4Xw8enzyQ-Ab5Kdo9dRTF6CVssZkECWqJxKFjlFL7CJMrPHOlGZgWVKtO49rQTRz2YTgvei6sGDOYNevzeFJcJzIHCjWT7Sgx6QIVN6C4R4DXAHvhELEekWluWbux7QfJGBzMDNXNcvNlwKXq8nX5AtClYg4UO8dh4V05Vhy1KMsMnVZlaAU_0Kbf_ne9FzwBRysgmYJJZghFz4dS8EvgDMVW-4vEqntmWlurwGQg4J5G4X_Xo5WXw5zaE9_XH5Ia0-BXDV81Lp98LqjmbKd_EDGG_KKQOUQBGkvoxvTzKN78K_GzyHlJeS0ueHxpdnk6vztvKSl8xpVaGkzcUFYU4YL=w1280-h720-no?authuser=0'
    q.questionBase, q.answerBase, q.constant, q.hint, q.website = questionBase, answer, constant, "Circumference of a circle = 2\u03c0r OR \u03c0d." , website
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()
    
def ed_be_area_and_circumference_23():
    pi = 3.1415835898
    b = randint(2,10)
    c = b*2
    area = round(pi * b * b, 2)
    circumference = round(pi * 2 * b, 2)
    if randint(0,1) == 0:
        values = (("b", b, "cm"),("c",c,"cm"),("the circumference",circumference,"cm"))
        order = list_mangle(values)
        questionBase = [
            f"On the diagram, {values[order[0]][0]} = {values[order[0]][1]}{values[order[0]][2]}.",
            f"Find {values[order[1]][0]}."]
        answer = f"{values[order[1]][0]} = {values[order[1]][1]}{values[order[1]][2]}"
    else:
        values = (("b", b, "cm"),("c",c,"cm"),("the area",area,"cm\u00b2"))
        order = list_mangle(values)
        questionBase = f"On the diagram, {values[order[0]][0]} = {values[order[0]][1]}{values[order[0]][2]}. Find {values[order[1]][0]}."
        answer = f"{values[order[1]][0]} = {values[order[1]][1]}{values[order[1]][2]}"
    hint = "Area of a circle = \u03c0r\u00b2. Circumference of a circle = 2\u03c0r OR \u03c0d."
    video, website = None, None
    q = cf.Question(cf.currentFuncName())
    q.piclink = 'https://lh3.googleusercontent.com/jRlx8Ljgw0jx-Ie1XzuRYGSx5cBIntZNxEv_GINalEbfVG_dnQDo_tw3ul9WTnaJyCnSRCyggL12_ns36ZvOQ-tsubM2Lg5-3ndLe1svj88OA0xWPv53fs9xfBBN46ebtKq-6cgrIKfKy3uHnD9n4J86e4Xm5dFrrvRdHE4aWuC4A_28nKl0uxzIg9fn_AN1GOLKTvHJZUUF6riHAuqDLMazhNOAeUxshej9GdpbEuykbWwf2SYyNPJTp8kTG1triy_VYwHI5JJmWKOvMrfe2BXZ1XuAwkKWOClhZpTYNkDA8gwH6fBA4oQwT9Dfd5EkdvdxDc3iiGDHYA4zrqFWWXBJl8ieIkRaOEec6Zvh0LQdJDQUy9yvNTayBLaf6vzv4Xw8enzyQ-Ab5Kdo9dRTF6CVssZkECWqJxKFjlFL7CJMrPHOlGZgWVKtO49rQTRz2YTgvei6sGDOYNevzeFJcJzIHCjWT7Sgx6QIVN6C4R4DXAHvhELEekWluWbux7QfJGBzMDNXNcvNlwKXq8nX5AtClYg4UO8dh4V05Vhy1KMsMnVZlaAU_0Kbf_ne9FzwBRysgmYJJZghFz4dS8EvgDMVW-4vEqntmWlurwGQg4J5G4X_Xo5WXw5zaE9_XH5Ia0-BXDV81Lp98LqjmbKd_EDGG_KKQOUQBGkvoxvTzKN78K_GzyHlJeS0ueHxpdnk6vztvKSl8xpVaGkzcUFYU4YL=w1280-h720-no?authuser=0'
    q.questionBase, q.answerBase, q.constant, q.hint, q.website = questionBase, answer, "\u03c0 = 3.14159", hint, website
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()
    
       

def ed_bf_arcs_and_sectors_12():
    values = (("a", "major arc"),("b","minor arc"),("c","minor sector"),("d","major sector"),("x","angle of minor sector"),("y","angle of major sector"))
    choice = randint(0,len(values)-1)
    if randint(0,1) == 0 :questionBase, answer = f"On the diagram above, what does {values[choice][0]} represent?", f"{values[choice][1]}"
    else: questionBase, answer = f"On the diagram above, which letter represents the {values[choice][1]}?", f"{values[choice][0]}"
    hint = "A major arc is a larger part of a circumference. A minor arc is the smaller part. A major sector is the larger area of a circle which is split by two radi. A minor sector is the smaller part."
    video, website = None, None
    q = cf.Question(cf.currentFuncName())
    q.piclink = 'https://lh3.googleusercontent.com/N060xDYk5F75mzW0bmk9dK-3iNFfb6Zq8T00qgH3cIFq8r5rF67Qm_cP9CkirSal70p11grMjwpc5XAgNX-fDZDlqbxds03rolTY2z6HgrGR_0DAtKlrzItwGakWYsOkPPxEsjwQxVufekCukTJjGxboQmKjJLFy8g4qN6seARWxKphRfeXvjHzI31PzO384MwRm0qtEgGtSoEOXJ9ZO24nAIeqptuqdvabLqTmea70GYUkdY5JQEv3QBDELxjL5XMB4GKTVM5b_0Ik1eX-w-vdgwxuK9ePLRC9rs7GV9jU9zv-eNDU2bp2ynrXP9sx2QY5HZEt8ltJQU8ICZCK9yHFBRM8WYCVNd-mUbJoGDRt5lBRpZJ4hZn2DHw1-_L4WmYq7c0SClcelzVC4scSyfOVSQ1lk6jZJYhAz1s5MTDK2c_1iCWtDLOhT7JYSp50y2e_bTJt5RYtz5sW2JFo7C1MRwYNNNeyeeI2tQwY7M3DZqw9_zeKTC-0R1BcV9rkNcDzYafTKT-jf5PP3eBcFf0bPZ3vgHY_0s51aB629QCY00rrTkl_MavZyM8yQ40mTmrXKS5KIBOTXhJWKC9cJ8bZKDIhVGsUrrboTnhjCUXqt3PHxYnhnKL5n_VFLmFjTQAx4F7mE-fTAuNf7S2FGokmYy5b3cs2zZiqYITrc8JkKCgZzdVO3DOHioiASu-io0wqCKHe9rw7wlxwNIHfiOAq4=w1280-h720-no?authuser=0'
    q.questionBase, q.answerBase, q.constant, q.hint, q.website = questionBase, answer, "\u03c0 = 3.14159", hint , website
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()
    

def ed_bg_segments_12():              
    values = (("r", "radius"),("e","chord"),("f","segment"),("h","distance from centre to chord"))
    choice = randint(0,len(values)-1)
    if randint(0,1) == 0 :questionBase, answer = f"On the diagram above, what does {values[choice][0]} represent?", f"{values[choice][1]}"
    else: questionBase, answer = f"On the diagram above, which letter represents the {values[choice][1]}?", f"{values[choice][0]}"
    hint = "A chord is a line which contacts both parts of the circumference but does not pass through the centre. A segment is a part of a cirle divided by a chord."
    q = cf.Question(cf.currentFuncName())
    q.piclink = 'https://lh3.googleusercontent.com/dchkNeGirzYclAR3zliZEexF7INCAzRYxzH0oYPbke0YWqHz33AB0T6N-yYL6uMdYtTvqqBBkDI6JTMYVpSHvhe4gKb3AMN6nytqp8J4AyTRhIrkQVmvvSaygU_qNxHl-O1wI6PjOwY_5R9S3ujIzW7MAk5GNVsUlnBKsD34erIlEHzHF3YYMrL5-xWpn2-b3a4Zt6px0m4Yz8Sa963HbDh3FN_3J3zAzTUF3wWXD72ucg_812UcKehE1DeEEXeJleXMgl4HPKfvVORolSoqVCqYXn9S0GKM4PAJp5o6MtAFuID5gU0v1nV7oQRum9oTMSOYNmjX7ZJC9-9ZzTV3nFERJc8t1m8hBjyRgrYz_uWDKROagpqXGAYIKeOi0zUgWk5sr6idXcRA6dYWgV_Hjv2uKXMbfWF-XXtMG21snGqf4TmPf6K3DLqna60-ZvCO90nf7jfx0OQcVq1vQVk3PtO-TFaJ_C3hQnybqryjSrUvQBmnjLvflLPpLYeKnoWCzXccaulCQCIwES1_Hve9-zk9WOUyDQ1gDB3lVQsIgQe4utRmXsQXDkVGcPMBPcjMwJXgkTjefpxv3wMtG6Yu8GjGw2L9io2dqvFu6abNR_FkJfujCft9DQgL9IRxtJtIYCrT33l4V7elSNv5uEDh2NA3XGEaj1G7v8eJagh0ulQ198DA_JBG2-4k2kxWF8YihY6YQxWAOVsYnFbgPF5EaQYB=w1280-h720-no?authuser=0'
    q.questionBase, q.answerBase, q.constant, q.hint = questionBase, answer, "\u03c0 = 3.14159", hint 
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()
    
   
def ed_bh_segments_arcs_and_sectors13():
    values = (("a", "major arc"),("b","minor arc"),("c","minor sector"),("d","major sector"),("e","chord"),("f","segment"))
    choice = randint(0,len(values)-1)
    if randint(0,1) == 0 :questionBase, answer = f"On the diagram above, what does {values[choice][0]} represent?", f"{values[choice][1]}"
    else: questionBase, answer = f"On the diagram above, which letter represents the {values[choice][1]}?", f"{values[choice][0]}"
    hint = "A chord is a line which contacts both parts of the circumference but does not pass through the centre. A segment is a part of a cirle divided by a chord."
    q = cf.Question(cf.currentFuncName())
    q.piclink = 'https://lh3.googleusercontent.com/-UJhKV7050N3hQs4AkZargVUa8HL6ZGpfR5Ugp8UU_1HJ3nGV_XKCUmT5PztRqPF4XXUFIKP5K2-TPytF-zU_hshT1fVQu66J1EVF8xAnEBB1cNlj01pfNj_yXeyAHM_L_ByD9Og54pevk0M9zmumStwIvO5tUVoBjapTOViGF9R54B7DtOl2jMnCcfzKK0B1N7p8OvuwHsNc5pmCID2fKKikoDAnukgTRsoTpcIXuQGKO2o-9GwrDLEk96jjbLT4eYKIyO4CKcSTS3RTNE8s1s6qsP6xxzmSL28GV1LVCcSkMDhLSGS8pYK30O-cqR8WNq3xEhmwB3eNPwXMC0ffz52Es0_3pDis7KukFGvaCu7UHH3wpn6awzJgvBjvTJh0T7LB0wMHsxvJuPvwe0eWXRJBaiYXtCxlk8f682TSBKABx0jqcsVQaSEumFTiI2j3M05wnYR_Rwzw0RDoPPOq_K5YmZQadYPyUItXCEh92kGkEdfdfO1DMDpaDnarR1oi9j04GtxLLqD2BVKWcAN_Gz9T-cwD76UcsbalUFk-5XDM7PionkGOI0rwHG3pdY7YDa0cYWMQEyHQUnwtQQerWCvquyoT9g9NOl9vnuZr3iTPB4-govkDM5v4pnuEv7T6YWLOinXVbKsRw_LPDCXik1wO68wtq0P-0wUK4AvSFgoUMTeQ4DNtQ4iTnFt_-UhZTp-o6SzXbudvlshE_oV66-K=w1280-h720-no?authuser=0'
    q.questionBase, q.answerBase, q.constant, q.hint, q.website = questionBase, answer,   "\u03c0 = 3.14159", hint , None
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()
    
def ed_bi_area_of_a_sector26():
    x = randint(1,179)
    y = 360 - x
    area = randint(5,50)
    minor_sector = round(x/360*area, 2)
    major_sector = round(y/360*area, 2)
    values = (("the minor sector's area",minor_sector,"cm\u00b2"),("the major sector's area", major_sector,"cm\u00b2" ))
    order = list_mangle(values)
    questionBase = [
        f"On the diagram (not to scale),",
        f"x = {x}\u00b0,",
        f"area = {area}cm\u00b2.",
        f"Find {values[order[0]][0]}."]
    answer = f"{values[order[0]][0]} = {values[order[0]][1]}{values[order[0]][2]}"
    hint = "The area of a sector = (angle of sector/360) x area of the circle."
    video, website = None, "https://www.bbc.co.uk/bitesize/guides/z9hsrdm/revision/1"
    q = cf.Question(cf.currentFuncName())
    q.piclink = 'https://lh3.googleusercontent.com/N060xDYk5F75mzW0bmk9dK-3iNFfb6Zq8T00qgH3cIFq8r5rF67Qm_cP9CkirSal70p11grMjwpc5XAgNX-fDZDlqbxds03rolTY2z6HgrGR_0DAtKlrzItwGakWYsOkPPxEsjwQxVufekCukTJjGxboQmKjJLFy8g4qN6seARWxKphRfeXvjHzI31PzO384MwRm0qtEgGtSoEOXJ9ZO24nAIeqptuqdvabLqTmea70GYUkdY5JQEv3QBDELxjL5XMB4GKTVM5b_0Ik1eX-w-vdgwxuK9ePLRC9rs7GV9jU9zv-eNDU2bp2ynrXP9sx2QY5HZEt8ltJQU8ICZCK9yHFBRM8WYCVNd-mUbJoGDRt5lBRpZJ4hZn2DHw1-_L4WmYq7c0SClcelzVC4scSyfOVSQ1lk6jZJYhAz1s5MTDK2c_1iCWtDLOhT7JYSp50y2e_bTJt5RYtz5sW2JFo7C1MRwYNNNeyeeI2tQwY7M3DZqw9_zeKTC-0R1BcV9rkNcDzYafTKT-jf5PP3eBcFf0bPZ3vgHY_0s51aB629QCY00rrTkl_MavZyM8yQ40mTmrXKS5KIBOTXhJWKC9cJ8bZKDIhVGsUrrboTnhjCUXqt3PHxYnhnKL5n_VFLmFjTQAx4F7mE-fTAuNf7S2FGokmYy5b3cs2zZiqYITrc8JkKCgZzdVO3DOHioiASu-io0wqCKHe9rw7wlxwNIHfiOAq4=w1280-h720-no?authuser=0'
    q.questionBase, q.answerBase, q.constant, q.hint, q.website= questionBase, answer, "\u03c0 = 3.14159", hint, website
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()
    
def ed_bj_length_of_arc26():
    x = randint(1,179)
    y = 360 - x
    circumference = randint(5,50)
    minor_arc = round(x/360*circumference, 2)
    major_arc = round(y/360*circumference, 2)
    values = (("the minor arc's length",minor_arc,"cm"),("the major arc's length", major_arc,"cm" ))
    order = list_mangle(values)
    questionBase = [
        f"On the diagram (not to scale),",
        f"x = {x}\u00b0,",
        f"circumference = {circumference} cm.",
        f"Find {values[order[0]][0]}."]
    answer = f"{values[order[0]][0]} = {values[order[0]][1]}{values[order[0]][2]}"
    hint = "The length of an arc = (angle of sector/360) x circumference."
    video, website = None, "https://www.bbc.co.uk/bitesize/guides/z9hsrdm/revision/2"
    q = cf.Question(cf.currentFuncName())
    q.piclink = 'https://lh3.googleusercontent.com/FDK9xHAeATxNXeZqqRIgA9Sd02ooJ7XwquHNYzBREBMKAP1FBJDMPgGzY0ZtqpQIkQNNS-IOVOb6XPD_pK9lkSXD9f_v2uyfPIcGKeuUStKmZ7chfsQ876o1k5ePYVHGW2hzRGi7BE1Qt93TRfk7AtQwPtTsHJl-3S8ekfWLb9MbuaY-E16gr4wkY01ikpSXGOQy-B2GI9gtJxQA9-ZAqk_0K3v4ZsPEsuYVEFrBHZjIlId5TC1rKqP23dr_ihfKy9ltj5wlsDJ5lnbM7D481j9fJVSXjUoVIup_WbKjYA1VASC9b9hwRC5541Ej6QBjUwWgUWfT4zdfwI8fbD1tsP0oCxU6Xibjk5HBPPHLkrUFiG5lMfZbZ57P611zQrmwL56r-nyny9pk7Zvm9c1e-XH-DkuOhpBWvkj8YKEA2WJBkAHYUd73Uiv-iLAnRmxhnMs1wlNItQJbH8-26u0aurJTqXXgJFijQQcFSkLPZelfUz8sRilkt49MfPX9MXhW4e8u4vDaof3pQ4-vBhEbRqerWAvfxph2lAIidTQvd0uOr2J8Jt3Hskf1-F67Hpj2MPCW13JEymB0l_5jPddm74D6GpXWbxJaWPAf-gEhQKVlFL5qh7EDc-KUWcETnJqLtJAow_e7IQelgg9z1OJz44JTEsDFc4hhCD9vH05uxyXaYl3BvxXFIBtQbdWkHpKfQ6njcXn_kcb7Wr5Eq4OGuWNz=w1280-h720-no?authuser=0'
    q.questionBase, q.answerBase, q.constant, q.hint, q.website = questionBase, answer,"\u03c0 = 3.14159", hint, website
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()
    

def ed_bk_area_of_segments37():
    r = randint(2,12)
    x = randint(1,110)
    e = randint(2,12)
    segment_area = round((x/360 * 3.14159 * r * r) - 0.5 * r * r * math.sin(math.radians(x)),2)
    values = (("x", x, "\u00b0"),("r",r,"cm"),("e",e,"cm"),("the area of the segment", segment_area,"cm\u00b2" ))
    order = list_mangle(values)
    questionBase = [
        f"On the diagram (not to scale),",
        f"{values[order[0]][0]} = {values[order[0]][1]} {values[order[0]][2]},",
        f"{values[order[1]][0]} = {values[order[1]][1]} {values[order[1]][2]} and",
        f"{values[order[2]][0]} = {values[order[2]][1]} {values[order[2]][2]}.",
        f"Find {values[order[3]][0]}."]
    answer = f"{values[order[3]][0]} = {values[order[3]][1]} {values[order[3]][2]}"
    hint = "The area of a segment = the area of a sector - the area of the triangle made by the two radi and the chord. This triangle = \u00bdr\u00b2sin x."
    video, website = None, "https://www.bbc.co.uk/bitesize/guides/z9hsrdm/revision/5"
    q = cf.Question(cf.currentFuncName())
    q.piclink = 'https://lh3.googleusercontent.com/uss2WfZrymSnkeeRT3REMrHmjYM-yVhYGY2ed9mNwKt9GqyBKWPux7m0G1bn3Od3tBZzVbQKAMWkQB4ebMa6dzjFyqFSUxOIPTiYm_w9B8Z3i6wvdSBXaBAeJ3UwdF1gi7RDf-vSdNEruRomSvp6PwAORh1KclvJpbkJLRkPzhT5Eqa9mvZekg_SuoQapfs2V3zHbW8H5ruV3Crghs_TiyYe13qMIQ41eAjYsXsac21sa9vRwBvbZPfkwplp7-8k5tD1MKMakkBU6RY9Mu9XFTQWrYYbggsJo2ZhiPgJCZktKOj16J8bsPVeG_ahgGk-gtWkZF8L6CUhR4neMpizRgcII22l2LoO0gCIuXzOpPnCP6VKSIEf9CPlQLszy6OP_lvj4dUd8UOcdax6823GVyIE-hnEUdEQ3N4U57wmqpXIyA17WoKCuOgKWvyFvPSbB4e4TVGS6WqlqlfWOOdgmo3l05osFUx7yx-MoQT_2EodDsWoaFMm8j8HMZrrHTDiYLPbPDp8qP0L37FGh2DgUtkvSFUM8Rxn6tm9mDrTBA5b2xrSAIaeQxXsCLyHiekGgMtLVE1fc_fSyd3NGKeTpBHjgt568Pl8Nr4u-TCJAr3zBemULbVsdIbJaYCXKqITfMzXNHwl50T-cKlma-ABwaE07I9geodWtudKNvOuNHalz3cfsabEZvCI_ryY8xv8PCwlHqaNQmdXzYNeZrcY0q-Q=w1280-h720-no?authuser=0'
    q.questionBase, q.answerBase, q.constant, q.hint, q.website = questionBase, answer, "\u03c0 = 3.14159", hint , website
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()
    

def ed_bl_area_of_pacman26():
    a = randint(2,15)
    x = randint(1,110)
    shaded_area = round((3.14159 * a * a) - (x/360*(3.14159 * a * a)), 2)
    values = (("x", x, "\u00b0"),("a",a,"cm"),("the area of pacman", shaded_area,"cm\u00b2" ))
    order = list_mangle(values)
    questionBase = [
        f"On the diagram,",
        f"{values[order[0]][0]} = {values[order[0]][1]} {values[order[0]][2]} and",
        f"{values[order[1]][0]} = {values[order[1]][1]}{values[order[1]][2]}.",
        f"Find {values[order[2]][0]}."]
    answer = f"{values[order[2]][0]} = {values[order[2]][1]} {values[order[2]][2]}"
    hint = "The area of a sector = (angle of sector/360) x area of the circle. The pacman in the diagram is a major sector."
    video, website = None, "https://www.bbc.co.uk/bitesize/guides/z9hsrdm/revision/1"
    q = cf.Question(cf.currentFuncName())
    q.piclink = 'https://lh3.googleusercontent.com/1OgWKFiSRGInmRHcM2Twv_nOhQI5G46l6oRsrJAYd7UzMcTJSNtMC4-QbOtiyRZZfMLpU50U1lM59YdJRugNlLXy_lpeZbmGkLjwnxGbpGP0dcWpbFJAbrkUS6WJcPe3WWm8nindl8ronLCKpLLQuEe1byBT4Vn65y7Zqbhd4HXDQhHdjszDEzKZ0CQBBKaF5tafakDvQeqDHzMMb19xYINe-xrVNcla6S8RFIYkYFjd7UvPeAW18Uf5vSUFLF4J4t5HCxM1osyFdYWf6vDTjnXrJt8t-K4IZ0o7PvzJKy_RAO2tzi1-Tj2crB7uAlQf5GwTt11-OkGr7aFCfBIuYtw9yO5-b_S-AYbzD3XOtKDrr0dhnJcAxbFydUNVJJVoPK998KoUhwD81SPWNT9XtMhycxo6c0IDPaBuP6ll4gqapHl62KJg3pB5IydEWmyeHDSAD2A_Q97y4X-vwSHfCbmD-1eHkA-p7rLJ0PCNpJ4HeGmga1_LdccBJWNeFTzVpaY9MvMblDI1s8FR0xsguF_R8mtzIPi2KuM4MbPKZYhjqyA2AVDUiaSN2PbpEdiWq9rrj0fEhIJaD8XzxgGyJEw6dEq2RH7ju0Bekzokj4RmgQFJ_51ug5tg5GEh9g1-SMr4iLmWryOhZo337abO-N9wWpXfFHBV7mxJ1lNbkJcqMSVsk_cOpU491i_Q-sw2UadJ012lXHmHYx9Rs8sRKUtA=w1280-h720-no?authuser=0'
    q.questionBase, q.answerBase, q.constant, q.hint, q.website = questionBase, answer, "\u03c0 = 3.14159", hint , website
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()
    

def ed_bm_shape_problem26():
    x = randint(100,160)
    a = randint(3,15)
    area_sector = round((x/360 * 3.14159 * a * a),2)
    length_arc = round((x/360 * 2 * 3.14159 * a), 2)
    area_segment = round((x/360 * 3.14159 * a * a) - 0.5 * a * a * math.sin(math.radians(x)),2)
    perimeter_shape = round((x/360 * 2 * 3.14159 * a) + a + a, 2)
    values = (("area of the sector", area_sector, "cm\u00b2"),("length of the arc",length_arc,"cm"),("area of the segment",area_segment,"cm\u00b2" ),("perimeter of the shape",perimeter_shape,"cm"))
    order = randint(0, len(values)-1)
    questionBase = [f"On the diagram,",f"x = {x}\u00b0 and",f"a = {a}cm.",f"Find {values[order][0]}."]
    answer = f"{values[order][0]} = {values[order][1]}{values[order][2]}"    
    hint = "The perimeter of this shape includes the arc AND the two radii, which are also on the outside of the shape. Feel free to go back a few questions if you need help with the others!"
    video, website = None, "https://www.bbc.co.uk/bitesize/guides/z9hsrdm/revision/1"
    q = cf.Question(cf.currentFuncName())
    q.piclink = 'https://lh3.googleusercontent.com/1OgWKFiSRGInmRHcM2Twv_nOhQI5G46l6oRsrJAYd7UzMcTJSNtMC4-QbOtiyRZZfMLpU50U1lM59YdJRugNlLXy_lpeZbmGkLjwnxGbpGP0dcWpbFJAbrkUS6WJcPe3WWm8nindl8ronLCKpLLQuEe1byBT4Vn65y7Zqbhd4HXDQhHdjszDEzKZ0CQBBKaF5tafakDvQeqDHzMMb19xYINe-xrVNcla6S8RFIYkYFjd7UvPeAW18Uf5vSUFLF4J4t5HCxM1osyFdYWf6vDTjnXrJt8t-K4IZ0o7PvzJKy_RAO2tzi1-Tj2crB7uAlQf5GwTt11-OkGr7aFCfBIuYtw9yO5-b_S-AYbzD3XOtKDrr0dhnJcAxbFydUNVJJVoPK998KoUhwD81SPWNT9XtMhycxo6c0IDPaBuP6ll4gqapHl62KJg3pB5IydEWmyeHDSAD2A_Q97y4X-vwSHfCbmD-1eHkA-p7rLJ0PCNpJ4HeGmga1_LdccBJWNeFTzVpaY9MvMblDI1s8FR0xsguF_R8mtzIPi2KuM4MbPKZYhjqyA2AVDUiaSN2PbpEdiWq9rrj0fEhIJaD8XzxgGyJEw6dEq2RH7ju0Bekzokj4RmgQFJ_51ug5tg5GEh9g1-SMr4iLmWryOhZo337abO-N9wWpXfFHBV7mxJ1lNbkJcqMSVsk_cOpU491i_Q-sw2UadJ012lXHmHYx9Rs8sRKUtA=w1280-h720-no?authuser=0'
    q.questionBase, q.answerBase, q.constant, q.hint, q.website = questionBase, answer,"\u03c0 = 3.14159", hint , website
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()
    

def prism():
    shape_list = ["http://www.k6-geometric-shapes.com/image-files/prism-rectangle-1.jpg",
                  "http://www.clipartkid.com/images/78/3d-rectangular-prism-in-real-life-image-galleries-imagekb-com-kGqhFW-clipart.png",
                  "https://netninja.com/wp-content/uploads/2014/05/toblerone.jpg",
                  "https://ae01.alicdn.com/kf/HTB151mQXODxK1RjSsphq6zHrpXaY/Triangular-color-prism-K9-Optical-Glass-Right-Angle-Reflecting-Triangular-Prism-For-Teaching-Light-Spectrum-Total.jpg",
                  "https://www.software3d.com/JPeg/Prism5.jpg",
                  "https://alchetron.com/cdn/pentagonal-prism-39739ed7-2b34-4eb4-9cab-29561face1d-resize-750.png"
                  "https://i.imgflip.com/2b5qcq.jpg",
                  ]
    return shape_list[randint(0,len(shape_list)-1)]

def cylinder():
    shape_list = ["https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fpics.me.me%2Fthe-orange-cylinder-is-here-it-is-orange-and-pillar-19722697.png&f=1&nofb=1",
                  "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fpics.onsizzle.com%2FFacebook-71403c.png&f=1&nofb=1",
                  "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fpics.me.me%2FFacebook-We-hate-when-cylinder-5-says-0861e6.png&f=1&nofb=1",
                  "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.pinimg.com%2Foriginals%2F1d%2F48%2F5f%2F1d485fd3db4a92dbe8bd0b5398110fe2.jpg&f=1&nofb=1",
                  "https://i.pinimg.com/564x/d0/05/69/d0056904186322fc43f289160fa30bd1.jpg",
                  "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fpics.conservativememes.com%2Fine-joseph-enouys-8-cylinder-48-shot-percussion-revolver-dated-1855-13726561.png&f=1&nofb=1"]
    return shape_list[randint(0,len(shape_list)-1)]

def sphere():
    shape_list = ["https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fpics.onsizzle.com%2Fgame-sphere-tsspherical-https-t-co-jnyuys9da1-11045947.png&f=1&nofb=1",
                  "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fpics.me.me%2Fflat-earther-or-sphere-earther-am-netker-for-i-am-33030488.png&f=1&nofb=1",
                  "https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fimageproxy.ifcdn.com%2Fcrop%3Ax-20%2Cresize%3A320x%2Ccrop%3Ax800%2Cquality%3A90x75%2Fimages%2F1c6828a88032dee5543cd9ee8d32db05607596b3c99efd04eaa70a64460fe712_1.jpg&f=1&nofb=1",
                  "https://pics.me.me/self-contained-self-supporting-ecological-system-permanently-sealed-within-a-hand-blown-borsilica-11473078.png",
                  "https://pics.me.me/sometimes-its-hard-being-a-sphere-%3Cp%3E-%3Ca-href-https-www-reddit-com-r-surrealmemes-comments-80kxjh-%3Esrc%3C-a%3E-%3C-p%3E-33131160.png",
                  "https://i0.wp.com/142.93.220.71/wp-content/uploads/2019/03/Microwave-Tinfoil-Into-Sphere-Smooth-Ball-Within-Minutes2.jpg",
                  "https://i.pinimg.com/originals/2c/79/b9/2c79b90aafccd9c6ec814dfdcdbe0d34.jpg",
                  "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fstatic.boredpanda.com%2Fblog%2Fwp-content%2Fuploads%2F2018%2F02%2Fsphere-of-42000-matches-wallacemk-fb18.png&f=1&nofb=1"]
    return shape_list[randint(0,len(shape_list)-1)]

def hemisphere():
    shape_list = ["https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.bo7qvXsehd77DPbUbb7GwAAAAA%26pid%3DApi&f=1",
                  "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse4.mm.bing.net%2Fth%3Fid%3DOIP.3gqUMVoQ9quaXQWZPWRdYwHaEo%26pid%3DApi&f=1",
                  "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse2.mm.bing.net%2Fth%3Fid%3DOIP.SjdteI3c4F_xKp6m0B1MNQHaHa%26pid%3DApi&f=1",
                  "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.NXmgxl0CctoJK-98Q51nZAHaFT%26pid%3DApi&f=1",
                  "http://www.cs.columbia.edu/CAVE/projects/DiffuseSL/images/hemisphere/Hemisphere.JPG",
                  "http://www.cmspinning.com/images/hemisphere_6_large.jpg"]
    return shape_list[randint(0,len(shape_list)-1)]

def pyramid():
    shape_list = ["https://s.newsweek.com/sites/www.newsweek.com/files/styles/full/public/2018/02/20/gettyimages-918637914.jpg",
                  "https://i2.wp.com/www.trinfinity8.com/wp-content/uploads/2015/12/Pyramid.jpg",                  "https://i.stack.imgur.com/ARVST.jpg",
                  "http://2.bp.blogspot.com/-DSqvsmnwWfA/U_o-VpTTH7I/AAAAAAAABKU/KA-uD-nC6eU/s1600/Tetrahedron%2BAlpha.jpg,"
                  "http://etc.usf.edu/clipart/43100/43188/pent1_43188_lg.gif",
                  "https://upload.wikimedia.org/wikipedia/commons/0/02/Pentagonal_pyramid.png",
                  "https://upload.wikimedia.org/wikipedia/commons/2/2a/Hexagonal_pyramid.png",
                  "https://www.det.nsw.edu.au/eppcontent/glossary/app/resource/image/111.png",]
    return shape_list[randint(0,len(shape_list)-1)]


def cone():
    shape_list = ["https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fimg.memecdn.com%2Fconezilla_c_3193391.jpg&f=1&nofb=1",
                  "https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fimages5.memedroid.com%2Fimages%2FUPLOADED14%2F510ee3b0d7741.jpeg&f=1&nofb=1",
                  "https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fmemecrunch.com%2Fmeme%2F1FXFO%2Fcone-head%2Fimage.png%3Fw%3D400%26c%3D1&f=1&nofb=1",
                  "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.tTNIoL5vfl9uH36bbsch2wHaKO%26pid%3DApi%26h%3D160&f=1",
                  "https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fc0263062.cdn.cloudfiles.rackspacecloud.com%2Fcontent%2Fimages%2Fsized%2Ffunny-fail-meme-traffic-cone_b4e32e0661ac7b6aa236927c8c448bd5_3x2_jpg_600x400_q85.jpg&f=1&nofb=1",
                  "https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fwww.teamjimmyjoe.com%2Fwp-content%2Fuploads%2F2015%2F02%2Fice-cream-missing-cone-you-had-one-job.jpg&f=1&nofb=1",
                  "https://cleanmemes.files.wordpress.com/2014/09/coneofhappiness1.jpg",
                  "https://s-media-cache-ak0.pinimg.com/736x/8d/46/b1/8d46b1f0516922ba248b6650f6152c1f.jpg",
                  "https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fwww.freakingnews.com%2Fpictures%2F58500%2FTraffic-Cone-Space-Shuttle--58732.jpg&f=1&nofb=1",
                  "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fpics.onsizzle.com%2Fthe-sorting-cone-youre-a-hazard-harry-memes-com-youre-3008662.png&f=1&nofb=1"]
                
    return shape_list[randint(0,len(shape_list)-1)]



def frustum():
    shape_list = ["http://etc.usf.edu/clipart/42700/42799/frust-cone5_42799_lg.gif",
                  "http://www.matematicasvisuales.com/images/geometry/desarrollosplanos/cones/frustum5.jpg",
                  "http://etc.usf.edu/clipart/42200/42230/conefrust_42230_lg.gif",
                  "https://qph.fs.quoracdn.net/main-qimg-21afb1a5be952d5c11fc4cf44c1f8ab6-c",
                  "https://qph.fs.quoracdn.net/main-qimg-fc4d439cc7ea5a00d0c11b0a71ed4c11-c",
                  "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse3.mm.bing.net%2Fth%3Fid%3DOIP.AVZoEcJfN9hjfjp5kbCZygHaGR%26pid%3DApi&f=1"]
    return shape_list[randint(0,len(shape_list)-1)]




def ed_ca_terminology13():
    #vertices, edge, face
    values = (("vertex", "a"),("edge", "b"),("face","c"))
    choice = randint(0,len(values)-1)
    if randint(0,1) == 0 :questionBase, answer = f"On the diagram above, what does {values[choice][1]} represent?", f"{values[choice][0]}"
    else: questionBase, answer = f"On the diagram above, which letter represents the {values[choice][0]}?", f"{values[choice][1]}"
    diagram, constant = f"/diagrams/gcsemaths/area_volume/ee10_terminology13/{randint(0,3)}.jpg", "\u03c0 = 3.1415835898"
    hint = "Vertices are corners, where two or more edges meet. Edges are the lines in between vertices. Faces are the spaces in between edges. Curved faces are sometimes called surfaces."
    video, website = None, "https://www.mathsisfun.com/geometry/vertices-faces-edges.html"
    piclink = None
    q = cf.Question(cf.currentFuncName())
    q.questionBase, q.answerBase, q.diagram, q.constant, q.hint, q.website = questionBase, answer, diagram, constant, hint, website
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()
    

def ed_cb_count_vertices_edges_faces13():
    values = (("cube",8,12,6,("http://memecrunch.com/meme/7WLH/ice-cube/image.png?w=400&c=1","https://ruwix.com/pics/memes/9-rubix-cube-neversolved.jpg","http://img.memecdn.com/don-t-know-if-ice-cube-has-balls-or-ice-cube-and-if-you-kick-him-does-ice-cube-have-crashed-ice_o_842184.jpg","https://pics.onsizzle.com/how-to-solve-a-1x1-rubiks-cube-tag-friends-to-10222173.png")),
               ("cuboid",8,12,6,(",https://i.imgflip.com/3rxwix.jpg","https://www.polyhedra.net/photo/rectangular-prism-01.jpg","https://ecdn.teacherspayteachers.com/thumbitem/3D-Shapes-Real-Life-Objects-Clip-Art-Rectangular-Prisms-4899203-1569632365/original-4899203-1.jpg")),
               ("square based pyramid",5,8,5,("https://i.pinimg.com/originals/a0/4f/26/a04f266a5d216d1ba4d74de0839a3618.jpg", "http://diggingforbones.files.wordpress.com/2012/08/how-the-pyramids.jpg","https://pics.onsizzle.com/my-food-pyramid-kind-of-looks-like-this-8948197.png","https://pics.onsizzle.com/the-great-pyramid-of-giza-contains-enough-stone-to-make-2908513.png", "https://kuulpeeps.com/wp-content/uploads/2018/06/Why-Bloggers-Should-Avoid-MLM-Like-the-Plague.jpg")),
               ("triangular prism",6,9,5,("https://www.procarton.com/wp-content/uploads/2015/02/toblerone_kopf2.jpg", "http://i1.kym-cdn.com/photos/images/facebook/001/191/306/5e8.jpg", "https://images7.memedroid.com/images/UPLOADED845/5aa68390474d5.jpeg", "https://breakbrunch.com/wp-content/uploads/2019/01/funny-meme-picture-1001180142-7.png")),
               ("tetrahedron", 4,6,4,("https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fthreesixty360.files.wordpress.com%2F2008%2F04%2Fsierpinski_tetrahedron.jpg%3Fw%3D450&f=1&nofb=1", "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.stack.imgur.com%2FKWAvA.jpg&f=1&nofb=1")))
    choice = randint(0,len(values)-1)
    thing = ("vertices", "edges","faces")
    thingChoice = randint(0,len(thing)-1)
    questionBase = f"How many {thing[thingChoice]} in a {values[choice][0]}?"
    answer = f"{values[choice][thingChoice+1]} {thing[thingChoice]}"
    diagram, constant = None, "\u03c0 = 3.14159"
    hint = "Vertices are corners, where two or more edges meet. Edges are the lines in between vertices. Faces are the spaces in between edges. Curved faces are sometimes called surfaces."
    video, website = None, "https://www.mathsisfun.com/geometry/vertices-faces-edges.html"
    q = cf.Question(cf.currentFuncName())
    q.piclink = f"{values[choice][4][randint(0,len(values[choice][4])-1)]}"
    q.questionBase, q.answerBase, q.diagram, q.constant, q.hint, q.website = questionBase, answer, diagram, constant, hint, website
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()
    

def ed_cc_surface_area14():
    people = peopleGen()
    true_tuple = ("the surface area is the total area of all faces", "the surface area is the total area of the shape's net", "a net is a 3D shape with each face folded out flat", "if you know area of one of the faces in a cube, you can calculate the whole surface area")
    false_tuple = ("the surface area is the total area of all the faces but, only ones you can directly see", "the surface area is half the total area of the shape's net, because you only see one side", "the surface area of a 3d shape includes the surface area on the inside", "if you know area of one of the faces in any 3d shape, you can calculate the whole surface area")
    choice = randint(0,1)
    answer = "Correct" if choice == 1 else "Incorrect"
    statement = true_tuple[randint(0,len(true_tuple)-1)] if answer == "Correct" else false_tuple[randint(0,len(false_tuple)-1)]
    questionBase = [
        f"{people[randint(0,len(people)-1)]} says that {statement}.",
        f"Is this statement correct or incorrect?"]
    diagram, constant = None, "\u03c0 = 3.14159"
    hint = "Surface area only applies to 3D objects and it's the total area of all the faces when added together."
    video, website, piclink = None, None, None
    q = cf.Question(cf.currentFuncName())
    q.questionBase, q.answerBase, q.diagram, q.constant, q.hint, q.website = questionBase, answer, diagram, constant, hint , website
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()
    
  
def ed_cd_surface_area_formulas14():
    values = (("sphere", "4\u03c0r\u00b2"),("cone","\u03c0rl + \u03c0r\u00b2"),("cylinder","2\u03c0rh + 2\u03c0r\u00b2"))
    choice = randint(0,len(values)-1)
    if randint(0,1) == 0 :questionBase, answer = f"What is the formula for the surface area of a {values[choice][0]}?", f"{values[choice][1]}"
    else: 
        answer  = f"{values[choice][0]}"
        questionBase = [
            f"The following formula can be used to calculate the surface area of what:",
            f"{values[choice][1]}?"]
    diagram, constant = None, "\u03c0 = 3.14159"
    hint = "All formulas in the link below!"
    video, website = None, "https://www.thoughtco.com/surface-area-and-volume-2312247"
    piclink = None
    q = cf.Question(cf.currentFuncName())
    q.questionBase, q.answerBase, q.diagram, q.constant, q.hint, q.website = questionBase, answer, diagram, constant, hint, website
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()
    
def ed_ce_surface_area_of_a_sphere25():
    r = randint(1,10)
    area = round(4*3.1415926*r*r, 2)
    questionBase = [
        f"In the sphere above, the radius = {r} cm.",
        f"Find the surface area."]
    answer = f"{area}cm\u00b2"
    diagram, constant = None, "\u03c0 = 3.14159"
    hint = "Surface area of a sphere = 4\u03c0r\u00B2"
    video, website = None, "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fimages-na.ssl-images-amazon.com%2Fimages%2FI%2F61WN2k1l5wL._SL1461_.jpg&f=1&nofb=1"
    q = cf.Question(cf.currentFuncName())
    q.questionBase, q.answerBase, q.diagram, q.constant, q.hint, q.website = questionBase, answer, diagram, constant, hint, website
    q.piclink = sphere()
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()
    
def ed_cf_surface_area_of_a_cylinder25():
    r = randint(1,10)
    h = randint(1,10)
    area = round(2*3.1415926*r*h + 2*3.1415926*r*r, 2)
    questionBase = [
        f"In the cylinder above,",
        f"the radius of the cross section = {r} cm and",
        f"the height is {h} cm.",
        f"Find the surface area."]
    answer = f"{area}cm\u00b2"
    diagram, constant = None, "\u03c0 = 3.14159"
    hint = "Surface area of a cylinder = 2\u03c0rh + 2\u03c0r\u00B2"
    video, website = None, "https://mathopenref.com/cylinderareamain.html"
    q = cf.Question(cf.currentFuncName())
    q.questionBase, q.answerBase, q.diagram, q.constant, q.hint, q.website = questionBase, answer, diagram, constant, hint, website
    q.piclink = cylinder()
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()
    
def ed_cg_surface_area_of_a_cone25():
    r = randint(1,10)
    l = randint(1,10)
    area = round(3.1415926*r*l + 3.1415926*r*r, 2)
    questionBase = [
        f"In the cone above,",
        f"radius of the base = {r} cm and",
        f"height of the cone = {l} cm.",
        f"Find the surface area."]
    answer = f"{area}cm\u00b2"
    diagram, constant = None, "\u03c0 = 3.14159"
    hint = "Surface area of a cone = \u03c0rl + \u03c0r\u00B2"
    video, website = None, "https://www.web-formulas.com/Math_Formulas/Geometry_Surface_of_Cone.aspx"
    q = cf.Question(cf.currentFuncName())
    q.questionBase, q.answerBase, q.diagram, q.constant, q.hint, q.website = questionBase, answer, diagram, constant, hint, website
    q.piclink = cone()
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()
    
def ed_ch_use_surface_area_formula_to_find_an_unknown_value_in_a_sphere25():
    r = randint(1,10)
    area = round(4*3.1415926*r*r, 2)
    values = (("radius",r, "cm"),("surface area", area, "cm\u00b2"))
    choices = []
    num = randint(0, len(values)-1)
    for i in range(len(values)):
        while num in choices:
            num = randint(0, len(values)-1)
        choices.append(num)
    questionBase = [
        f"In the sphere above,",
        f"{values[choices[0]][0]} = {values[choices[0]][1]} {values[choices[0]][2]}.",
        f"Find {values[choices[1]][0]}."]
    answer = f"{values[choices[1]][1]} {values[choices[1]][2]}"
    diagram, constant = None, "\u03c0 = 3.14159"
    hint = "Surface area of a sphere = 4\u03c0r\u00B2"
    video, website = None, "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fimages-na.ssl-images-amazon.com%2Fimages%2FI%2F61WN2k1l5wL._SL1461_.jpg&f=1&nofb=1"
    q = cf.Question(cf.currentFuncName())
    q.questionBase, q.answerBase, q.diagram, q.constant, q.hint, q.website = questionBase, answer, diagram, constant, hint, website
    q.piclink = sphere()
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()
    
def ed_ci_use_surface_area_formula_to_find_an_unknown_value_in_a_cyinder25():
    r = randint(1,10)
    h = randint(1,10)
    area = round(2*3.1415926*r*h + 2*3.1415926*r*r, 2)
    values = (("the radius",r, "cm"), ("the height",h,"cm"),("the surface area", area, "cm\u00b2"))
    choices = []
    num = randint(0, len(values)-1)
    for i in range(len(values)):
        while num in choices:
            num = randint(0, len(values)-1)
        choices.append(num)
    questionBase = [
        f"In the cylinder above,",
        f"{values[choices[0]][0]} = {values[choices[0]][1]}{values[choices[0]][2]} and",
        f"{values[choices[1]][0]} = {values[choices[1]][1]}{values[choices[1]][2]}",
        f"Find {values[choices[2]][0]}."]
    answer = f"{values[choices[2]][1]}{values[choices[2]][2]}"
    diagram, constant = None, "\u03c0 = 3.14159"
    hint = "Surface area of a cylinder = 2\u03c0rh + 2\u03c0r\u00B2"
    video, website = None, "https://mathopenref.com/cylinderareamain.html"
    q = cf.Question(cf.currentFuncName())
    q.piclink = cylinder()
    q.questionBase, q.answerBase, q.diagram, q.constant, q.hint, q.website = questionBase, answer, diagram, constant, hint, website
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()

def ed_cj_use_surface_area_formula_to_find_an_unknown_value_in_a_cone25():
    r = randint(1,10)
    l = randint(1,10)
    area = round(3.1415926*r*l + 3.1415926*r*r, 2)
    values = (("radius",r, "cm"), ("length",l,"cm"),("surface area", area, "cm\u00b2"))
    choices = []# first two numbers in this list will be used to choose two out of the above to make question and final number in list for the question
    num = randint(0, len(values)-1)#choose a random number between 0 and 2
    for i in range(len(values)):
        while num in choices:#if num is is choices, get another number and try to add it
            num = randint(0, len(values)-1)
        choices.append(num)
    questionBase = [
        f"In the cone above:",
        f"{values[choices[0]][0]} = {values[choices[0]][1]} {values[choices[0]][2]} and",
        f"{values[choices[1]][0]} = {values[choices[1]][1]} {values[choices[1]][2]}.",
        f"Find the {values[choices[2]][0]}."]
    answer = f"{values[choices[2]][1]} {values[choices[2]][2]}"
    diagram, constant = None, "\u03c0 = 3.14159"
    hint = "Surface area of a cone = \u03c0rl + \u03c0r\u00B2"
    video, website = None, "https://www.web-formulas.com/Math_Formulas/Geometry_Surface_of_Cone.aspx"
    q = cf.Question(cf.currentFuncName())
    q.questionBase, q.answerBase, q.diagram, q.constant, q.hint, q.website = questionBase, answer, diagram, constant, hint, website
    q.piclink = cone()
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()
    
def ed_ck_problem_hemisphere36():
    r = randint(1,10)
    area = round((4*3.1415926*r*r)/2 + 3.1415926*r*r, 2)
    values = (("the radius",r, "cm"),("the surface area", area, "cm\u00b2"))
    choices = []
    num = randint(0, len(values)-1)
    for i in range(len(values)):
        while num in choices:
            num = randint(0, len(values)-1)
        choices.append(num)
    questionBase = [
        f"In the hemisphere above:",
        f"{values[choices[0]][0]} = {values[choices[0]][1]} {values[choices[0]][2]}.",
        f"Find {values[choices[1]][0]}."]
    answer = f"{values[choices[1]][1]}{values[choices[1]][2]}"
    diagram, constant = None, "\u03c0 = 3.14159"
    hint = "A hemisphere is exactly half of a sphere, and don't forget that a hemisphere also has a flat face. So: 4\u03c02r\u00B2 \u00f7 2 + 2\u03c0r\u00B2. This can be simplified to 3\u03c0r\u00B2"
    video, website = None, "http://mathcentral.uregina.ca/QQ/database/QQ.09.07/h/nicholas4.html"
    q = cf.Question(cf.currentFuncName())
    q.questionBase, q.answerBase, q.diagram, q.constant, q.hint, q.website = questionBase, answer, diagram, constant, hint, website
    q.piclink = hemisphere()
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()
    
def ed_da_identify_the_3D_shape13():
    options = ((prism(), "prism"),(sphere(),"sphere"),(pyramid(), "pyramid"),(sphere(),"sphere"),(cone(),"cone"),(frustum(),"frustum"),(hemisphere(),"hemisphere"))
    choice = randint(0,len(options)-1)
    answer = f"{options[choice][1]}"
    questionBase = "What is the name of the 3D shape in the image above?"
    diagram, constant = None, "\u03c0 = 3.14159"
    hint = "Surface area only applies to 3D objects and it's the total area of all the faces when added together."
    video, website, piclink = None, "https://revisionmaths.com/gcse-maths/geometry-and-measures/3d-shapes", f"{options[choice][0]}"
    q = cf.Question(cf.currentFuncName())
    q.piclink = options[choice][0]
    q.questionBase, q.answerBase, q.diagram, q.constant, q.hint, q.website = questionBase, answer, diagram, constant, hint, website
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()
    
def ed_db_definitions_of_3D_shapes13():
    people = peopleGen()
    true_tuple = ("a prism is a solid (3D) object which is the same all the way through",
                  "a prism has a constant area of cross section all the way though",
                  "if a prism has a circular cross section, it can be called a cylinder",
                  "a cylinder is a type of prism",
                  "a sphere has a constant radius, wherever you measure it",
                  "if all the sides of a prism are identical squares, it is called a cube",
                  "a pyramid is a shape that goes from a flat base up to a point at the top",
                  "a pyramid's base can be any shape at all",
                  "if a pyramid's base is circular, it is called a cone",
                  "a frustum is left when the top of a cone is cut off parallel to its base")
    false_tuple= ("a prism is a solid (3D) object which isn't always the same all the way through",
                  "the cross section of a prism can change",
                  "a cylinder is not a prism",
                  "any shape with a circular base is a cylinder",
                  "a cube is not a type of prism",
                  "a pyramid is a shape that goes from a flat base up to flat top",
                  "a pyramid's base must be square",
                  "a cone is not a pyramid",
                  "if you cut a cone parallel to its base, a frustum is the smaller cone at the top")
    choice = randint(0,1)
    answer = "Correct" if choice == 1 else "Incorrect"
    statement = true_tuple[randint(0,len(true_tuple)-1)] if answer == "Correct" else false_tuple[randint(0,len(false_tuple)-1)]
    questionBase = [
        f"{people[randint(0,len(people)-1)]} says that {statement}.",
        f"Is this statement correct or incorrect?"]
    diagram, constant = None, "\u03c0 = 3.14159"
    hint = "Surface area only applies to 3D objects and it's the total area of all the faces when added together."
    video, website, piclink = None, None, None
    q = cf.Question(cf.currentFuncName())
    q.questionBase, q.answerBase, q.diagram, q.constant, q.hint, q.website = questionBase, answer, diagram, constant, hint, website
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()
    
def ed_dc_volume_formulas13():
    values = (("prism", "cross-sectional area \u00d7 length"),
              ("cylinder","\u03c0r\u00b2 \u00d7 length"),
              ("sphere", "4\u20443\u03c0r\u00b3"),
              ("pyramid", "\u2153 \u00d7 area of base \u00d7 height"),
              ("cone", "\u2153\u03c0r\u00b2h"),
              ("frustum","\u2153\u03c0R\u00b2H - \u2153\u03c0r\u00b2h where R and H are the radius and height of the complete cone and r and h are the radius and height of the smaller cone"),
              ("hemisphere","2\u20443\u03c0r\u00b3"))  
    choice = randint(0,len(values)-1)
    if randint(0,1) == 0 :questionBase, answer = f"What is the formula for the volume of a {values[choice][0]}?", f"{values[choice][1]}"
    else: questionBase, answer = f"The following formula can be used to calculate the surface area of what: {values[choice][1]}?", f"{values[choice][0]}"
    diagram, constant = None, "\u03c0 = 3.14159"
    hint = "All formulas in the link below!"
    video, website = None, "https://byjus.com/maths/three-dimensional-shapes/"
    q = cf.Question(cf.currentFuncName())
    q.questionBase, q.answerBase, q.diagram, q.constant, q.hint, q.website = questionBase, answer, diagram, constant, hint, website
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()
    
'''
Volume of:
prisms
spheres
pyramids
cones
frustrums
hemispheres

rates of flow

problems'''

def ed_dd_volume_of_a_prism_with_cross_sectional_area_known13():
    area = randint(8,80)
    length = randint(5,10)
    volume = area * length
    questionBase =[
        f"In the diagram above (not to scale) the cross sectional area of the prism is {area}cm\u00b2",
        f"and the length is {length}cm.",
        f"Find the volume of the prism"]
    answer = f"{volume} cm\u00b3"
    diagram, constant = None, "\u03c0 = 3.14159"
    hint = "Volume of a prism = cross sectional area \u00d7 length"
    video, website = None, "https://www.wikihow.com/Calculate-the-Volume-of-a-Prism"
    q = cf.Question(cf.currentFuncName())
    q.questionBase, q.answerBase, q.diagram, q.constant, q.hint, q.website = questionBase, answer, diagram, constant, hint, website
    q.piclink = prism()
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()
    
def ed_de_volume_of_a_sphere_with_radius_known25():
    r = randint(8,80)
    volume = round(4/3 * 3.14159 * r * r * r, 2)
    questionBase =[
        f"In the diagram above (not to scale) the radius of the sphere is {r}cm.",
        f"Find the volume of the sphere."]
    answer = f"{volume} cm\u00b3"
    diagram, constant = None, "\u03c0 = 3.14159"
    hint = "Volume of a sphere = 4\u20443\u03c0r\u00b3"
    video, website = None, "https://www.onlinemathlearning.com/volume-of-a-sphere.html"
    q = cf.Question(cf.currentFuncName())
    q.questionBase, q.answerBase, q.diagram, q.constant, q.hint, q.website = questionBase, answer, diagram, constant, hint, website
    q.piclink = sphere()
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()
    
def ed_df_volume_of_a_pyramid_with_base_and_height_known25():
    base = randint(10,40)
    height = randint(5,20)
    volume = round(1/3 * base * height, 2)
    questionBase = [
        f"In the diagram above (not to scale):",
        f"the verticle height of the pyramid is {height}cm and",
        f"area of the base is {base}cm\u00b2.",
        f"Find the volume of the pyramid."]
    answer = f"{volume} cm\u00b3"
    diagram, constant = None, "\u03c0 = 3.14159"
    hint = "volume of pyramid = \u2153 \u00d7 area of base \u00d7 height"
    video, website = None, "https://www.bbc.co.uk/bitesize/guides/zcnb8mn/revision/6"
    q = cf.Question(cf.currentFuncName())
    q.questionBase, q.answerBase, q.diagram, q.constant, q.hint, q.website = questionBase, answer, diagram, constant, hint, website
    q.piclink = pyramid()
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()
    
def ed_dg_volume_of_a_cone_with_radius_and_height_known25():
    r = randint(5,20)
    height = randint(5,20)
    volume = round(1/3 * (3.1415 * r * r) * height, 2)
    questionBase = [
        f"In the diagram above (not to scale):",
        f"the verticle height of the cone is {height} cm and",
        f"radius the base is {r} cm.",
        f"Find the volume of the pyramid."]
    answer = f"{volume} cm\u00b3"
    diagram, constant = None, "\u03c0 = 3.14159"
    hint = "volume of pyramid = \u2153 \u00d7 area of base \u00d7 height"
    video, website = None, "https://www.bbc.co.uk/bitesize/guides/zcnb8mn/revision/6"
    q = cf.Question(cf.currentFuncName())
    q.questionBase, q.answerBase, q.diagram, q.constant, q.hint, q.website = questionBase, answer, diagram, constant, hint, website
    q.piclink = cone()
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()
    
def ed_dh_volume_of_a_frustrum_with_volume_of_original_cone_known46():
    oc = randint(700, 1000)
    r = randint(5,15)
    height = randint(12,30)
    volume = round(oc - (1/3 * (3.1415 * r * r) * height), 2)
    questionBase = [
        f"In the diagram above (not to scale):",
        f"the volume of the original cone is {oc} cm\u00b3,",
        f"the height of the removed cone is {height} cm and",
        f"the radius of the base of the removed cone is {r} cm.",
        "Find the volume of the cone."]
    answer = f"{volume} cm\u00b3"
    diagram, constant = None, "\u03c0 = 3.14159"
    hint = "volume of frustum of a cone = volume of original cone - volume of removed cone (volume of cone = \u2153 \u00d7 \u03c0r\u00d7\u00b2 \u00d7 height)"
    video, website = None, "https://www.bbc.co.uk/bitesize/guides/zcnb8mn/revision/6"
    q = cf.Question(cf.currentFuncName())
    q.questionBase, q.answerBase, q.diagram, q.constant, q.hint, q.website = questionBase, answer, diagram, constant, hint, website
    q.piclink = cone()
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()
    
def ed_di_volume_of_a_hemisphere_with_radius_known35():
    r = randint(8,80)
    volume = round(2/3 * 3.14159 * r * r * r, 2)
    questionBase = [
        f"In the diagram above (not to scale) the radius of the hemisphere is {r} cm.",
        "Find the volume of the hemispheresphere."]
    answer = f"{volume} cm\u00b3"
    diagram, constant = None, "\u03c0 = 3.14159"
    hint = "Volume of a sphere = \u2154\u03c0r\u00b3"
    video, website = None, "https://www.onlinemathlearning.com/volume-of-a-sphere.html"
    q = cf.Question(cf.currentFuncName())
    q.questionBase, q.answerBase, q.diagram, q.constant, q.hint, q.website = questionBase, answer, diagram, constant, hint, website
    q.piclink = sphere()
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()

'''
ea1 = basics
ea2 = parallel lines
ea3 = geometry problems

eb1 = polygons
eb2 = triangles and quadrilaterals
eb3 = circle geometry

ec1 = congruent shapes
ec2 = similar shapes
ec3 = the four transformations
ec4 = MORE ENLARGEMENTS AND PROJECTIONS

ed1 = area of trianges and quadrilaterals 
ed2 = area of circles

ee1 = 3D shapes and surface area
vertices 
faces 
edges 3

surface area 5
surface area = total area of all faces, area of net, 3d shape folded out flat, 
formulas for surface area of spheres cones and cylinders. 
find sphere
find cylinder
find cone

problem = surface of hemisphere


ee2 = 3D shapes and volume
definition
formulas

Volume
prisms
spheres
pyramids
cones
frustrums
hemispheres


rates of flow

problems



ef1 = Triangle construction
ef2 = Loci and construction

eg1 = bearings
'''


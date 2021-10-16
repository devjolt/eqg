from django.shortcuts import render
from random import randint, randrange
from gcsemaths import gcsemaths_classes_functions as cf
import fractions
import itertools

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
    return cf.moduleListGen(list_callable_functions(), 'p', 0, 1)

def module_path():
    return '/gcsemaths/exam_non_calc/'
    
'''
The name of each function contains:
- paper number and tier eg p1f = paper 1 foundation tier
- exam series eg 18n = 2018 November
- question number eg 9 = question 9 in exam series
- question description
- the number of marks the question is worth
- _ place holder for unused level

Example:
p1f_18n_9_fraction_half_way3_ indicates 
paper 1 foundation in the 2018 November exam series, question 9 worth 3 marks
'''
def p1f_18n_9_fraction_half_way3_():
    number1, number2 = randint(1, 15)/8, randint(1, 15)/8 #create two decimal numbers which can easily be converted to fractions
    while number1 == number2: number2 = randint(1, 16)/8 #make sure second decimal number is different to firs

    printed1 = f"1 {fractions.Fraction(number1-1).numerator}\u2044{fractions.Fraction(number1-1).denominator}" if number1 > 1 else f"{fractions.Fraction(number1).numerator}\u2044{fractions.Fraction(number1).denominator}"
    printed2 = f"1 {fractions.Fraction(number2-1).numerator}\u2044{fractions.Fraction(number2-1).denominator}" if number2 > 1 else f"{fractions.Fraction(number2).numerator}\u2044{fractions.Fraction(number2).denominator}"

    top, bottom = sorted([number1, number2], reverse = True)[0], sorted([number1, number2], reverse = True)[1]
    difference = top - bottom
    mid_point = difference / 2
    answer = bottom + mid_point

    correct = f"1 {fractions.Fraction(answer-1).numerator}\u2044{fractions.Fraction(answer-1).denominator}" if answer > 1 else f"{fractions.Fraction(answer).numerator}\u2044{fractions.Fraction(answer).denominator}" #creates mixed fraction if answer greater than one
    if answer  == 1: correct = '1'

    incorrect = [
        f"{fractions.Fraction(answer-1).numerator}\u2044{fractions.Fraction(answer-1).denominator}" if answer > 1 else f"1 {fractions.Fraction(answer).numerator}\u2044{fractions.Fraction(answer).denominator}",
        f"1 {fractions.Fraction(difference*2-1).numerator}\u2044{fractions.Fraction(difference*2-1).denominator}" if difference*2 > 1 else f"{fractions.Fraction(difference*2).numerator}\u2044{fractions.Fraction(difference*2).denominator}",
        f"{fractions.Fraction(bottom + difference+ mid_point).numerator}\u2044{fractions.Fraction(bottom + difference + mid_point).denominator}"
    ]
    q = cf.Question(cf.currentFuncName(), correct, incorrect)
    q.questionBase = [
        f"Work out the fraction that is halfway between {printed1} and {printed2}.",
        "Give your answer as a mixed fraction if appropriate."]
    q.webLink = 'https://www.mathsisfun.com/fractions_subtraction.html' 
    q.workOn = 'Subtracting fractions'
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()
    
def p1f_18n_10_four_possible_values2_():
    while True:
        try:
            num = randint(2,9)*randint(2,8)
            correct = [i for i in range(1,num+1) if num%i == 0]

            def addStuff(correct, num):
                incorrect = correct.copy()
                del incorrect[randint(0,len(correct)-1)]
                num = randint(1,num-1)
                while num in incorrect:
                    num = randint(1,num-1)
                incorrect.append(num)
                return sorted(incorrect)
            incorrect = [addStuff(correct, num),addStuff(correct, num),addStuff(correct, num)]
            break
        except:
            continue

    q = cf.Question(cf.currentFuncName(), correct, incorrect)
    q.questionBase = [
        f"x is a positive integer.",
        f"{num} \u00f7 x is a positive integer.",
        f"Work out the {len(correct)} possible values of x."]
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()
    
def p1f_18n_11a_probability_dice1_():
    sides, one_of_the_sides = randrange(4,12,2), randint(1,3)
    numbers = []
    for i in range(1,one_of_the_sides+1):
        poss = randint(1,sides)
        while poss in numbers:
            poss = randint(1,sides)
        numbers.append(poss)

    if len(numbers) == 1:
        nums = f'is {numbers[0]}'
    elif len(numbers)==2:
        nums = f'are {numbers[0]} or {numbers[1]}.'
    else:
        nums = f'are {numbers[0]}, {numbers[1]} or {numbers[2]}.'
  
    def all_options(one_of_the_sides, sides):
        correct = one_of_the_sides / sides
        return f"{fractions.Fraction(one_of_the_sides, sides).numerator}\u2044{fractions.Fraction(one_of_the_sides, sides).denominator} (fraction), {round(correct,3)} (decimal), or {round(correct*100,3)}% (percentage)"

    correct = all_options(one_of_the_sides, sides)
    incorrect = [all_options(one_of_the_sides, sides-1), all_options(one_of_the_sides, sides+1), all_options(one_of_the_sides - randrange(-1,1,2), sides)]
    
    q = cf.Question(cf.currentFuncName(), correct, incorrect)
    q.questionBase = [
        f"A fair dice has {sides} sides, numbered 1 to {sides}.",
        f"After it is rolled, {sides - 1} of the numbers can be seen.",
        f"What is the probability that one of these {sides - 1} numbers {nums}"]
    q.webLink = 'https://revisionmaths.com/gcse-maths-revision/statistics-handling-data/probability' 
    q.workOn = 'Probability'
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()
    

def p1f_18n_11b_probability_dice2_():
    sides = randrange(4,12,2)
    num = randint(1,sides)
    all_sides = [i for i in range(1,sides+1)]
    total = sum(all_sides)
    correct = total-num
    incorrect = [total, total - randint(1,sides)+1, sides - num + 1]
    
    q = cf.Question(cf.currentFuncName(), correct, incorrect)
    q.questionBase = [
        f"A fair dice has {sides} sides, numbered 1 to {sides}.",
        f"After it is rolled, {sides - 1} of the numbers can be seen.",
        f"If the number {num} can't be seen, what is the greatest possible sum of the sides which can be seen?"]
    q.webLink = 'https://revisionmaths.com/gcse-maths-revision/statistics-handling-data/probability' 
    q.workOn = 'Knowledge of dice. Kidding. Probability'
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()
    


def p1f_18n_21_number_cards3_():
    cards = list(set([randint(9,25) for i in range(randint(4,6))]))
    combos = [c for i in range(len(cards)+1) for c in itertools.combinations(cards,i)]
    pairs = [i for i in combos if len(i) ==2]
    totals = [i[0] + i[1] for i in pairs]
    target = randint(28,41)
    greater = randint(0,1)
    valid_totals = [i for i in totals if i > target] if greater == 1 else [i for i in totals if i < target]
    greater_less = 'more' if greater == 1 else 'less'
    correct = f"{fractions.Fraction(len(valid_totals),len(totals)).numerator}\u2044{fractions.Fraction(len(valid_totals),len(totals)).denominator}"
    if valid_totals == totals: 
        correct = '1'
        incorrect_option = '0'
    elif valid_totals == 0:
        correct = '0'
        incorrect_option = '1'
    else:
        incorrect_option = str(randint(0,1))

    incorrect = [
        f"{fractions.Fraction(len(valid_totals) + 1,len(totals)).numerator}\u2044{fractions.Fraction(len(valid_totals) + 1,len(totals)).denominator}",
        f"{fractions.Fraction(len(valid_totals) -1 ,len(totals)).numerator}\u2044{fractions.Fraction(len(valid_totals) - 1,len(totals)).denominator}",
        incorrect_option,
    ]
    q = cf.Question(cf.currentFuncName(), correct, incorrect)
    q.questionBase = [
        f"Here are {len(cards)} number cards:",
        f"{cards}",
        f"Two of the {len(cards)} cards are picked at random.",
        f"Work out the probability that the total of the two numbers is {greater_less} than {target}"]
    q.webLink = 'https://revisionmaths.com/gcse-maths-revision/statistics-handling-data/probability' 
    q.workOn = 'Probability'
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_callable_functions(), cf.currentFuncName(), module_path(), cf.currentFuncName()[0:2], 0, 2)
    return q.returnAll()
    
#def p1f_18n_30_work_out_the_percentage3(request):
#    fro, to = randint(2,12)*10, randint(24,36)*10

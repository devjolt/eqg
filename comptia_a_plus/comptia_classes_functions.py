from random import randint, shuffle
import sys
import re
from utilities import universal_classes_functions as eqg

from comptia_a_plus.a_core_1_220_1001 import aa_mobile_devices_logic, ab_networking_technology_logic, ac_hardware_logic, ad_virtualisation_cloud_computing_logic, ae_troubleshooting_logic

currentFuncName = lambda n=0: sys._getframe(n + 1).f_code.co_name # allows previousNext functionality to work by getting current function's name

class Question(eqg.UniversalQuestion):
    '''
    Adds ability to include drag and drop pairs

    '''
    pair1a, pair1b, pair2a, pair2b, pair3a, pair3b, pair4a, pair4b, pair5a, pair5b, pair6a, pair6b = None, None, None, None, None, None, None, None, None, None, None, None
    pair7a, pair7b, pair8a, pair8b, pair9a, pair9b, pair10a, pair10b, pair11a, pair11b, pair12a, pair12b = None, None, None, None, None, None, None, None, None, None, None, None

    template = None
    num = randint(0,3)

    def item(self, iterable):
        return iterable[randint(0, len(iterable)-1)]

    def returnAll(self):
        return{
        'previousQ': self.previousQ, 'nextQ': self.nextQ, #previous and next question links
        'currentQname':self.currentQname, 'previousQname':self.previousQname, 'nextQname':self.nextQname,
        'hint': self.hint, 'workon': self.workon, 'weblink': self.weblink, 'video': self.video, #string containing instruction, string describing skill demonstrated in question, link to useful resource, link to youtube video
        'diagram': self.diagram, 'piclink': self.piclink, #link to static file, url if image from web
        'qtype': self.qtype, 'correctRequired': self.correctRequired, 'answerReveal': self.answerReveal,
        'constantList':self.constantList,
        'constant':self.constant,

        'questionNumber':self.questionNumber, 'questionBase': self.questionBase, 'codeBase': self.codeBase, 'answerBase': self.answerBase, 'answerCodeBase': self.answerCodeBase, 'answerUnits':self.answerUnits, 'marksBase': self.marksBase,

        'beforeType':self.beforeType, 'afterType':self.afterType,#for placing text either side of text to be entered

        'questionPartList': self.questionPartList,#list of dictionaries containing: sub_number, sub_question, sub_answer, sub_mark

        'a1':self.a1, 'a2':self.a2, 'a3':self.a3, 'a4':self.a4, 'a5':self.a5, 'a6':self.a6, 'a7':self.a7, 'a8':self.a8, 'a9':self.a9, 'a10':self.a10, 'a11':self.a11, 'a12':self.a12, #mc choices
        'a1code':self.a1code, 'a2code':self.a2code, 'a3code':self.a3code, 'a4code':self.a4code, 'a5code':self.a5code, 'a6code':self.a6code, 'a7code':self.a7code, 'a8code':self.a8code,'a9code':self.a9code,'a10code':self.a10code,'a11code':self.a11code,'a12code':self.a12code, #mc choices for pre formatting when code is used
        'a1ci': self.a1ci, 'a2ci':self.a2ci, 'a3ci': self.a3ci, 'a4ci': self.a4ci, 'a5ci': self.a5ci, 'a6ci': self.a6ci,'a7ci': self.a7ci,'a8ci': self.a8ci,'a9ci': self.a9ci,'a10ci': self.a10ci, 'a11ci': self.a11ci,'a12ci': self.a12ci, #correct/incorrect indicators for all options
        'multi_correct':self.multi_correct,

        'pair1a': self.pair1a, 'pair1b': self.pair1b, 'pair2a': self.pair2a, 'pair2b': self.pair2b, 'pair3a': self.pair3a, 'pair3b': self.pair3b, 'pair4a': self.pair4a, 'pair4b': self.pair4b, 'pair5a': self.pair5a, 'pair5b': self.pair5b, 
        'pair6a': self.pair6a, 'pair6b': self.pair6b, 'pair7a': self.pair7a, 'pair7b': self.pair7b, 'pair8a': self.pair8a, 'pair8b': self.pair8b, 'pair9a': self.pair9a, 'pair9b': self.pair9b, 'pair10a': self.pair10a, 'pair10b': self.pair10b, 
        'options': self.options#false option fillers
    }
            
class SelectMcDrag(Question):
    options = None#used 
    choice = None#used to change pairs into correct, incorrect lists for use in select questions, must be available for use in question
    filler_pairs = None

    def __init__(self, qtype = None, correct = None, incorrect = None, pairs = None, fillers = [], marks = 1, correctRequired = 1, numOptions = 4, ):
        self.correct = correct
        self.incorrect = incorrect
        self.pairs = pairs
        self.fillers = fillers
        self.marks = marks
        self.correctRequired = correctRequired
        self.numOptions = numOptions
        self.qtype = qtype

        self.make_nums()#needs to happen automatically, decide where correct responses will be inserted into list of mc/select/drag options
        self.select_qtype()#select question type based on combination of assets provided above
        

    def select_qtype(self):
        """based on what is inputted on instantiation, what sort of question will we be doing?
        'select', 'multi', 'drag'
        """
        choice = randint(0,1)
        if self.correct != None: #if a list of correct items is supplied
            self.populate_select_multi_using_correct_incorrect()#generate logic for select or mc question
            if self.qtype == None:#if qtype is not specified, choose randomly between valid types select and submit or multiple choice
                self.qtype = 'select' if choice == 0 else 'multi'#change flag for template
        elif self.pairs != None:#if a list of pairs is supplied, proceed with drag and drop/multi choice logic
            if self.qtype == 'drag':
                self.populate_drag_using_pairs()
            elif self.qtype == 'multi':
                self.populate_multi_using_pairs()
            elif self.qtype == 'select':
                self.populate_multi_using_pairs()
            elif self.qtype == None:
                self.qtype = 'select' if choice == 0 else 'multi'
                self.populate_multi_using_pairs()

    def populate_select_multi_using_correct_incorrect(self):
        self.answers_mangle()#insert correct responses into list of options using values generated above
        self.reveal_answer_generator()#create answerReveal for revealing answer. Must happen after answers mangle
        self.correct_incorrect_sequence()#create list containing indicators to show where answer at given index is correct or incorrect

    def populate_multi_using_pairs(self):
        self.make_correct_incorrect()
        self.answers_mangle()#insert correct responses into list of options using values generated above
        self.reveal_answer_generator()#create answerReveal for revealing answer. Must happen after answers mangle
        self.correct_incorrect_sequence()#create list containing indicators to show where answer at given index is correct or incorrect

    def make_nums(self):
        """Decide where correct responses should be inserted into list of mc options
        """
        self.nums = []
        for i in range(self.correctRequired):
            num = randint(0, self.numOptions - 1)
            while num in self.nums:
                num = randint(0, self.numOptions - 1)
            self.nums.append(num)
        self.nums = sorted(self.nums)

    def make_correct_incorrect(self):
        self.choice = randint(0, len(self.pairs)-1)
        self.correct = (self.pairs[self.choice][1],)
        self.incorrect = tuple([i[1] for i in self.pairs if self.pairs.index(i)!= self.choice]) + tuple(self.fillers)

    def answers_mangle(self):
        """Assign self.ax mc option variables to correct and incorrect answers
        assign self.answerx correct answer variables with correct answers"""
        options = []
        for i in range(self.numOptions - self.correctRequired):#populate options with random but different incorrect answers from list, leaving space for correct answers
            option = tuple(self.incorrect)[randint(0, len(tuple(self.incorrect)) - 1)]
            while option in options:
                option = tuple(self.incorrect)[randint(0, len(tuple(self.incorrect)) - 1)]
            options.append(option)
        corList = []
        for i in range(self.correctRequired):
            cor = self.correct[randint(0, len(self.correct) - 1)]
            while cor in corList:
                cor = self.correct[randint(0, len(self.correct) - 1)]
            options.insert(self.nums[i], cor)#add correct items to options at locations in self.num
            corList.append(cor)#add correct items to corList so that they can be assigned to self.answerx variables

        while len(options) != 10:#as we have a maximum of 10 self.ax multi choice option variables to assign using this list, 
            options.append(None)#list needs to be topped up to len(10) with None values to allow the following:
        self.a1, self.a2, self.a3, self.a4, self.a5, self.a6, self.a7, self.a8, self.a9, self.a10 = options[0], options[1], options[2], options[3], options[4], options[5], options[6], options[7], options[8], options[9]

        while len(corList) != 3:#as we have a maximum of 3 correct self.answerx variables to assign using this list, 
            corList.append(None)#list topped up to len(3) with None values to allow the following:
        self.answer1, self.answer2, self.answer3 = corList[0], corList[1], corList[2]

    def correct_incorrect_sequence(self):
        """assigns self.axci variables up to 10 ordered strings consisting of int(correctRequired) "correct" 
        and int(numOptions - correctRequired) "incorrect"s to be used as flags for js in template."""
        listy = ['incorrect' for i in range(self.numOptions - self.correctRequired)]#populates listy with incorrect flags
        for i in range(self.correctRequired):
            listy.insert(self.nums[i], 'correct')#adds 'correct' flags to listy at appropriate locations
        while len(listy) != 10:
            listy.append(None)#tops up len of listy to 10 to allow:
        self.a1ci, self.a2ci, self.a3ci, self.a4ci, self.a5ci = listy[0], listy[1], listy[2], listy[3], listy[4]
        self.a6ci, self.a7ci, self.a8ci, self.a9ci, self.a10ci = listy[5], listy[6], listy[7], listy[8], listy[9]

    def reveal_answer_generator(self):
        self.answerReveal = self.answer1
        if self.answer2 != None:
            self.answerReveal += f", {self.answer2}"
            if self.answer3 != None:
                self.answerReveal += f", {self.answer3}"

    

    def populate_drag_using_pairs(self):
        correct_pairs = []
        for i in range(self.correctRequired):
            pair = self.pairs[randint(0, len(self.pairs)-1)]
            while pair in correct_pairs:
                pair = self.pairs[randint(0, len(self.pairs)-1)]
            correct_pairs.append(pair)
        
        self.answerReveal = ''
        for item in correct_pairs:
            self.answerReveal += f"{item[0]} - {item[1]}; "
        self.answerReveal = self.answerReveal[:-2]

        while len(correct_pairs) < 10:
            correct_pairs.append((None, None))

        options_to_drag = []
        for i in range(self.correctRequired):
            options_to_drag.append(correct_pairs[i][1])

        if len(self.pairs) < self.numOptions:
            for i in range(self.numOptions-len(self.pairs)):
                filler = self.fillers[randint(0, len(self.fillers)-1)]
                while filler in options_to_drag:
                    filler = self.fillers[randint(0, len(self.fillers)-1)]
                options_to_drag.append(filler)
        else:
            while len(options_to_drag) != self.numOptions:
                filler = self.pairs[randint(0, len(self.pairs)-1)][1]
                while filler in options_to_drag:
                    filler = self.pairs[randint(0, len(self.pairs)-1)][1]
                options_to_drag.append(filler)


        shuffle(options_to_drag)
    
        self.pair1a, self.pair1b, self.pair2a, self.pair2b = correct_pairs[0][0], correct_pairs[0][1], correct_pairs[1][0], correct_pairs[1][1]
        self.pair3a, self.pair3b, self.pair4a, self.pair4b = correct_pairs[2][0], correct_pairs[2][1], correct_pairs[3][0], correct_pairs[3][1]
        self.pair5a, self.pair5b, self.pair6a, self.pair6b = correct_pairs[4][0], correct_pairs[4][1], correct_pairs[5][0], correct_pairs[5][1]
        self.pair7a, self.pair7b, self.pair8a, self.pair8b = correct_pairs[6][0], correct_pairs[6][1], correct_pairs[7][0], correct_pairs[7][1]
        self.pair9a, self.pair9b, self.pair10a, self.pair10b = correct_pairs[8][0], correct_pairs[8][1], correct_pairs[9][0], correct_pairs[9][1]
        
        #self.a1, self.a2, self.a3, self.a4, self.a5 = filler_pairs[0], filler_pairs[1], filler_pairs[2], filler_pairs[3], filler_pairs[4]
        #self.a6, self.a7, self.a8, self.a9, self.a10 = filler_pairs[5], filler_pairs[6], filler_pairs[7], filler_pairs[8], filler_pairs[9]

        self.options = list(options_to_drag)

    """
    After completing above functions, 
    next step here is making an html template to handle the data we feed it...

    Suggestion is two columns, one for things you're looking for and the other for options
    """

class MultipleChoice(Question):
    nums = None
    def __init__(self, correct, incorrect, marks = 1, correctRequired = 1, numOptions = 4, qtype = 'rand'):
        self.correct = correct#list containing possible correct resonses
        self.incorrect = incorrect# list containing possible incorrect responses
        self.marks = marks
        self.correctRequired = correctRequired# number of correct choices needed for a mark to be awarded
        self.numOptions = numOptions# number of multiple choice options to choose from
        self.qtype = qtype

        self.qtype_selector()
        self.make_nums()#decide where correct responses will be inserted into list of mc options
        self.answers_mangle()#insert correct responses into list of options using values generated above
        self.reveal_answer_generator()#create answerReveal for revealing answer. Must happen after answers mangle
        self.correct_incorrect_sequence()#create list containing indicators to show where answer at given index is correct or incorrect

    def qtype_selector(self):
        if self.qtype != 'rand':
            return
        else:
            self.qtype = 'multi' if randint(0,1) == 1 else 'select'

    def make_nums(self):
        """Decide where correct responses should be inserted into list of mc options
        """
        self.nums = []
        for i in range(self.correctRequired):
            num = randint(0, self.numOptions - 1)
            while num in self.nums:
                num = randint(0, self.numOptions - 1)
            self.nums.append(num)
        self.nums = sorted(self.nums)
    
    def answers_mangle(self):
        """Assign self.ax mc option variables to correct and incorrect answers
        assign self.answerx correct answer variables with correct answers"""
        options = []
        for i in range(self.numOptions - self.correctRequired):#populate options with random but different incorrect answers from list, leaving space for correct answers
            option = tuple(self.incorrect)[randint(0, len(tuple(self.incorrect)) - 1)]
            while option in options:
                option = tuple(self.incorrect)[randint(0, len(tuple(self.incorrect)) - 1)]
            options.append(option)
        corList = []
        for i in range(self.correctRequired):
            cor = self.correct[randint(0, len(self.correct) - 1)]
            while cor in corList:
                cor = self.correct[randint(0, len(self.correct) - 1)]
            options.insert(self.nums[i], cor)#add correct items to options at locations in self.num
            corList.append(cor)#add correct items to corList so that they can be assigned to self.answerx variables

        while len(options) != 10:#as we have a maximum of 10 self.ax multi choice option variables to assign using this list, 
            options.append(None)#list needs to be topped up to len(10) with None values to allow the following:
        self.a1, self.a2, self.a3, self.a4, self.a5, self.a6, self.a7, self.a8, self.a9, self.a10 = options[0], options[1], options[2], options[3], options[4], options[5], options[6], options[7], options[8], options[9]

        while len(corList) != 3:#as we have a maximum of 3 correct self.answerx variables to assign using this list, 
            corList.append(None)#list topped up to len(3) with None values to allow the following:
        self.answer1, self.answer2, self.answer3 = corList[0], corList[1], corList[2]

    def correct_incorrect_sequence(self):
        """assigns self.axci variables up to 10 ordered strings consisting of int(correctRequired) "correct" 
        and int(numOptions - correctRequired) "incorrect"s to be used as flags for js in template."""
        listy = ['incorrect' for i in range(self.numOptions - self.correctRequired)]#populates listy with incorrect flags
        for i in range(self.correctRequired):
            listy.insert(self.nums[i], 'correct')#adds 'correct' flags to listy at appropriate locations
        while len(listy) != 10:
            listy.append(None)#tops up len of listy to 10 to allow:
        self.a1ci, self.a2ci, self.a3ci, self.a4ci, self.a5ci = listy[0], listy[1], listy[2], listy[3], listy[4]
        self.a6ci, self.a7ci, self.a8ci, self.a9ci, self.a10ci = listy[5], listy[6], listy[7], listy[8], listy[9]

    def reveal_answer_generator(self):
        self.answerReveal = self.answer1
        if self.answer2 != None:
            self.answerReveal += f", {self.answer2}"
            if self.answer3 != None:
                self.answerReveal += f", {self.answer3}"

class DragAndDrop(Question):
    """
    Select num_correct pairs
    Select num_options - num_correct pairs to make up to total needed options
    pass these into the template how do these need to go into the template

    a1

    b2
    a2    
    """
    pair1a, pair1b, pair2a, pair2b, pair3a, pair3b, pair4a, pair4b, pair5a, pair5b, pair6a, pair6b = None, None, None, None, None, None, None, None, None, None, None, None
    pair7a, pair7b, pair8a, pair8b, pair9a, pair9b, pair10a, pair10b, pair11a, pair11b, pair12a, pair12b = None, None, None, None, None, None, None, None, None, None, None, None

    filler_pairs = None
    qtype = 'drag'
    options = None

    def __init__(self, pairs, fillers, marks = 1, correctRequired = 1, numOptions = 4):
        self.pairs = pairs
        self.fillers = fillers
        self.marks = marks
        self.correctRequired = correctRequired
        self.numOptions = numOptions

        self.make_nums()
        self.select_and_assign_correct_pairs_and_options()

    def make_nums(self):
        """Decide where correct responses should be inserted into list of mc options
        """
        self.nums = []
        for i in range(self.correctRequired):
            num = randint(0, self.numOptions - 1)
            while num in self.nums:
                num = randint(0, self.numOptions - 1)
            self.nums.append(num)
        self.nums = sorted(self.nums)

    def select_and_assign_correct_pairs_and_options(self):
        correct_pairs = []
        for i in range(self.correctRequired):
            pair = self.pairs[randint(0, len(self.pairs)-1)]
            while pair in correct_pairs:
                pair = self.pairs[randint(0, len(self.pairs)-1)]
            correct_pairs.append(pair)
        

        self.answerReveal = ''
        for item in correct_pairs:
            self.answerReveal += f"{item[0]} - {item[1]}; "
        self.answerReveal = self.answerReveal[:-2]

        while len(correct_pairs) < 10:
            correct_pairs.append((None, None))

        options_to_drag = []
        for i in range(self.correctRequired):
            options_to_drag.append(correct_pairs[i][1])

        if len(self.pairs) < self.numOptions:
            for i in range(self.numOptions-len(self.pairs)):
                filler = self.fillers[randint(0, len(self.fillers)-1)]
                while filler in options_to_drag:
                    filler = self.fillers[randint(0, len(self.fillers)-1)]
                options_to_drag.append(filler)
        else:
            while len(options_to_drag) != self.numOptions:
                filler = self.pairs[randint(0, len(self.pairs)-1)][1]
                while filler in options_to_drag:
                    filler = self.pairs[randint(0, len(self.pairs)-1)][1]
                options_to_drag.append(filler)


        shuffle(options_to_drag)
    
        self.pair1a, self.pair1b, self.pair2a, self.pair2b = correct_pairs[0][0], correct_pairs[0][1], correct_pairs[1][0], correct_pairs[1][1]
        self.pair3a, self.pair3b, self.pair4a, self.pair4b = correct_pairs[2][0], correct_pairs[2][1], correct_pairs[3][0], correct_pairs[3][1]
        self.pair5a, self.pair5b, self.pair6a, self.pair6b = correct_pairs[4][0], correct_pairs[4][1], correct_pairs[5][0], correct_pairs[5][1]
        self.pair7a, self.pair7b, self.pair8a, self.pair8b = correct_pairs[6][0], correct_pairs[6][1], correct_pairs[7][0], correct_pairs[7][1]
        self.pair9a, self.pair9b, self.pair10a, self.pair10b = correct_pairs[8][0], correct_pairs[8][1], correct_pairs[9][0], correct_pairs[9][1]
        
        #self.a1, self.a2, self.a3, self.a4, self.a5 = filler_pairs[0], filler_pairs[1], filler_pairs[2], filler_pairs[3], filler_pairs[4]
        #self.a6, self.a7, self.a8, self.a9, self.a10 = filler_pairs[5], filler_pairs[6], filler_pairs[7], filler_pairs[8], filler_pairs[9]

        self.options = list(options_to_drag)

    """
    After completing above functions, 
    next step here is making an html template to handle the data we feed it...

    Suggestion is two columns, one for things you're looking for and the other for options
    """

def view_builder(module, name):
    '''returns template dictionary for a named function containing everything a view needs to populate a template and display
    module = string containing name of given module
    name = string containing name of a given function
    
    RELIES ON IMPORTING MODULE
    '''
    passed = eval(f"{module}.{name}()")#gets tuple from named function in logic file
    return passed

moduleListGen = eqg.moduleListGen
previousNext = eqg.previousNext

#cleans underscores and code from module name for use in quesitons. 
def underscoreless(name):
    return re.sub('_',' ',name[5:])

def mcRevealTemplate():
    return "comptia_a_plus/mcReveal.html"
def dragRevealTemplate():
    return "comptia_a_plus/dragReveal.html"
def dragDoubleRevealTemplate():
    return "comptia_a_plus/dragDoubleReveal.html"
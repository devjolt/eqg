from random import randint
import re

class UniversalQuestion():
    """
    Returns everything needed for templates handling
    reveal, input, mutliple choice or printable questions 
    """
    '''
    Following variables to be used as strings in template
    '''
    previousQ,nextQ = None, None #populated with string links by previousNext() func
    previousQname,currentQname, nextQname = None, None, None #populated with string link NAMES by previousNext() func

    diagram, piclink = None, None #location of diagram image, link to picture
    hint, workon, weblink, video = None, None, None, None #str(hint), str(something to be imporoved), links to instruction and instructional video

    constantList = None# containing {name, value, units} of a constant
    constant = None#legacy, not required because above exists
    
    level = None#level of question for use in maths, physics etc

    questionNumber = None#as suggested, the number of the question
    questionBase, codeBase = None, None #string for question to be printed onto page, with code formatting

    beforeType, afterType = None, None#strings to appear before and after typed responses
    '''
    Sometimes used to select type of template used
    '''
    qtype = None#type of question(input, drag, multi)
    '''
    Question logic inputs used by JavaScript on templates 
    '''  
    answerBase, answerCodeBase, answerUnits = None, None, None #correct answer (NOTE: is answerReveal above needed?), in code formatting, units for answer
    answerReveal =None#used if revealed answer is composed of several correct answers
    marksBase = 1 # number of marks available for correct repsonse, also visible on template

    #used to build a multi part question
    questionPartList = None # list of dicts: [{#sub_number, sub_question, sub_code_base, sub_answer, sub_answer_code_base, sub_mark},...]

    #12 vars for possible mutli choice answers in both regular and code formatting
    a1, a1code, a2, a2code, a3, a3code, a4, a4code, a5, a5code, a6, a6code = None, None, None, None, None, None, None, None, None, None, None, None
    a7, a7code, a8, a8code, a9, a9code, a10, a10code, a11, a11code, a12, a12code = None, None, None, None, None, None, None, None, None, None, None, None
    #12 correct/incorrect indicator variables for use with above in multi choice
    a1ci, a2ci, a3ci, a4ci, a5ci, a6ci, a7ci, a8ci, a9ci, a10ci, a11ci, a12ci = None, None, None, None, None, None, None, None, None, None, None, None
    multi_correct = None#number of correct answers required for mark
    correctRequired = None#one of these is probably redundant

    nums = None#placeholder used in logic below
    def __init__(self, function_name, correct = None, incorrect = None, marks = 1, correctRequired = 1, numOptions = 4, qtype = 'rand'):
        """
        INITIALISE WITH:
        - only function name required
        - only function name AND correct answer to get a simple base question
        Templates with incorrect = None will not offer multi choice as an option
        qtype allows template to choose between select and submit or sudden death type multi choice
        """
        self.function_name = function_name
        self.correct = correct#list containing possible correct resonses OR single correct answer
        self.incorrect = incorrect# list containing possible incorrect responses for use with mutli choice questions
        self.marks = marks
        self.correctRequired = correctRequired# number of correct choices needed for a mark to be awarded
        self.numOptions = numOptions# number of multiple choice options to choose from
        self.qtype = qtype
        
        if self.correct:#if list of correct answers given
            self.if_multi()#if a list of incorrect answers is passed in, do multi choice logic!
        

    def if_multi(self):
        if len(self.incorrect) != None:#if incorrect is not none, assume it is a list of incorrect responses
            if self.correct != list:#if self.correct not a list, it now needs to be for below functions, even if one item
                self.correct = [self.correct]
            self.make_nums()#decide where correct responses will be inserted into list of mc options
            self.answers_mangle()#insert correct responses into list of options using values generated above
            self.reveal_answer_generator()#create answerReveal for revealing answer. Must happen after answers mangle
            self.correct_incorrect_sequence()#create list containing indicators to show where answer at given index is correct or incorrect
        if self.correct != list:#if self.correct not a list (ie not part of multi choice)...
            self.answerBase = self.correct#make that the base answer because why on earth wouldn't you?


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

    def item(self, iterable):
        return iterable[randint(0, len(iterable)-1)]


    def returnAll(self):
        """
        returns the magical dictionary used to populate a template
        """
        #if self.questionBase != list:#if questionBase is not a list of question lines ie it's just a string:
        #    self.questionBase = [self.questionBase]#make it into a list because that's what the template's expecting!
        
        return{
        'previousQ': self.previousQ, 'nextQ': self.nextQ, #previous and next question links
        'currentQname':self.currentQname, 'previousQname':self.previousQname, 'nextQname':self.nextQname,
        
        'diagram': self.diagram, 'piclink': self.piclink, #link to static file, url if image from web
        'hint': self.hint, 'workon': self.workon, 'weblink': self.weblink, 'video': self.video, #string containing instruction, string describing skill demonstrated in question, link to useful resource, link to youtube video
        
        'constantList':self.constantList,
        'constant':self.constant,

        'level':self.level,#level of question for use in maths, physics etc

        'questionNumber':self.questionNumber,
        'questionBase': self.questionBase, 'codeBase': self.codeBase,

        'beforeType':self.beforeType, 'afterType':self.afterType,#for placing text either side of text to be entered

        'qtype': self.qtype, 
        
        'answerBase': self.answerBase, 'answerCodeBase': self.answerCodeBase, 'answerUnits':self.answerUnits,
        'answerReveal': self.answerReveal,
        'marksBase': self.marksBase,

        'questionPartList': self.questionPartList,#list of dictionaries containing:
        #sub_number, sub_question, sub_code_base, sub_answer, sub_answer_code_base, sub_mark

        'a1':self.a1, 'a2':self.a2, 'a3':self.a3, 'a4':self.a4, 'a5':self.a5, 'a6':self.a6, 'a7':self.a7, 'a8':self.a8, 'a9':self.a9, 'a10':self.a10, 'a11':self.a11, 'a12':self.a12, #mc choices
        'a1code':self.a1code, 'a2code':self.a2code, 'a3code':self.a3code, 'a4code':self.a4code, 'a5code':self.a5code, 'a6code':self.a6code, 'a7code':self.a7code, 'a8code':self.a8code,'a9code':self.a9code,'a10code':self.a10code,'a11code':self.a11code,'a12code':self.a12code, #mc choices for pre formatting when code is used
        'a1ci': self.a1ci, 'a2ci':self.a2ci, 'a3ci': self.a3ci, 'a4ci': self.a4ci, 'a5ci': self.a5ci, 'a6ci': self.a6ci,'a7ci': self.a7ci,'a8ci': self.a8ci,'a9ci': self.a9ci,'a10ci': self.a10ci, 'a11ci': self.a11ci,'a12ci': self.a12ci, #correct/incorrect indicators for all options
        'multi_correct':self.multi_correct,
        'correctRequired': self.correctRequired,
    }

def moduleListGen(entireModuleList, qtype = None, start = 0, end = None): #generates a list of all functions with a certain pattern in their name
    count = -1
    required_module_list = []
    if qtype == None: # use qtype = None to use low high to select slice of list returned in relation to total modules in THIS file, low = -1 for last module only
        for thing in entireModuleList[start:end]:
            count += 1
            required_module_list.append(thing)
    else:
        for thing in entireModuleList:
            if str(thing)[start:end] == qtype: # use qtype ='anystring', low = int representing start of string, high = int representing end of string for modules selected by name
                count += 1
                required_module_list.append(thing)
    return required_module_list

def previousNext(modList, name='', module_path='', qtype = None, start = 0, end = 2):#uses list of all functions to return previous and next modules in list
    '''
    based on def aa_bb_name_of_module()
    where:
    aa denotes mudule and sub module
    bb denotes topic and question identifier
    '''
    modList = moduleListGen(modList, qtype, start, end)#list of all possible functions in a file created here using 
    modDict = {}
    count = -1
    for thing in modList:
        count+=1
        modDict.update({str(thing):count})
    place = modDict[name]
    current = modList[place]
    try:
        next_q = modList[place+1]
    except IndexError:
        next_q = modList[0]
    try:
        previous_q = modList[place-1]
    except IndexError:
        previous_q = modList[-1]

    currentQname = re.sub('_', ' ', current[6:])
    nextQname = re.sub('_', ' ', next_q[6:])
    previousQname = re.sub('_', ' ', previous_q[6:])
    return f"{module_path}{previous_q}", f"{module_path}{next_q}", currentQname, nextQname, previousQname
    # e.g.:/comptia_a_plus/core_1_220_1001/aea1_ram_cmos_issue_symptom_mc

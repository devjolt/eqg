from django.shortcuts import render
from random import randint, randrange
from comptia_a_plus import comptia_classes_functions as cf
from comptia_a_plus import variety_lists as vl

def list_functions():
    """returns list of all modules in this file
    Used by:
    modulesList (to generate a list of all the questions in a module)
    previousNext (to generate sequential links to next and previous practise question)
    This function MUST remain in THIS file to work correctly!
    """
    #entireModuleList = [key for key, value in globals().items() if callable(value) and value.__module__ == __name__]
    entireModuleList = []
    for key, value in globals().items():
        if callable(value) and value.__module__==__name__:
            entireModuleList.append(key)
    return entireModuleList

def modulesList():#this list is used by views to automatically generate views!
    return cf.moduleListGen(list_functions(), 'a', 0, 1)

def allSectionsList():
    section_lists = []
    sections = {
        'a':'laptop hardware', 
        'b':'laptop screens',
        'c':'laptop features',
        'd':'types of devices',
        'e':'cables',
        'f':'connectivity',
        'g':'accessories',
        'h':'connections',
        'i':'connecting to other devices',
        'j':'configuring emails',
        'k':'synchronisation'
        }
    for key, value in sections:
        section_lists.append({key:(value, cf.moduleListGen(list_functions(), key, 2, 3)[0])})
    print(section_lists)
    return section_lists

def module_path():
    return '/comptia_a_plus/core_1_220_1001/'

#paper, series, question, name, marks in names
def test():
    pairs = (
        ('Pair 1 item a', 'Pair 1 item b'),
        ('Pair 2 item a', 'Pair 2 item b'),
        ('Pair 3 item a', 'Pair 3 item b'),
        ('Pair 4 item a', 'Pair 4 item b'),
        ('Pair 5 item a', 'Pair 5 item b'),
        ('Pair 6 item a', 'Pair 6 item b'),
        ('Pair 7 item a', 'Pair 7 item b'),
        ('Pair 8 item a', 'Pair 8 item b'),
        ('Pair 9 item a', 'Pair 9 item b'),
        ('Pair 10 item a', 'Pair 10 item b'),
    )
    correct = (
        'correct1', 'correct2', 'correct3', 'correct4', 'correct5', 
        'correct6', 'correct7', 'correct8', 'correct9', 'correct10'
        )
    incorrect = (#
        'incorrect1', 'incorrect2', 'incorrect3', 'incorrect4', 'incorrect5', 
        'incorrect6', 'incorrect7', 'incorrect8', 'incorrect9', 'incorrect10'
        )
    q = cf.SelectMcDrag('multi', None, None, pairs, () )
    return q.returnAll()

def test_dr():
    pairs = (
        ('Pair 1 item a', 'Pair 1 item b'),
        ('Pair 2 item a', 'Pair 2 item b'),
        ('Pair 3 item a', 'Pair 3 item b'),
        ('Pair 4 item a', 'Pair 4 item b'),
        ('Pair 5 item a', 'Pair 5 item b'),
        ('Pair 6 item a', 'Pair 6 item b'),
        ('Pair 7 item a', 'Pair 7 item b'),
        ('Pair 8 item a', 'Pair 8 item b'),
        ('Pair 9 item a', 'Pair 9 item b'),
        ('Pair 10 item a', 'Pair 10 item b'),
    )
    q = cf.DragAndDrop(pairs, None, 1, 2, 6)
    print('Trying')
    return q.returnAll()

def test_do():
    pairs = (
        ('Gaming PC RAM', '12GB RAM'),
        ('Gaming PC Graphics', 'Pair 2 item b'),
        ('Gaming PC Power Supply', 'Pair 3 item b'),
        ('Gaming PC Cooling', 'Pair 4 item b'),
        ('Gaming PC Peripherals', 'Pair 5 item b'),
        ('Virtualisation PC RAM', '24GB RAM'),
        ('Pair 7 item a', 'Pair 7 item b'),
        ('Pair 8 item a', 'Pair 8 item b'),
        ('Pair 9 item a', 'Pair 9 item b'),
        ('Pair 10 item a', 'Pair 10 item b'),
    )
    q = cf.DragAndDrop(pairs, None, 1, 10, 10)
    print('Trying')
    return q.returnAll()

#a laptop hardware

def aa_aa_laptop_keyboards():

    correct = (
        "may have keys which are closer together", 
        "may have fewer keys", 
        "may not have a numeric key pad", 
        "may have smaller buttons for less commonly used keys", 
        "may be missing some keys",
        "may be missing PAGE UP or PAGE DOWN keys", 
        "will have all alphabet keys in similar positions", 
    )
    incorrect = (
        "may have keys which are further apart", 
        "may have more keys", 
        "may have a numeric key pad", 
        "may have the same button sizes for all keys", 
        "will have the same keys",
        "may be missing a CAPSLOCK key", 
        "may be missing an ESCAPE key key", 
        "may be missing an ESCAPE key key", 
        "may be missing a SPACE bar", 
        "may not be back-lit", 
        "may require you to use the SHIFT key to access some numbers",
        "may require you to use the SHIFT key to access some less common letters",
    )
    number = randint(1,4)
    if randint(0,1) == 1:
        q = cf.SelectMcDrag(None, correct, incorrect, None, (), 1, number, randint(5,6))
        q.questionBase = f"Choose the all correct statements about laptop keyboards:"
    else:
        q = cf.SelectMcDrag(None, incorrect, correct, None, (), 1, number, randint(5,6))
        q.questionBase = f"Choose the all incorrect statements about laptop keyboards:"
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), cf.currentFuncName(), module_path(),"aa") 
    return q.returnAll()

def aa_ab_laptop_storage():
    
    correct = (
        "desktops tend to use 3.5 inch hard drives", 
        "laptops tend to use 2.5 inch hard drives", 
        "2.5 inch SSD drives tend to be compatible with laptops",
        "SSD drives are silent"
        "SSD drives are faster than hard drives", 
        "SSD drives have less latency than hard drives",
        "SSD drives have no large moving parts", 
        "SSHD drives are a combination of hard drive and SSD",
        "SSHD drives allow data to be writen to the HD to be cached by the SSD", 
        "hard drives tend to provide more capacity for less cost than SSDs"
        "SSD stands for solid state drive", 
        "SSHD stands for solid state hybrid drive",
    )
    incorrect = (
        "desktops tend to use 2.5 inch hard drives", 
        "laptops tend to use 3.5 inch hard drives", 
        "3.5 inch SSD drives tend to be compatible with laptops",
        "hard drives are silent"
        "hard drives are faster than SSD", 
        "SSD drives have more latency than hard drives",
        "Hard drives have no moving parts", 
        "SSHD drives are a combination of two hard drives",
        "SSHD drives are a combination of two SSDs",
        "SSHD drives allow data to be writen to the SSD to be cached by the hard drive", 
        "SSDs tend to provide more capacity for less cost than Hard drives"
        "SSD stands for secure state drive", 
        "SSHD stands for secure state hybrid drive",
        "SSD stands for silent state drive", 
        "SSHD stands for silent state hybrid drive",
    )
    number = randint(1,4)
    if randint(0,1) == 1:
        q = cf.SelectMcDrag(None, correct, incorrect, None, (), 1, number, randint(5,6))
        q.questionBase = f"Choose the all correct statements about laptop storage:"
    else:
        q = cf.SelectMcDrag(None, incorrect, correct, None, (), 1, number, randint(5,6))
        q.questionBase = f"Choose the all incorrect statements about laptop storage:"
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), cf.currentFuncName(), module_path(),"aa") 
    return q.returnAll()

def aa_ac_laptop_RAM():
    correct = (
        "SODIMM stands for small outline dual inline memory module", 
        "Micro DIMM stands for Micro dual inline memory module", 
        "laptop RAM is generally a different size to desktop RAM",
        "there are often a limited number of slots for RAM in a laptop",
    )
    incorrect = (
        "SODIMM stands for silent outline dual inline memory module", 
        "SODIMM stands for small outline dual inline micro module", 
        "SODIMM stands for small outline dual inline micro memory", 
        "Micro DIMM stands for Micro differentiated inline memory module",
        "Micro DIMM stands for Micro direct inline memory module",
        "laptop RAM is generally compatible with desktop RAM",
        "laptop RAM and desktop RAM are interchangable",
        "it is often possible to upgrade the number of slots available for laptop RAM",
        "most laptop RAM can be inserted bi-directionally",
        "laptop RAM sticks are proprietory to each brand of laptop", 
    )
    number = randint(1,3)
    if randint(0,1) == 1:
        q = cf.SelectMcDrag(None, correct, incorrect, None, (), 1, number, randint(4,5))
        q.questionBase = f"Choose the all correct statements about laptop wireless network cards:"
    else:
        q = cf.SelectMcDrag(None, incorrect, correct, None, (), 1, number, randint(4,5))
        q.questionBase = f"Choose the all incorrect statements about laptop wireless network cards:"
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), cf.currentFuncName(), module_path(),"aa") 
    return q.returnAll()

'''
def aa_ad_general_laptophardware
    correct = (
        "Optical drives are becoming less common in laptops", 
        "DVDs and CD are being replaced by other media", 
    )
'''


def aa_ae_laptop_upgrades():
    items = (
        ("8GB RAM and 500GB HDD. Spare slots exist for RAM and storage. They are concerned that their laptop takes a long time to boot up, but have a limited budget.", "Add an SSD, and make this the bootable drive"),
        ("2GB RAM and 256GB SSD. Spare slots exist for RAM and storage. They are concerned that their laptop slows down when multitasking, but have a limited budget.", "Add a 4GB stick of RAM"),        
        ("8GB RAM and 128GB SSD. Spare slots exist for RAM and storage. They need much more storage space on their laptop, but have a limited budget.", "Add a 1TB 2.5 inch hard drive"),
        ("16GB RAM and 526GB SSD. Spare slots exist for RAM and storage. They have a GPU built into the motherboard. They want to upgrade their graphics processing ability and have a large budget","It is unlikely that they will be able to upgrade. They should consider buying a new laptop with the specs they want" )
    )
    fillers = (
        "Upgrade the video card",
        "Upgrade the motherboard",
        "Upgrade the battery",
        "Add a 1TB 3.5 inch hard drive",
        "Replace the hard drive with a hard drive from another laptop",
        "Replace the old RAM with newer RAM", 
        "Recommend turning off the WIFI",
        "Recommend buying a new laptop", 
        "Replace the 2.5 inch drive with a larger 3.5 inch drive", 
        "Replace the old battery", 
        "Add a GPU in the RAM slot", 
        "Add a GPU in the storage slot", 
        "Upgrade the existing GPU", 
    )
            
    if randint(0,1) == 0:
        q = cf.SelectMcDrag(None, None, None, items, fillers, 1, 1, randint(4,5))
        q.questionBase = f"{q.item(vl.names)}, a {q.item(vl.technitians)} {q.item(vl.users)}, has a laptop with {items[q.choice][0]} How should you advise them to proceed?"
    else:
        q = cf.SelectMcDrag('drag', None, None, items, fillers, 1, 2, randint(4,5))
        q.questionBase = f"The following are descriptions of existing laptop specs and user requirements. Match them with appropriate solutions:"
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), cf.currentFuncName(), module_path(),"aa")
    return q.returnAll()

def aa_af_laptop_security():
    items = (
        ("purchase new laptops which will be secure without the need to continuously log in to their machines", "built in security card readers"),
        ("provide existing business laptops with security without the need to continuously log in to their machines", "external security card readers"),
        ("purchase new laptops which will be easy to secure against theft from workstations", "ensure new laptops have slots for physical laptop locks"),
        ("provide existing business laptops with security against theft from workstations", "purchase physical laptop locks"),
    )
    fillers = (
        "remove login functionality", 
        "remove the need to enter a password", 
        "install security cameras",
        )
    if randint(0,1) ==0:
        q = cf.SelectMcDrag(None, None, None, items, fillers, 1, 1, randint(4,5))
        q.questionBase = f"{q.item(vl.names)}, a {q.item(vl.technitians)} {q.item(vl.users)}, wants to {items[q.choice][0]}. How should you advise them to proceed?"
    else:
        q = cf.SelectMcDrag('drag', None, None, items, fillers, 1, 1, randint(4,5))
        q.questionBase = f"Match the following requirements with the appropriate solution if a business owner wishes to:"
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), cf.currentFuncName(), module_path(),"aa")
    return q.returnAll()
def aa_ag_wifi_cards():
    correct = (
        "laptops have seperate slots for different wifi cards", 
        "laptops have a unique slot for 802.11 wireless cards", 
        "laptops have a unique slot for WAN (cellular network) wireless cards", 
        "laptops have a unique slot for PAN (Bluetooth) wireless cards",
        "wireless cards in laptops can be replaced", 
        "a wireless card is likely to have an antenna which needs to be attached", 
        "the antenna for a wireless card is likely to end near the top of the laptop screen",
        "mini PCI is larger than mini PCI express."
        "mini PCI express cards are smaller than mini PCI cards."
    )
    incorrect = (
        "all wireless functionality on a laptop is controlled by the same card", 
        "wireless cards have built in antennas", 
        "wireless cards are hard wired into the laptop's motherboard and cannot be replaced", 
        "wireless cards are built into the shell of the laptop and cannot be replaced", 
        "wireless cards a proprietory to each laptop",
        "wireless functionality in a laptop is controlled by the graphics card", 
        "mini PCI is smaller than mini PCI express",
        "mini PCI express cards are larger than mini PCI cards",
        "the antenna for a wireless card is likely to end near the base of the laptop screen",
        "the antenna for a wireless card is likely to end near the hinge of the laptop screen",
        "the antenna for a wireless card is likely to end near the power socket",
    )
    number = randint(1,4)
    if randint(0,1) == 1:
        q = cf.SelectMcDrag(None, correct, incorrect, None, (), 1, number, randint(5,6))
        q.questionBase = f"Choose the all correct statements about laptop wireless network cards:"
    else:
        q = cf.SelectMcDrag(None, incorrect, correct, None, (), 1, number, randint(5,6))
        q.questionBase = f"Choose the all incorrect statements about laptop wireless network cards:"
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), cf.currentFuncName(), module_path(),"aa") 
    return q.returnAll()

def aa_ag_motherboard_and_video_card():
    correct = (
        "in most laptops, the video card is built in or not upgradable", 
        "in many laptops, there is a video card build into the motherboard", 
        "in most laptops, the motherboard is proprietary", 
        "in many laptops, most of the computational components are on the motherboard", 
        "in some laptops, there may be a discrete graphics card", 
        "in most laptops, there is an integrated memory crontroller", 
        "in most laptops, the video controller is not upgradable", 
        "in most laptops, processors are slower than desktops due to heat management issues",
        "in most laptops, heat management is an issue because of confined space",  
    )
    incorrect = (
        "in most laptops, the video card can be upgraded as easilly as RAM", 
        "in most laptops, the video card can be upgraded as easilly as storage", 
        "in many laptops, there is discrete graphics card", 
        "in most laptops, all components are upgradable", 
        "in many laptops, many of the components which could be upgraded on a desktop can also be upgraded", 
        "in most laptops, heat management is easier because the components are smaller"
        "in many laptops, most of the computational components are seperate form the motherboard", 
        "in most laptops, processors are faster than desktops due to smaller size",
        "in many laptops, larger fans mean easier heat management than desktops", 
        "in most laptops, heat management is less of an issue because there is less air circulation",  
    )
    number = randint(1,4)
    if randint(0,1) == 1:
        q = cf.SelectMcDrag(None, correct, incorrect, None, (), 1, number, randint(4,6))
        q.questionBase = f"Choose the all correct statements about laptop hardware:"
    else:
        q = cf.SelectMcDrag(None, incorrect, correct, None, (), 1, number, randint(4,6))
        q.questionBase = f"Choose the all incorrect statements about laptop hardware:"
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), cf.currentFuncName(), module_path(),"aa") 
    return q.returnAll()

def aa_ah_laptop_power():
    correct = (
        "in laptops, AC to DC power conversion is done on an external power brick",
        "in desktops, AC to DC power conversion is done on an internal power supply",
        "laptop power supplies convert AC to 110 volts or 220 DC input",
        "the DC jack on the laptop is specific to the laptop's power supply",
        "different laptop power leads may not be interchangable",
        "you can often get information about your power supply from the adapter",
        "most laptops use a rechargable Li-Ion battery",
        "Li-Ion batteries have no memory effect",
        "Li-Ion batteries do not have to be fully charged and discharged",
        "charging diminishes the capacity of Li-Ion batteries",
        "battery form factor differs for each laptop",
    )
    incorrect = (
        "in laptops, AC to DC power conversion is done on an internal power supply",
        "in desktops, AC to DC power conversion is done on an external power brick",
        "laptop power supplies convert DC to 110 volts or 220 AC input",
        "the DC jack on each laptop is usally interchangable",
        "different laptop power leads are usually interchangable",
        "most laptops use a rechargable NiCad battery",
        "most laptops use a rechargable NiCam battery",
        "most laptops use a rechargable NiMn battery",
        "Li-Ion batteries experience memory effect",
        "Li-Ion batteries have to be fully charged and discharged",
        "memory effect diminishes the capacity of Li-Ion batteries",
        "batteries are interchangable between laptops",
        "charging maintains the capacity of Li-Ion batteries",
    )
    number = randint(1,4)
    if randint(0,1) == 1:
        q = cf.SelectMcDrag(None, correct, incorrect, None, (), 1, number, randint(4,6))
        q.questionBase = f"Choose the all correct statements about powering laptops:"
    else:
        q = cf.SelectMcDrag(None, incorrect, correct, None, (), 1, number, randint(4,6))
        q.questionBase = f"Choose the all incorrect statements about powering laptops:"
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), cf.currentFuncName(), module_path(),"aa") 
    return q.returnAll()

def aa_ai_Power_lead_troubleshooting():
    items = (
        ("has lost their laptop power lead", "take details of the make and model of their laptop to order a new power lead"),
        ("is complaining that their laptop, several years old but otherwise functional, has a short battery life", "take details of the make and model of their laptop to order a new battery"),
        ("has damaged their power lead, and it no longer fits their laptop", "inspect the power lead to see if it can be repaired or needs to be replaced"),
        ("is unable to charge their laptop. No charging light comes on when the lead is plugged in, and the jack seems loose", "remove the screws from the back of the laptop to check that the jack is correctly seated"),
    )
    fillers = (
        "allow them to try your power lead", 
        "allow them to try your battery",
        "tell them to find another user with a laptop of the same brand and borrow their power lead",
        "tell them to find another user with a laptop of the same brand and borrow their battery",
        "backup their hard drive and order an SSD drive",
        "order them a new device",
    )
    if randint(0,1) ==0:
        q = cf.SelectMcDrag(None, None, None, items, fillers, 1, 1, randint(4,5))
        q.questionBase = f"{q.item(vl.names)}, a {q.item(vl.technitians)} {q.item(vl.users)}, {items[q.choice][0]}.How should you help them?"
    else:
        q = cf.SelectMcDrag('drag', None, None, items, fillers, 1, 1, randint(4,5))
        q.questionBase = f"Match the following fault symptoms with the appropriate solutions if a user has:"
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), cf.currentFuncName(), module_path(),"aa")
    return q.returnAll()

def aa_aj_laptop_frames():
    correct = (        
        "plastic frames are lightweight",
        "plastic frames are less durable than metal",
        "plastic frames are inexpensive",
        "metal frames are heavier",
        "metal frames are more durable than plastic",
        "metal frames are more expensive than plastic",
        "metal frames can be more difficult to repair",
    )
    
    incorrect = (        
        "plastic frames are heavier",
        "plastic frames are more durable than metal",
        "plastic frames are expensive",
        "metal frames are lighter",
        "metal frames are less durable than plastic",
        "metal frames are less expensive than plastic",
        "metal frames can be easier to repair",
    )
    if randint(0,1) == 1:
        q = cf.SelectMcDrag(None, correct, incorrect, None, (), 1, 2, randint(4,6))
        q.questionBase = f"Choose the two correct statements about laptop frames:"
    else:
        q = cf.SelectMcDrag(None, incorrect, correct, None, (), 1, 2, randint(4,6))
        q.questionBase = f"Choose the two incorrect statements about laptop frames:"
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), cf.currentFuncName(), module_path(),"aa") 
    return q.returnAll()


#b laptop screens
def aa_ba_Laptop_screen_repair():
    items = (
        ("black even when the device is powered on. The laptop has an LCD screen lit by a cold cathode flourescent lamp. When you examine the screen, you see that data is visible on the screen when examined with a bright light.","It may be possible to replace the CCFL backlight to repair the screen"),
        ("black even when the device is powered on. The laptop has an LCD screen lit by light emmiting diodes. When you examine the screen, you see that data is visible on the screen when examined with a bright light.","The the backighting is faulty, it may be difficult just to replace the backlight, but you should investigate further"),
        ("normal apart from faint outlines resembling they layout of a website they often use, which are permanently on the screen. The laptop has an OLED display.","The screen has degraded and you may be able to replace it"),
    )
    fillers = (
        "You can fix the individual leds in their screen which are causing the fault",
        "The need to replace their entire device",
        "The video card is faulty and that you many be able to replace it",
        "There is not enough power getting to the screen and you will need to replace the battery"
    )
    if randint(0,1) ==0:
        q = cf.SelectMcDrag(None, None, None, items, fillers, 1, 1, randint(4,5))
        q.questionBase = f"{q.item(vl.names)}, a {q.item(vl.technitians)} {q.item(vl.users)}, brings you, a technitian, their laptop for repair and shows you that {items[q.choice][0]}. The user insists that the screen should be repaired rather than replaced if possible. You should tell them?"
    else:
        q = cf.SelectMcDrag('drag', None, None, items, fillers, 2, 2, randint(4,5))
        q.questionBase = f"Match the following fault symptoms with the appropriate solutions if a laptop screen is:"
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), cf.currentFuncName(), module_path(),"aa")
    return q.returnAll()

def aa_bb_Laptop_screen_recommendation():
    items = (
        ('have low power consumption and be cheap', 'Laptop with an LCD screen backlit by LEDS.'),
        ('have the abilility to display true black pixels for the cheapest cost', 'Laptop with an passive matrix organic LED screen.'),
        ('have the ability to display true black pixels on a large screen at high resolution', 'Laptop with an active matrix organic LED screen.'),
    )
    fillers = (
        'Laptop with an LCD screen backlit by a cold cathod flourescent lamp',
        'Laptop with a screen which can be adjusted for brightness',
        'Laptop with a low power video card',
        'Laptop with a high powered video card',
        'Laptop with a screen resolution of at least 1080p'
    )
    if randint(0,1) ==0:
        q = cf.SelectMcDrag(
            None, None, None, items, fillers, 1, 1, randint(4,6)
            )
        q.questionBase = f"{q.item(vl.names)}, a {q.item(vl.technitians)} {q.item(vl.users)}, is interested in buying a new laptop, and is confused as to how the type of screen on the laptop should impact what they choose. They say the device they buy should {items[q.choice][0]}. What type of screen should you recommend?"
    else:
        q = cf.SelectMcDrag(
            'drag', None, None, items, fillers, 2, 2, randint(4,6)
            )
        q.questionBase = f"Match the following screen requirements with their solutions:"
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), cf.currentFuncName(), module_path(),"aa")
    return q.returnAll()

def aa_bc_LCD_screens():
    correct = (
        'LCD screens are lightweight',
        'LCD screen are cheap',
        'LCD screens struggle to display black well',
        'LCD screens are backlit by LEDs or CCFL',
        'The LEDs in an LCD screen use DC power',
        'The CCFL in an LCD screen uses AC power',
        'The LEDs in an LCD screen do not require an inverter', 
        'The CCFL in an LCD screen requires an inverter',
        'A CCFL in an LCD screen requires higher power than LEDs',
        'CCFL LCD screens are less common now',
        'CCFL LCD screens tend to be older',
    )
    incorrect = (
        'LCD screens are heavy',
        'LCD screen are expensive',
        'LCD screens display black well',
        'LCD screens are not backlit',
        'The LEDs in an LCD screen use AC power',
        'The CCFL in an LCD screen uses DC power',
        'The LEDs in an LCD screen require an inverter', 
        'The CCFL in an LCD screen does not require an inverter',
        'A CCFL in an LCD screen requires lower power than LEDs',
        'CCFL LCD screens are more common now',
        'CCFL LCD screens tend to be newer',
    )
    if randint(0,1):
        q = cf.SelectMcDrag(None, correct, incorrect, None, (), 1, 2, randint(5,8))
        q.questionBase = f"Choose the two correct statements:"
    else:
        q = cf.SelectMcDrag(None, incorrect, correct, None, (), 1, 2, randint(5,8))
        q.questionBase = f"Choose the two incorrect statements:"
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), cf.currentFuncName(), module_path(),"aa")
    return q.returnAll()

def aa_bd_LCD_vs_OLED():
    correct = (
        'LCD screen are less expensive than OLED',
        'OLED screens are more expensive than LCD',
        'OLED screens display black better than LCD',
        'LCD screens use less power than OLED',
        'OLED screen use more power than LCD',
    )
    incorrect = (
        'LCD screen are more expensive than OLED',
        'OLED screens are less expensive than LCD',
        'LCD screens display black better than OLED',
        'OLED screens use less power than LCD',
        'LCD screen use more power than OLED',
    )
    if randint(0,1):
        q = cf.SelectMcDrag(None, correct, incorrect, None, (), 1, 2, randint(4,5))
        q.questionBase = f"Choose the two correct statements:"
    else:
        q = cf.SelectMcDrag(None, incorrect, correct, None, (), 1, 2, randint(4,5))
        q.questionBase = f"Choose the two incorrect statements:"
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), cf.currentFuncName(), module_path(),"aa")
    return q.returnAll()


def aa_be_Around_a_screen():
    correct = (
        'Camera',
        'Microphone',
        'Bluetooth antenae',
        'Wifi antenae',
    )
    incorrect = (
        'Graphics card',
        'RAM',
        'Battery',
        'Power lead',
    )

    if randint(0,1):
        q = cf.SelectMcDrag(None, correct, incorrect, None, (), 1, 2, randint(4,5))
        q.questionBase = f"Which two of these would you expect to find in a laptop's lid?"
    else:
        q = cf.SelectMcDrag(None, incorrect, correct, None, (), 1, 2, randint(4,5))
        q.questionBase = f"Which two of the following would you not expect to find in a laptop's lid?"
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), cf.currentFuncName(), module_path(),"aa")
    return q.returnAll()

def aa_ca_Laptop_features():
    correct = (
        'The microphone in a laptop is often inadequate for professional use',
        'Professional audio capture on a laptop will probably require an aftermarket microphone',
        'Laptop wifi antennae often wrap around the laptop screen',
        'Laptop bluetooth antennae often wrap around the laptop screen',
        'Hybrid laptops have detatchable keyboards and touchscreen',
        'Some laptops may have touchscreen interfaces',
        'Some laptops may allow the use of stylus for graphical interface',
    )
    incorrect = (
        'The microphone in a laptop is often as good as a good USB microphone',
        'Professional audio capture on a laptop seldom requires an aftermarket microphone',
        'Laptop wifi antennae often wrap around the laptop keyboard',
        'Laptop bluetooth antennae often wrap around the laptop keyboard',
        'A device with a touchscreen interface is not a laptop',
        'Stylus for graphical work are now outdated',
    )
    if randint(0,1):
        q = cf.SelectMcDrag(None, correct, incorrect, None, (), 1, 2, randint(4,5))
        q.questionBase = f"Choose the two correct statements:"
    else:
        q = cf.SelectMcDrag(None, incorrect, correct, None, (), 1, 2, randint(4,5))
        q.questionBase = f"Choose the two incorrect statements:"
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), cf.currentFuncName(), module_path(),"aa") 
    return q.returnAll()
#b laptop screens
#c laptop features
def aa_cb_function_keys():
    correct = (
        "may adjust screen brightness",
        "can toggle key backlight on or off",
        "can toggle wifi on or off",
        "can provide convenient media keys (e.g. pause, fast forward etc)",
        "can adjust noise volume",
        "can be used to switch between project, dual screens and laptop screen modes",
        "can turn a laptop's touchpad on or off",
        "can adjust screen orientation",
    )
    incorrect = (
        "can adjust screen size",
        "can prevent your laptop from becoming stolen",
        "must all be programmed",
        "cannot adjust a laptop's keyboard backlight thic can be adjusted through the BIOS",
        "cannot turn off touchpads, which can only be turned off in the BIOS",
        "can provide security in the event of theft",
        "may protect your data",
        "can improve laptop performance",
    )
    if randint(0,1):
        q = cf.SelectMcDrag(None, correct, incorrect, None, (), 1, 2, randint(5,7))
        q.questionBase = f"Choose the two correct statements. Laptop function keys:"
    else:
        q = cf.SelectMcDrag(None, incorrect, correct, None, (), 1, 2, randint(4,5))
        q.questionBase = f"Choose the two incorrect statements. function keys:"
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), cf.currentFuncName(), module_path(),"aa") 
    return q.returnAll()


def aa_cc_laptop_features():
    items = (
        ("a device to use to give presentations where an external projector or screen is not present", "rotating screen"),
        ("a device to use as a laptop, whilst also being able to draw freehand", "laptop with removable screen"),
        ("to leave a laptop in a location whilst preventing theft", "laptop lock"),
        ("the cheapest option to use a printer, another screen a mouse and a full keybaord at work desk without having to mess with wires", "port replicator"),
        ("to combine power supply, connections to peripherals, extra slots for memory cards, keyboard and mouse with their laptop at their desk", "docking station"),
        ("to change quickly between projecting to a second screen and the laptop's screen", "function keys"),
        ("to be able to quickly mute the laptop", " mute hotkey"),
        ("to be able to quickly start, stop and cycle through media", " media hotkeys"),
        ("to save power whilst away from a socket", " turn off keyboard backlighting and turn down screen backlight"),
        ("to keep laptop screen projection running whilst device is closed", " adjust settings in the BIOS or utility"),
    )
    fillers = (
        "buy a laptop with an OLED display",
        "use a screen splitter cable",
        "install an internal modem",
        "upgrade the wireless card",
        "update appropriate drivers",
        "purchase a desktop", 
        "use a password",
    )
    q = cf.SelectMcDrag(None, None, None, items, fillers, 1, 1, randint(4,7))
    q.questionBase = f"{q.item(vl.names)}, a {q.item(vl.technitians)} {q.item(vl.users)}, comes to you for advice. They need {items[q.choice][0]}. What should you tell them?"
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), cf.currentFuncName(), module_path(),"aa")
    return q.returnAll()


def aa_cd_laptop_locks():
    correct = (
        'connect to metal reinforced slots on the laptop',
        'must also be connected to a solid object',
        'cannot prevent the laptop from being opened',
        'can prevent your laptop from being taken from a location',
        'are a mechanical security device',
    )
    incorrect = (
        'prevent identity theft',
        'make your password invisible',
        'can prevent your laptop from being used by an anauthorised user',
        'are an electronic security device',
        'prevent the laptop from being opened',
        'can prevent your laptop from being accessed through the BIOS',
    )

    if randint(0,1):
        q = cf.SelectMcDrag(None, correct, incorrect, None, (), 1, 1, randint(4,6))
        q.questionBase = f"Choose the correct statement. Physical laptop locks:"
    else:
        q = cf.SelectMcDrag(None, incorrect, correct, None, (), 1, 1, randint(4,6))
        q.questionBase = f"Choose the incorrect statement. Physical laptop locks:"
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), cf.currentFuncName(), module_path(),"aa") 
    return q.returnAll()


def aa_ce_docking_stations_and_port_replicators():
    correct = (
        'docking stations provide a power supply',
        'port replicators do not provide a power supply',
        'docking stations extend laptop functionality',
        'port replicators allow you to connect peripherals through a usb or special port on your laptop',
        'desktop adapter cards in docking stations can give laptops desktop functionality',
        'port replicators allow use of peripherals without having to plug them each into the laptop every time',
        'docking stations allow use of peripherals without having to plug them each into the laptop every time',
        'port replicators extend existing laptop interfaces',
        'docking stations extend existing laptop interfaces',
        'docking stations do more than extending existing laptop interfaces'
    )
    incorrect = (
        'port replicators provide a power supply',
        'docking stations do not provide a power supply',
        'a usb keyboard extends laptop functionality',
        'docking stations allow you to connect peripherals through a usb or special port on your laptop',
        'desktop adapter cards in port replicators can give laptops desktop functionality',
        'port replicators allow desktop functionaliry on your laptop',
        'docking stations have to be plugged into a USB port',
        'port replicators do more than exending existing laptop interfaces',
        'port replicators allow duplicate http ports',
        'port replicators allow access to multiple docker instances',
    )
    number = randint(1,3)
    if randint(0,1):
        q = cf.SelectMcDrag(None, correct, incorrect, None, (), number, number, randint(6,8))
        q.questionBase = f"Choose all correct statements:"
    else:
        q = cf.SelectMcDrag(None, incorrect, correct, None, (), number, number, randint(6,8))
        q.questionBase = f"Choose all incorrect statements:"
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), cf.currentFuncName(), module_path(),"aa") 
    return q.returnAll()

def aa_cf_Laptop_security():
    items = (
        ("the ability to charge their devices, access corporate LAN resources, and allow for a variety of other removable hardware.","Docking station"),
        ("the ability to leave their desks without having to worry about their device being stolen","physical laptop lock"),
    )
    fillers = ("Port replicator", "Thunderbolt", "USB hub", "Lightning", "wireless hub",)
    q = cf.SelectMcDrag(None, None, None ,items,fillers, 1, 1, randint(4, 5))
    q.questionBase = f"A {q.item(vl.businesses)} business owner wants to provide security to laptop users with {items[q.choice][0]}. Which of the following devices would BEST meet the owner’s needs?"    
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), cf.currentFuncName(), module_path(),"aa")
    return q.returnAll()


#b laptop screens
#c laptop features
#d types of devices
def aa_da_Mobile_device_choice():
    items = (
        ('casually watch films, send emails and instant messages whilst travelling', 'mobile phone'),
        ('make video calls, notes and technical sketches', 'tablet'),
        ('read books whilst on holiday', 'ereader'),
        ('play immersive games at home', 'vr headset'),
        ('view future building plans superimposed onto existing sites', 'augmented reality device'),
        ('monitor their heart rate throughout the day', 'fitness monitor'),
        ('send and recieve messages from the office in as small a form factor as possible', 'smart watch'),
        ('navigate between locations on foot or driving', 'satnav'),
        ("have internet access in locations without access to ethernet or wifi", "portable hotspot"),
    )
    fillers = ('desktop computer', 'magnetic card reader', 'color inkjet printer')
    if randint(0,1) == 0:
        q = cf.SelectMcDrag('multi', None, None, items,fillers,1,1,6)
        q.questionBase = f"A {q.item(vl.users)} is seeking advice on which device to purchase for a friend who wants to {q.item(vl.businesses)} business owner. The friend needs the ability to {items[q.choice][0]}. Which of the following would be the BEST recommendation?"
    else:
        q = cf.SelectMcDrag('drag', None, None, items,fillers,1,4,randint(5,7))
        q.questionBase = f"Match the following use cases with the device that best meets their needs at the lowest cost:"

    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), cf.currentFuncName(), module_path(),"aa")
    return q.returnAll()

def aa_db_Tablet_features():
    correct = (
        'touch screen',
        'screen larger than 7 inches diagonal',
        'capable of playing media',
        'bluetooth enabled',
        'wifi enabled',
        'may be able to access cellular networks',
        'LED or OLED screen',
        'used for mobile communication',
    )
    incorrect = (
        'very low power consumptopn',
        'wearable',
        'commonly monochromatic screen',
        'used to monitor heartbeat',
        'used to monitor steps taken during the day',
        'requires view of the sky to function',
    )
    number = randint(1,3)
    if randint(0,1):
        q = cf.SelectMcDrag(None, correct, incorrect, None, (), 1, number, randint(5,7))
        q.questionBase = f"Choose all correct statements about tablets:"
    else:
        q = cf.SelectMcDrag(None, incorrect, correct, None, (), 1, number, randint(5,7))
        q.questionBase = f"Choose all incorrect statements about tablets:"
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), cf.currentFuncName(), module_path(),"aa") 
    return q.returnAll()

def aa_dc_Ereader_features():
    correct=(
        'very low power consumption',
        'wifi connectivity',
        'cellular network connectivity',
        'commonly monochromatic screen',
        'suitable for use in direct light',
        'specialised mobile device',
    )

    incorrect=(
        'commonly OLED screen',
        'suitable for playing films',
        'used to monitor heartbeat',
        'requires view of the sky to function',
        'wearable',
        'used for augmented reality',
        'used for virtual reality',
        'used for mobile communication',
    )
    number = randint(1,3)
    if randint(0,1):
        q = cf.SelectMcDrag(None, correct, incorrect, None, (), 1, number, randint(5,7))
        q.questionBase = f"Choose all correct statements about Ereaders:"
    else:
        q = cf.SelectMcDrag(None, incorrect, correct, None, (), 1, number, randint(5,7))
        q.questionBase = f"Choose all incorrect statements about Ereaders:"
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), cf.currentFuncName(), module_path(),"aa") 
    return q.returnAll()

def aa_dd_GPS_features():
    correct = (        
        'requires view of the sky',
        'specialised mobile device',
        'requires regular updates',
    )
    incorrect = (
        'used for augmented reality',
        'used for virtual reality',
        'extension of phone and body',
        'used for mobile communication',
    )
    number = 2
    if randint(0,1):
        q = cf.SelectMcDrag(None, correct, incorrect, None, (), 1, number, randint(4,5))
        q.questionBase = f"Choose all correct statements about GPS devices:"
    else:
        q = cf.SelectMcDrag(None, incorrect, correct, None, (), 1, number, randint(4,5))
        q.questionBase = f"Choose all incorrect statements about GPS devices:"
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), cf.currentFuncName(), module_path(),"aa") 
    return q.returnAll()

def aa_de_Mobile_device_specs():
    items = (
        ('screen larger than 7 inches diagonal', 'tablet'),
        ('searable device capable of playing media', 'smart watch'),
        ('device with a monochromatic screen with very low power consumption', 'ereader'),
        ('requires a view of the sky and periodic updates', 'gps'),
        ('wearable device capable of superimposing images or data onto your surroundings', 'augmented reality mobile device'),
        ('screen between 3.6 to 6 inches diagonal with cellular connectivity', 'mobile communication device'),
        ('a device which only performs one or two tasks', 'specialised mobile device'),
        ('a device where inputs from the real world allow you to interact with a virtual world', 'virtual reality device'),
    )
    if randint(0,1) == 0:
        q = cf.SelectMcDrag('multi', None, None, items,[],1,1,6)
        q.questionBase = f"Which mobile device best fits the following description: {items[q.choice][0]}"
    else:
        q = cf.SelectMcDrag('drag', None, None, items,[],1,randint(1,4),randint(5,7))
        q.questionBase = f"Match the following use cases with the device that best meets their needs at the lowest cost:"

    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), cf.currentFuncName(), module_path(),"aa")
    return q.returnAll()


#b laptop screens
#c laptop features
#d types of devices
#e connectors

def aa_ea_USB_connector_descriptions():
    items = (
        ("a non-directional connector","USB-C"),
        ("an almost square-shaped connector","USB-B"),
        ("a rectangular shaped connector, sized 16 x 8mm","USB-A"),
        ("the slimest, non-directional connector", "lightning"),
    )
    fillers = ("Micro-USB", "Mini-USB")
    if randint(0,1) ==0:
        q = cf.SelectMcDrag(None, None, None, items, fillers, 1, 1, randint(4,5))
        q.questionBase = f"Which of the following charging and data ports has {items[q.choice][0]}?"
    else:
        q = cf.SelectMcDrag('drag', None, None, items, fillers,1, randint(1,3), 5)
        q.questionBase = "Match the descriptions of different types of USB connectors with their names."
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), cf.currentFuncName(), module_path(),"aa")
    return q.returnAll()

def aa_eb_USB_connector_sizes():
    items = (
        ('a 24-pin USB connector system with a rotationally symmetrical connector', 'USB-C'),
        ('a 6.85 by 1.8 mm connector intended for use with mobile devices', 'Micro USB-B'),
        ('a 3 by 7 mm connector intended for use with small devices', 'Mini USB-B'),
        ('16 by 8 mm with an elongated rectangular cross-section, carries both power and data', 'USB-A'),
        ('11.5 by 10.5 mm with a near square cross-section with the top exterior corners beveled, ', 'USB-B'),
        ('an 8-pin connector system with rotational symmetry', 'lightning'),
    )
    if randint(0,1) ==0:
        q = cf.SelectMcDrag(
                None, None, None, items, (), 1, 1, randint(4,5)
                )
        q.questionBase = f"Which of the following is {items[q.choice][0]}?"
    else:
        q = cf.SelectMcDrag(
                'drag', None, None, items, (),1, randint(3,5), 5
                )
        q.questionBase = "Match the descriptions of different types of USB connectors with their names."
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), cf.currentFuncName(), module_path(),"aa")
    return q.returnAll()

def aa_ec_Lightning_connectors():
    correct = (
        'have no top or bottom',
        'can be used on all modern apple devices',
        'can be used in iphones',
        'can be used in ipads',
        'can be used in ipods',
        'supply power faster than micro usb',
        'supply power and transfer data',
        'are flat',
        'have 8 pins',
        'supply more power than older 30 pin connectors',
        'are more durable than older 30 pin connectors',
    )
    incorrect=(
        'must be inserted the correct way round',
        'come in 8 and 30 pin configurations',
        'can only be used in iphones',
        'can only be used in ipads',
        'can only be used in ipods',
        'can be used in legacy 30 pin apple devices',
        'are compatible with most android devices',
        'are compatible with USB C connectors',
        'supply power more slowly than micro usb',
        'only supply power',
        'only supply data',
        'are the same shape as a usb',
        'have 30 pins',
        'is TRRS',
    )
    number = 2
    if randint(0,1):
        q = cf.SelectMcDrag(None, correct, incorrect, None, (), 1, number, randint(6,10))
        q.questionBase = f"Choose all correct statements about lightning connectors:"
    else:
        q = cf.SelectMcDrag(None, incorrect, correct, None, (), 1, number, randint(6,10))
        q.questionBase = f"Choose all incorrect statements about lightning connectors:"
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), cf.currentFuncName(), module_path(),"aa") 
    return q.returnAll()

def aa_ed_USB_C_connectors():        
    correct = (
        "can provide analog audio",
        "can provide power",
        "can provide data",
        "24 pins",
        "support USB 2.1",
        "support USB 3",
        "flatter than other USB connectors",
        "double sided",
        "have no top or bottom",
    )
    incorrect=(
        "can only provide power",
        "can only provide data",
        "cannot provide power",
        "cannot be used for analog audio",
        "18 pins",
        "30 pins",
        "8 pins",
        "thicker than other USB connectors",
        "unidirectional",
        "can only be inserted when correctly oriented",
        "are TRRS",
    )
    number = 2
    if randint(0,1):
        q = cf.SelectMcDrag(None, correct, incorrect, None, (), 1, number, randint(6,8))
        q.questionBase = f"Choose all correct statements about USB-C connectors:"
    else:
        q = cf.SelectMcDrag(None, incorrect, correct, None, (), 1, number, randint(6,8))
        q.questionBase = f"Choose all incorrect statements about USB-C connectors:"
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), cf.currentFuncName(), module_path(),"aa") 
    return q.returnAll()


#b laptop screens
#c laptop features
#d types of devices
#e connectors
#f connectivity
def aa_fa_Mobile_hotspots():
    correct = (
        "may incur additional charges and cost",
        "allow you to extend a cellular data network to all other devices",
        "can function as a personal wireless router",
        "some mobile devices can be configured as a wireless server",
        "other devices can connect via USB",
        "other devices can connect via PAN",
        "other devices can connect via Bluetooth",
        "require the mobile hotspot to have its own internet or data connection",
    )
    incorrect = (
        "allow you to extend a cellular data network to all other devices",
        "require an additional personal wireless router",
        "mobile devices cannot be configured as a wireless server",
        "other devices can connect via NFC",
        "other devices can connect via MAN",
        "require the device connected to the mobile hotspot to have its own internet or data connection",
    )
    number = randint(1,3)
    if randint(0,1):
        q = cf.SelectMcDrag(None, correct, incorrect, None, (), 1, number, randint(6,8))
        q.questionBase = f"Choose all correct statements about mobile hotspots:"
    else:
        q = cf.SelectMcDrag(None, incorrect, correct, None, (), 1, number, randint(6,8))
        q.questionBase = f"Choose all incorrect statements about mobile hotspots:"
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), cf.currentFuncName(), module_path(),"aa") 
    return q.returnAll()

def aa_fb_Personal_area_networks():
    correct = (
        'high speed communication',
        '10m range', 
        'used for tethering',
        'used in headsets and headphones',
        'used in health monitors',
        'used for connecting to external speakers',
        'Bluetooth',
    )
    incorrect = (
        'low speed communication',
        '1m range',
        '20m range',
        '10cm range',
        '100m range', 
        'used for phone payment systems',
        'used for contactless card payments',
        'used for in person information exchange',
    )
    number = randint(1,3)
    if randint(0,1):
        q = cf.SelectMcDrag(None, correct, incorrect, None, (), 1, number, randint(5,7))
        q.questionBase = f"Choose all correct descriptions of PAN in mobile devices:"
    else:
        q = cf.SelectMcDrag(None, incorrect, correct, None, (), 1, number, randint(5,7))
        q.questionBase = f"Choose all incorrect descriptions of PAN in mobile devices:"
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), cf.currentFuncName(), module_path(),"aa") 
    return q.returnAll()

def aa_fc_Near_field_communication():
    correct = (
        'for ending small amounts of data',
        'wireless',
        'limited range',
        'less than 10cm range',
        'used for phone payment systems',
        'used for contactless card payments',
        'used for in person information exchange',
        'has encryption support',
        'used in id cards',
    )
    correct = (
        'for ending large amounts of data',
        'IR',
        'requires internet connection',
        'less than 1m range',
        'less than 20m range',
        'less than 100m range', 
        'used for wireless headphones',
        'used for mobile hotspot tethering',
        'used for sharing images and media',
        'has no encryption support',
    )
    number = randint(1,3)
    if randint(0,1):
        q = cf.SelectMcDrag(None, correct, incorrect, None, (), 1, number, randint(5,8))
        q.questionBase = f"Choose all correct descriptions of NFC mobile devices:"
    else:
        q = cf.SelectMcDrag(None, incorrect, correct, None, (), 1, number, randint(5,8))
        q.questionBase = f"Choose all incorrect descriptions of NFC mobile devices:"
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), cf.currentFuncName(), module_path(),"aa") 
    return q.returnAll()

def aa_fd_IR_in_mobile_devices():
    correct = (
        "can be used to control other devices",
        "cannot be used for file transfers",
        "cannot be used for printing",
        "is included on many smartphones",
        "is included on many tablets",
        "is included on many smartwatches",
    )
    incorrect = (
        "cannot be used to control other devices",
        "can be used for file transfers",
        "can be used for printing",
        "is not included on smartphones",
        "is not included on tablets",
        "is not included on smartwatches",
    )
    number = randint(1,3)
    if randint(0,1):
        q = cf.SelectMcDrag(None, correct, incorrect, None, (), 1, number, randint(4,5))
        q.questionBase = f"Choose all correct statements about IR in mobile devices:"
    else:
        q = cf.SelectMcDrag(None, incorrect, correct, None, (), 1, number, randint(4,5))
        q.questionBase = f"Choose all incorrect statements about IR in mobile devices:"
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), cf.currentFuncName(), module_path(),"aa") 
    return q.returnAll()


def aa_fe_Mobile_wireless_connectivity():
    items = (
        ('Devices use haptic confirmation for sharing data wirelessly.', 'IR'),
        ('Devices are paired using a code for sharing data wirelessly.', 'Bluetooth'),
        ('Devices are placed in close proximity within line of sight for sharing data wirelessly', 'NFC'),
        ('Devices are connected via a wire for sharing data or connectivity', 'Tethering'),
        )
    fillers = ('Lightning', 'Digital Speech', 'Email', 'Microwaves', 'Ethernet', 'Hotspot', 'Cellular')
    q = cf.SelectMcDrag('drag', None, None, items, fillers, 1, randint(1,3), randint(3,6))
    q.questionBase = "Drag each mobile technology to the description of its use. Some answers will not be used."
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), cf.currentFuncName(), module_path(),"aa")
    return q.returnAll()

def aa_ff_Hotspot_troubles():
    correct = ("The connection is throttled",)
    incorrect = (
        "There is a low RFID signal", "SSID is not found", 
        "It is out of range", "IPconfig is invalid", 
        "Incorrect port",
        )
    q = cf.SelectMcDrag(
        None, correct, incorrect, None, [], 1, 1, randint(4, len(incorrect))
        )
    q.questionBase = f"A {q.item(vl.technitians)} technician has noticed that when at a {q.item(vl.businesses)} company headquarters the laptop connection to the Internet is more responsive than when using the company-provided phone as a hotspot. The technician updated the drivers on the WiFi NIC without resolution and then verified the configuration on the WiFi was correct. Which of the following configurations could cause the decreased performance?"
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), cf.currentFuncName(), module_path(),"aa")
    return q.returnAll()



#b laptop screens
#c laptop features
#d types of devices
#e connectors
#f connectivity
#g accessories
def aa_ga_Mobile_accesory_recommendations():
    items = (
        ("an apple user who wants to listen to audio privately", "headphones with a lightning connector"),
        ("an android user wanting to listen to audio without physically connecting anything","bluetooth headphones"),
        ("someone who wants to play stereo sound in their room", "gobile speaker"),
        ("a user who wants a console experience on their tablet", "game pad"),
        ("allow something to charge their and others' devices whilst away from home", "mobile battery pack"),
        ("avoid scratches on their devices' screen", "screen protector"),
        ("protect a phone when dropped","device protector"),
        ("enable a phone to be used to take card payments","credit card reader"),
        ("increase the storage capacity of a tablet", "micro-sd")
    )
    if randint(0,1) ==0:
        q = cf.SelectMcDrag(
                None, None, None, items, (), 1, 1, randint(4,5)
                )
        q.questionBase = f"What would you recommend to {items[q.choice][0]}?"
    else:
        q = cf.SelectMcDrag(
                'drag', None, None, items, (),1, randint(2,4), randint(5,7)
                )
        q.questionBase = "Match the folloring requirements with the apporpriate mobile accesory:"
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), cf.currentFuncName(), module_path(),"aa")
    return q.returnAll()

def aa_gb_Mobile_audio_accesories():
    correct = (
        "audio accessories may be hands free",
        "audio accessories may connect via a TRRS jack",
        "audio accessories may connect via USB-C",
        "audio accessories may connect via lighning",
        "audio accessories may connect via 3.5mm jack",
        "audio accessories may connect via bluetooth",
    )
    incorrect = (
        "audio accessories may connect via USB-A",
        "audio accessories may connect via PAN",
        "audio accessories may connect via LAN",
        "audio accessories may connect via WAN",
        "audio accessories may connect via 1/4 in jack",
        "audio accessories may connect via IR",
    )
    number = 2
    if randint(0,1):
        q = cf.SelectMcDrag(None, correct, incorrect, None, (), 1, number, randint(5,6))
        q.questionBase = f"Choose all correct statements about mobile audio accessories:"
    else:
        q = cf.SelectMcDrag(None, incorrect, correct, None, (), 1, number, randint(5,6))
        q.questionBase = f"Choose all incorrect statements about mobile audio accessories:"
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), cf.currentFuncName(), module_path(),"aa") 
    return q.returnAll()

def aa_gc_Screen_and_device_protectors():
    correct = (
        "screen protectors can be difficult to install correctly",
        "screen protectors are harder to install than device protectors",
        "device protectors are easier to install than screen protectors",
        "screen protectors may prevent scratches to the screen",
        "screen protectors do not provide shock absorbance for the device",
        "screen protectors do not provide waterproofing",
        "device protectors may provide waterproofing",
        "device protectors never provide shock absorbance",
        "device protectors may interfere with docking stations and interfaces",
        "screen protectors do not interfere with docking stations and interfaces",
    )
    incorrect = (
        "screen protectors are easy to install correctly",
        "screen protectors are easier to install than device protectors",
        "device protectors are harder to install than screen protectors",
        "device protectors may prevent scratches to the screen",
        "device protectors do not provide shock absorbance for the device",
        "device protectors never provide waterproofing",
        "screen protectors may provide waterproofing",
        "screen protectors never provide shock absorbance",
        "screen protectors may interfere with docking stations and interfaces",
        "device protectors do not interfere with docking stations and interfaces",
    )
    number = randint(2,5)
    if randint(0,1):
        q = cf.SelectMcDrag(None, correct, incorrect, None, (), 1, number, randint(6,8))
        q.questionBase = f"Choose all correct statements about screen and device protectors:"
    else:
        q = cf.SelectMcDrag(None, incorrect, correct, None, (), 1, number, randint(6,8))
        q.questionBase = f"Choose all incorrect statements about screen and device protectors:"
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), cf.currentFuncName(), module_path(),"aa") 
    return q.returnAll()


def aa_gd_Credit_card_readers():
    correct = (
        "can make a phone into a point of sale",
        "can make a tablet into a point of sale",
        "can connect via an audio TRRS jack",
        "can connect via lightning",
        "can connect via USB",
        "can connect via bluetooth",
        "can provide email reciepts",
        "can allow documents to be signed via touch",
        "can provide immediate feedback via internet link",
        "are ideal for small and mobile businesses"
    )
    incorrect = (
        "can make an ereader into a point of sale",
        "make a fitness monitor into a point of sale",
        "can connect via IR",
        "can connect via ethernet",
        "can connect via NFC",
        "can take cash payments",
        "can allow signed documents to be scanned",
        "can provide immediate credit feedback via internet link",
        "do not require internet connection",
        "require vision of the sky",
    )
    number = randint(1,4)
    if randint(0,1):
        q = cf.SelectMcDrag(None, correct, incorrect, None, (), 1, number, randint(6,8))
        q.questionBase = f"Choose all correct statements about credit card readers:"
    else:
        q = cf.SelectMcDrag(None, incorrect, correct, None, (), 1, number, randint(6,8))
        q.questionBase = f"Choose all incorrect statements about credit card readers:"
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), cf.currentFuncName(), module_path(),"aa") 
    return q.returnAll()

def aa_ge_SD_cards():
    correct = (
        "SD cards are larger than micro SD cards",
        "micro SD cards are smaller than SD cards",
        "micro SD cards are easy to loose if not in the device",
        "micro SD cards increase device storage",
        "SD cards increase device storage",
        "micro SD cards have SFF",
        "SD cards are commonly used in Windows devices",
        "SD cards are commonly used in Android devices",
        "SD cards are not commonly used in iOS devices",
    )

    incorrect = (
        "SD cards are smaller than micro SD cards",
        "micro SD cards are larger than SD cards",
        "all mobile devices accept SD cards",
        "micro SD cards increase device RAM",
        "micro SD cards increase device processor speed",
        "micro SD cards increase device resolution",
        "micro SD cards have NFC",
        "micro SD cards have TRRS",
        "SD cards are not commonly used in Windows devices",
        "SD cards are not commonly used in Android devices",
        "SD cards are commonly used in iOS devices",
    )
    number = randint(1,4)
    if randint(0,1):
        q = cf.SelectMcDrag(None, correct, incorrect, None, (), 1, number, randint(6,8))
        q.questionBase = f"Choose all correct statements about SD cards:"
    else:
        q = cf.SelectMcDrag(None, incorrect, correct, None, (), 1, number, randint(6,8))
        q.questionBase = f"Choose all incorrect statements about SD cards:"
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), cf.currentFuncName(), module_path(),"aa") 
    return q.returnAll()


#b laptop screens
#c laptop features
#d types of devices
#e connectors
#f connectivity
#g accessories
#h mobile hotspots
def aa_gf_Powering_mobile_devices():
    items = (
        ("They are concerned about wall outlet availability at the conferences and needs to continuously use the device for important updates whilst moving easilly between workshops.", "Wireless charging pad"),
        ("It is expected that wall outlets will be readilly available.", "An extra charging cord"),
        ("Much of the conference will involve practical exercises away from the computer, but they will need to go online once during the day to check in with the office.", "Power saving mode"),
        ("The conference lasts for several days, and part of it will be spent in a remote location without access to power.", "Power bank"),
    )
    fillers = ("Airplane mode", "USB cable", "Mobile hotspot")
    if randint(0,1) ==0:
        q = cf.SelectMcDrag(
            None, None, None, items, fillers, 1, 1, randint(4,7)
            )
        q.questionBase = f"{q.item(vl.names)}, a {q.item(vl.technitians)} {q.item(vl.users)}, needs to attend several day-long conferences and wants to ensure their mobile device will have enough power for these events. {items[q.choice][0]} Which of the following should a technician recommend to BEST accommodate their needs at the lowest cost?"
    else:
        q = cf.SelectMcDrag(
            'drag', None, None, items, fillers, 1, randint(1,3), randint(4,7)
            )
        q.questionBase = f"Match the solutions with the concerns of a management team sending a delegate to a conference"
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), cf.currentFuncName(), module_path(),"aa")
    return q.returnAll()

def aa_ha_Wireles_hotspot():
    correct = ("802.11")
    incorrect = (
        "127.0.0.1",
        "Port 8080",
        "192.601.xxx.xxx",
        "NFC",
        "WAN",
    )
    q = cf.SelectMcDrag(None, correct, incorrect, None, (), 1, 1, 4)
    q.questionBase = f"What type of network does a phone use when broadcasting as use as a wireless hotspot?"
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), cf.currentFuncName(), module_path(),"aa") 
    return q.returnAll()

def aa_hb_Mobile_hotspot():
    correct = (
        "you can connect to a mobile hotspot through its 802.11 network",
        "you can connect to a mobile hotspot by tethering with a USB cable",
        "you can connect to a mobile hotspot by tethering through bluetooth",
        "connecting to a mobile hotspot may incur charges to the hotspot owner", 
        "using a device as a hotspot will shorten battery life",
    )
    incorrect = (
        "you can connect to a mobile hotspot through port 8000",
        "you can connect to a mobile hotspot through it's address at 127.0.0.1",
        "you can connect to a mobile hotspot by tethering it through NFC",
        "you can connect to a mobile hotspot by tethering it through MAN",
        "you can connect to a mobile hotspot by tethering it through IMEI",
        "connecting to a mobile hotspot may incur charges to the owner of the connecting device",
        "using a device as a hotspot does not affect battery life",
    )
    number = randint(1,3)
    if randint(0,1):
        q = cf.SelectMcDrag(None, correct, incorrect, None, (), 1, number, randint(4,5))
        q.questionBase = f"Choose all correct statements about mobile wifi:"
    else:
        q = cf.SelectMcDrag(None, incorrect, correct, None, (), 1, number, randint(4,5))
        q.questionBase = f"Choose all incorrect statements about mobile wifi:"
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), cf.currentFuncName(), module_path(),"aa") 
    return q.returnAll()

def aa_hc_Wifi_on_mobile_devices():
    correct=(
        "airplane mode",
        "if an Apple user: swipe down to access the control center and turn on wifi",
        "if an Android user: go to settings, and wireless and network settings to turn on wifi",
    )
    incorrect=(
        "plug the phone into the plane's ethernet",
        "get the plane's Bluetooth pin",
        "find out the plane's bluetooth ID",
        "if an Apple user: swipe down to access the control center and turn on NFC",
        "if an Android user: go to settings, then wireless and network settings to enable PAN",
    )
    number = randint(1,3)
    if randint(0,1):
        q = cf.SelectMcDrag(None, correct, incorrect, None, (), 1, number, randint(4,5))
        q.questionBase = f'''A user in your company will shortly be making a business flight. During takeoff, they will be required to turn off all of their laptop's wireless functionality.
    After this, they want to be able to take aDvantage of the plane's free on board wifi. 
    Which of the following might they need to do in this situation? Select all correct optoions.'''
    else:    
        q = cf.SelectMcDrag(None, incorrect, correct, None, (), 1, number, randint(4,5))
        q.questionBase = f'''A user in your company will shortly be making a busniess flight, during which they will be required to turn off all of their wireless networks during takeoff. 
    After this, they want to be able to take advantage of the plane's free on board wifi. 
    Which of the following would they NOT need to do in this situation? Select all correct optoions.'''
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), cf.currentFuncName(), module_path(),"aa") 
    return q.returnAll()

def aa_hd_Using_bluetooth():
    correct=(
        "both devices must be bluetooth enabled",   
        "both devices must have bluetooth switched on",
        "both devices must be on discoverable mode",
        "a pin must be entered on the device making the connection request",
        "all Bluetooth devices must be paired manually the first time they are paired",
        "Bluetooth devices may pair automatically after the first pairing",
        "all discoverable devices in within range are listed",
        )
    incorrect=(
        "one of the devices must be Bluetooth enabled",
        "pairing always happens automatically",
        "all devices with Bluetooth on are discoverable",
        "one of the devices must have Bluetooth switched on",
        "a pin is unneccesary if you own both devices",
        "devices which you own are listed",
        )    
    number = randint(1,3)
    if randint(0,1):
        q = cf.SelectMcDrag(None, correct, incorrect, None, (), 1, number, randint(4,6))
        q.questionBase = f"Choose all correct statements about Bluetooth pairing:"
    else:
        q = cf.SelectMcDrag(None, incorrect, correct, None, (), 1, number, randint(4,6))
        q.questionBase = f"Choose all incorrect statements about Bluetooth pairing:"
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), cf.currentFuncName(), module_path(),"aa") 
    return q.returnAll()

def aa_he_pairing_devices():
    items = (
        ("1", "Both devices must have their bluetooth switched on"),
        ("2", "The device you wish to connect to must be discoverable"),
        ("3", "Find the device you wish to connect with in the discoverable devices list"),
        ("4", "Make a connection request"),
        ("5", "Enter the pin on the device you are connecting with"),
    )
    fillers = ()
    q = cf.SelectMcDrag('drag', None, None, items, fillers, 1, 5, 5)
    q.questionBase = f"Order the following steps of pairing bluetooth devices:"
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), cf.currentFuncName(), module_path(),"aa")
    
def aa_ia_Base_band_radio_processors():
    correct = (
        "they have their own firmware",
        "they have their own memory",
        "firmware is updated over the air",
        "updates are often invisible to end users",
        "updates include preffered roaming lists",
        "use prefered roaming lists to decide which towers to communicate with",
        "may be updated with network codes and country codes",
    )
    incorrect = (
        "they have their own firmware",
        "they use phone's memory",
        "firmware is updated only when user conents",
        "end users schedule updates",
        "are hardcoded with country and area codes",
    )
    number = randint(1,3)
    if randint(0,1):
        q = cf.SelectMcDrag(None, correct, incorrect, None, (), 1, number, randint(4,6))
        q.questionBase = f"Choose all correct statements about baseband mobile processors:"
    else:
        q = cf.SelectMcDrag(None, incorrect, correct, None, (), 1, number, randint(4,6))
        q.questionBase = f"Choose all incorrect statements about baseband mobile processors"
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), cf.currentFuncName(), module_path(),"aa") 
    return q.returnAll()

def aa_ib_IMEI_and_IMSI():
    correct = (
        "all cellular network enabled devices have a unique IMEI number",
        "IMEI stands for International Mobile Equipment Identity",
        "the IMEI allows services to be allowed on a device",
        "the IMEI allows services to be disallowed on a device",
        "IMSI stands for International mobile subscriber identity",
        "the ISMI identified each unique network user",
        "the ISMI can be linked to a sim card",
        "the ISMI can move between phones",
    )
    incorrect = (
        "stands for Integrated Mobile Encrypted Infrastructure",
        "all cellular enabled devices on a particular network have a unique IMEI Network number",
        "the ISMI allows services to be allowed on a device",
        "the ISMI allows services to be disallowed on a device",
        "IMSI stands for International Mobile Service Identity",
        "the IMEI identified each unique network user",
        "the IMEI can be linked to a sim card",
        "the IMEI can move between phones",
    )
    number = randint(1,3)
    if randint(0,1):
        q = cf.SelectMcDrag(None, correct, incorrect, None, (), 1, number, randint(4,6))
        q.questionBase = f"Choose all correct statements about IMEI and ISMI numbers:"
    else:
        q = cf.SelectMcDrag(None, incorrect, correct, None, (), 1, number, randint(4,6))
        q.questionBase = f"Choose all incorrect statements about IMEI and ISMI numbers:"
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), cf.currentFuncName(), module_path(),"aa") 
    return q.returnAll()

def aa_ic_Device_as_VPN_endpoint():
    correct = (
        "mobile devices can be turned into a VPN endpoint for secure communication",
        "a VPN allows secure communication between you and another device",
        "VPN software may be integrated into a phone",
        "VPN software may be downloaded into a phone",
        "VPN software may require additional configuration to function",
        "VPN software may require server information", 
        "VPN software may require an RSA secure ID to be generated",
        "a VPN admin may send a single file to update you with the VPN details",
    )
    incorrect = (
        "mobile devices can be turned into a VPN endpoint for faster communication",
        "a VPN allows faster communication between you and another device",
        "VPN software is always pre-configured",
        "VPN software may require mobile network information", 
        "VPN software may require an ISMI number to be generated",
        "VPN software may require an IMEI number to be generated",
        "a VPN admin may need access to your device to configure it correctly",
    )
    number = randint(1,3)
    if randint(0,1):
        q = cf.SelectMcDrag(None, correct, incorrect, None, (), 1, number, randint(4,6))
        q.questionBase = f"Choose all correct statements about using a device as a VPN endpoint:"
    else:
        q = cf.SelectMcDrag(None, incorrect, correct, None, (), 1, number, randint(4,6))
        q.questionBase = f"Choose all incorrect statements about using a device as a VPN endpoint:"
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), cf.currentFuncName(), module_path(),"aa") 
    return q.returnAll()



def aa_ja_Email_terminology():
    items = (
        ("pop", "post office protocol"),
        ("imap", "internet message access protocol"),
        ("tcp", "transmission control protocol"),
        ("smtp","simple message transfer protocol"),
        ("SSL", "secure socket layer")
        ("S/MIME", "secure multipurpose internet main extensions")
    )
    fillers = ('posting office protocol','post order protocol', 'internet message authentication protocol', 'international message access protocol', 'transmission computer protocol', 'transmitted control protocol', 'signed message transfer protocol','secure server layer','socket security layer')
    if randint(0,1) ==0:
        q = cf.SelectMcDrag(None, None, None, items, fillers, 1, 1, randint(4,6))
        q.questionBase = f"What does {items[q.choice][0]} stand for?"
    else:
        q = cf.SelectMcDrag('drag', None, None, items, fillers, 1, randint(2,4), randint(4,6))
        q.questionBase = f"Match the following accronyms with their correct descriptions?"
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), cf.currentFuncName(), module_path(),"aa")
    return q.returnAll()

def aa_jb_TCP_ports_used_for_email():
    items = (
        ("pop3","110"),
        ("SSL popS3","995"),
        ("IMAP","143"),
        ("SSL IMAPS","993"),
        ("SMTP no authentication","25"),
        ("SMPT with authentication","587"),
    )
    fillers = ("8000", "8080", "401","10", "111","992" "996", "404", "341", "994","26","52","586","785")
    if randint(0,1) ==0:
        q = cf.SelectMcDrag(None, None, None, items, fillers, 1, 1, randint(4,6))
        q.questionBase = f"What TCP port us used for {items[q.choice][0]}?"
    else:
        q = cf.SelectMcDrag('drag', None, None, items, fillers, 1, randint(2,4), randint(4,6))
        q.questionBase = f"Match the following protocols with their respective TCP ports:"
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), cf.currentFuncName(), module_path(),"aa")
    return q.returnAll()

def aa_jc_Email_protocols_and_configuration():
    correct = (
        "POP3 uses TCP/110",
        "SSL POP3 uses TCP/995",
        "older systems use POP3",
        "newer systems use IMAP4",
        "IMAP4 allows access to mail stored on a central server",
        "IMAP allows creation of folders",
        "IMAP allows server side searching",
        "POP3 allows downloading mail to a local client",
        "In POP3 services, network ports are defined by the email provider",
        "To use IMAP services, your system must know the name of the provider's server",
        "POP3 can optionally delete downloaded emails from the server",

    )
    incorrect = (
        "POP3 uses RTP/110",
        "POP3 uses HTTP/110",
        "SSL POP3 uses RTP/995",
        "SSL POP3 uses CPU/995",
        "older systems use IMAP4",
        "newer systems use POP3",
        "IMAP4 allows access to mail stored on your local server",
        "POP3 allows creation of folders",
        "POP3 allows server side searching",
        "SMTP allows downloading mail to a local client",
        "In POP3 services, network ports are defined locally",
        "To use IMAP services, you must have HTTP enabled",
        "POP3 alwaya deletes downloaded emails from the server", 
    )
    number = randint(1,3)
    if randint(0,1):
        q = cf.SelectMcDrag(None, correct, incorrect, None, (), 1, number, randint(4,8))
        q.questionBase = f"Choose all correct statements about Email protocols and configuration:"
    else:
        q = cf.SelectMcDrag(None, incorrect, correct, None, (), 1, number, randint(4,8))
        q.questionBase = f"Choose all incorrect statements about Email protocols and configuration:"
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), cf.currentFuncName(), module_path(),"aa") 
    return q.returnAll()

def aa_jd_Sending_and_recieving_Emails():
    correct = (
        "sending emails is done using SMPT",
        "SMPT allows mail to be sent from a device to a mail server",    
        "SMTP requires mail to be sent from a local device",
        "SMTP requires mail to be sent from a trusted device",
        "SMTP usually requires authentication to send messages",
        "SMTP with no authentication uses TCP/25",
        "SMTP with authentication uses TCP/587",
        "using unauthenticated SMTP is less common",
        "using authenticated SMTP is more common",
    )
    incorrect = (
        "sending emails is done using POP3",
        "sending emails is done using IMAP4",
        "sending emails is done using SPMT",
        "POP3 allows mail to be sent from a device to a mail server",    
        "IMAP4 allows mail to be sent from a device to a mail server",    
        "SMTP requires mail to be sent from a mobile device",
        "SMTP requires mail to be sent from an active device",
        "SMTP usually requires authentication to retrieve",
        "SMTP with authentication uses TCP/25",
        "SMTP with no authentication uses TCP/587",
        "using unauthenticated SMTP is more common",
        "using authenticated SMTP is less common",
    )
    
    number = randint(1,3)
    if randint(0,1):
        q = cf.SelectMcDrag(None, correct, incorrect, None, (), 1, number, randint(4,8))
        q.questionBase = f"Choose all correct statements about sending and recieving Emails:"
    else:
        q = cf.SelectMcDrag(None, incorrect, correct, None, (), 1, number, randint(4,8))
        q.questionBase = f"Choose all incorrect statements about sending and recieving Emails:"
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), cf.currentFuncName(), module_path(),"aa") 
    return q.returnAll()

def aa_je_Configuring_older_systems_for_Email():
    correct = (
        "you must provide network ports defined and provided by email provider",
        "TCP port 995 is used with SSL",
        "TCP port 110 is required where SSL is not used",
        "An email address and password is required to download emails using POP3", 
        "An email address and password is required to send emails using SMTP", 
        "TCP port 25 is used to send emails without authentication but is rarely used",
        "TCP port 587 is commonly used to send emails with SMTP and requires authentication",
    )
    incorrect = (
        "you must provide network ports defined by the user",
        "TCP port 995 is used where SSL is not required",
        "TCP port 110 is required where SSL is required",
        "An email address and password is required to download emails using SMTP", 
        "An email address and password is required to send emails using POP3", 
        "TCP port 25 is used to send emails with authentication but is rarely used",
        "TCP port 587 is commonly used to send emails with SMTP without authentication",
    )
    
    number = randint(1,3)
    if randint(0,1):
        q = cf.SelectMcDrag(None, correct, incorrect, None, (), 1, number, randint(4,6))
        q.questionBase = f"Choose all correct statements about configuring older systems for Email:"
    else:
        q = cf.SelectMcDrag(None, incorrect, correct, None, (), 1, number, randint(4,6))
        q.questionBase = f"Choose all incorrect statements about configuring older systems for Email:"
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), cf.currentFuncName(), module_path(),"aa") 
    return q.returnAll()

def aa_jf_Configuring_modern_systems_for_email():
    correct = (
        "network ports defined and provided by email provider",
        "TCP port 993 is used with SSL to download emails",
        "TCP port 143 is requires where SSL is not used to download emails",
        "An email address and password is required to download emails using IMAP4", 
        "An email address and password is required to send emails using SMTP", 
        "TCP port 25 is used to send emails without authentication but is rarely used",
        "TCP port 587 is commonly used to send emails with SMTP and requires authentication",
        "Folders may be created to store emails",
        "Emails stored on the server are searchable", 
    )
    incorrect = (
        "network ports defined and provided by the user",
        "TCP port 993 is used where SSL is not used to download emails",
        "TCP port 143 is requires where SSL is used to download emails",
        "Only an email address is required to download emails using IMAP4", 
        "Only a password is required to download emails using IMAP4", 
        "Only a password is required to send emails using SMTP", 
        "Only an email address is required to send emails using SMTP", 
        "TCP port 25 is used to send emails with SMTP with authentication but is rarely used",
        "TCP port 587 is commonly used to send emails with SMTP and requires no authentication",
        "Emails stored on the server are not searchable", 
    )
    number = randint(1,3)
    if randint(0,1):
        q = cf.SelectMcDrag(None, correct, incorrect, None, (), 1, number, randint(4,8))
        q.questionBase = f"Choose all correct statements about configuring modern systems for Email:"
    else:
        q = cf.SelectMcDrag(None, incorrect, correct, None, (), 1, number, randint(4,8))
        q.questionBase = f"Choose all incorrect statements about configuring modern systems for Email:"
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), cf.currentFuncName(), module_path(),"aa") 
    return q.returnAll()


def aa_jg_Configuring_and_using_enterprise_email():
    correct = (
        "commonly integrated with contacts, calendars and reminders",
        "information can be synchronised between devices", 
        "providers supply an email address", 
        "access to email is often through a provider's domain",
        "may use S/MIME to encrypt and sign messages",
        "gmail splits the inbox into tabs",
        "gmail uses imap4 and pop3",
        "Yahoo mail uses imap4 and pop3",
        "icloud email uses apple's main server and imap4",
    )
    incorrect = (
        "information secured on a single device", 
        "user supplies an email address", 
        "access to email is often through the user's own domain",
        "may use S/MIME to backup messages",
        "may use S/MIME to screen messages",
        "gmail provides a seperate server for each inbox",
        "gmail uses TCP and NFC",
        "Yahoo mail uses IMAP3 and POP4",
        "icloud email uses apple's main server and imail",
    )
    number = randint(1,3)
    if randint(0,1):
        q = cf.SelectMcDrag(None, correct, incorrect, None, (), 1, number, randint(4,8))
        q.questionBase = f"Choose all correct statements about configuring enterprise Email:"
    else:
        q = cf.SelectMcDrag(None, incorrect, correct, None, (), 1, number, randint(4,8))
        q.questionBase = f"Choose all incorrect statements about configuring enterprise Email:"
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), cf.currentFuncName(), module_path(),"aa") 
    return q.returnAll()


def aa_ka_Synchronisation(): 
    correct = (
        "most synchronisation is invisible to the user",
        "both client and server must authenticate each other for synchronisation to take place",
        "synchronisation can be between devices",
        "devices can synchronise to the cloud", 
        "synchronisation can be between a device and your car",
        "contacts, applications, email and pictures can be synchronised",
    )
    incorrect = (
        "most synchronisation requires user approval",
        "only the server must be authenticated for synchronisation to take place", 
        "only the client must be authenticated for synchronisation to take place", 
        "a device can be synchronised to itself",
        "synchronisation must be between mobile devices",
        "your processor and RAM can be synchronised", 
        "your IP address can be synchronised", 
    )
    number = randint(1,3)
    if randint(0,1):
        q = cf.SelectMcDrag(None, correct, incorrect, None, (), 1, number, randint(4,6))
        q.questionBase = f"Choose all correct statements about synchronisation:"
    else:
        q = cf.SelectMcDrag(None, incorrect, correct, None, (), 1, number, randint(4,6))
        q.questionBase = f"Choose all incorrect statements about synchronisation:"
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), cf.currentFuncName(), module_path(),"aa") 
    return q.returnAll()

def aa_kb_User_synchronisation():
    items = (
        ("An Apple user wants to synchronise their iphone with their car", "iOS Car Play"),
        ("An Apple user wants to synchronise their iphone with their desktop", "iTunes"),
        ("An Apple user wants to synchronise their iphone with the cloud", "iCloud"),
        ("An Android user wants to synchronise their device with their car", "Android Auto"),
        ("An Android user wants to backup their music to their desktop", "third party app"),
        ("An Android user wants to synchronise their calendar between devices", "gmail"),
    )
    fillers = ("youtube", "Apple iCar","Android Drive", "iDrive", "iPod", "iBackMeUp", "iSynch")
    if randint(0,1) ==0:
        q = cf.SelectMcDrag(None, None, None, items, fillers, 1, 1, randint(4,6))
        q.questionBase = f"{items[q.choice][0]}. What solution do you suggest?"
    else:
        q = cf.SelectMcDrag('drag', None, None, items, fillers, 1, randint(2,3), randint(4,6))
        q.questionBase = f"Match the following problems with their solutions:"
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), cf.currentFuncName(), module_path(),"aa")
    return q.returnAll()

def aa_kc_Synchronisation_to_desktop():
    correct = (
        "Enough disk space must be available on the backup device", 
        "Apple users may be able to synchronise using a lightning cable", 
        "Apple users may be able to synchronise using a USB-C cable", 
        "You can synchronise using your device's 802.11 wireless network", 
        "Android users may be able to synchronise using a USB-C cable", 
        "Android users may be able to synchronise using a Micro USB-B cable", 
    )
    incorrect = (
        "Data to be backed up will be compressed to fit available space on the backup device", 
        "Apple users may be able to synchronise using a micro USB-B cable",
        "Apple users may be able to synchronise using a thunderbolt cable",  
        "You cannot synchronise using your device's 802.11 wireless network", 
        "Android users may be able to synchronise using a lightning cable",
        "Android users may be able to synchronise using NFC", 
        "Android users may be able to synchronise using a USB-D cable", 
    )
    number = randint(1,3)
    if randint(0,1):
        q = cf.SelectMcDrag(None, correct, incorrect, None, (), 1, number, randint(4,6))
        q.questionBase = f"Choose all correct statements about synchronising with a desktop:"
    else:
        q = cf.SelectMcDrag(None, incorrect, correct, None, (), 1, number, randint(4,6))
        q.questionBase = f"Choose all incorrect statements about synchronising with a desktop:"
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), cf.currentFuncName(), module_path(),"aa") 
    return q.returnAll()

def aa_kd_Synchronising_with_a_car():
    correct = (
        "Apple users may synchronise their data with a compatible car using 'iOS Car Play'", 
        "Android users may synchronise their data with a compatible car using 'Android Auto'", 
        "you can synchronise contact data and music with some cars", 
        "when synchronised, your car and phone can share data in real time", 
        "synchronisation with a rental car may present security issues", 
        "synchronisation with a borrowed car may present security issues", 
        "data from your phone may be displayed on a larger screen in your car", 
        "you may be able to use car speakers to hear phone calls and music from your phone", 
        "synchronisation with your car can take place via cable", 
        "synchronisation with your can can take place via Bluetooth",
    )
    incorrect = (
        "data synchronised with a car is automaically deleted when it detects a new user", 
        "Apple users may synchronise their data with a compatible car using iTunes", 
        "Android users may synchronise their data with a compatible car using 'Gmail Drive'", 
        "you can directly interact with your cars on-board black box through synchronisation", 
        "your phone can only synchronise with your car via tethering", 
        "synchronisation with a rental car is no less safe than using an ATM",  
        "a mobile device synchronised with a car will be able to drive it",  
        "synchronisation with your car can take place via NFC", 
        "synchronisation with your can can take place via WAN",
    )
    number = randint(1,3)
    if randint(0,1):
        q = cf.SelectMcDrag(None, correct, incorrect, None, (), 1, number, randint(4,8))
        q.questionBase = f"Choose all correct statements about synchronising with a car:"
    else:
        q = cf.SelectMcDrag(None, incorrect, correct, None, (), 1, number, randint(4,8))
        q.questionBase = f"Choose all incorrect statements about synchronising with a car:"
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), cf.currentFuncName(), module_path(),"aa") 
    return q.returnAll()

def aa_ke_Synchronising_Apple_devices():
    correct = (
        "lighning connectors when synchronising data with a desktop",
        "USB-C connectors when synchronising data with a desktop",
        "iOS Car Play to synchronise data with a compatible car", 
        "iTunes to back up their mobile device data to cloud", 
        "recover their system data when backed up to the cloud", 
        "iTunes to back up contact data",
        "iTunes to back up music data",
        "iTunes to back up calendar data",
        "iOS to back up all data types to the cloud", 
    )
    incorrect = (
        "USB-D connectors when synchronising data with a desktop",
        "thunderbolt connectors when synchronising data with a desktop",
        "iOS Auto Synch to synchronise data with a compatible car", 
        "iTunes to back up only music data to cloud", 
        "iTunes back up all data except contact data",
        "iTunes to back up all data except music data",
        "iTunes to back up all data except calendar data",
        "iOS to back up only image data to the cloud", 
    )
    number = randint(1,3)
    if randint(0,1):
        q = cf.SelectMcDrag(None, correct, incorrect, None, (), 1, number, randint(4,7))
        q.questionBase = f"Choose all correct statements about synchronising Apple devices:"
    else:
        q = cf.SelectMcDrag(None, incorrect, correct, None, (), 1, number, randint(4,7))
        q.questionBase = f"Choose all incorrect statements about synchronising Apple devices:"
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), cf.currentFuncName(), module_path(),"aa") 
    return q.returnAll()

def aa_la_Trouble_reading_text():
    correct =('Use the magnifier.',)
    incorrect = ('Increase the resolution.','Use haptic feedback.','Utilize text-to-speech.',)
    q = cf.SelectMcDrag(None, correct, incorrect, None, (), 1, 1, 4)
    q.questionBase = f"A technician is setting up a Windows mobile device for a user who had trouble reading text on a previous device, especially at night. Which of the following adjustments would be MOST appropriate?"
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), cf.currentFuncName(), module_path(),"aa")
    return q.returnAll()

from django.shortcuts import render
from random import randint, randrange
from comptia_a_plus import comptia_classes_functions as cf
from comptia_a_plus import variety_lists as vl

def list_functions():
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
    return cf.moduleListGen(list_functions(), 'a', 0, 1)

def module_path():
    return '/comptia_a_plus/core_1_220_1001/'

#paper, series, question, name, marks in names

def ae_aa_ram_cmos_issue_symptom():
    ram = ('Continuous reboots','Blue Screen of death', 'The amount of RAM displays incorrectly', 'Sporadic freezes','Corrupted files', 'Attemps to install new programs fail','Video card fails to load', 'Ram not recognised by computer')
    cmos = ('Incorrect date or time displayed','Wrong BIOS time', 'Missing drivers for external devices such as printers', 'Unable to start programs')
    other = ('disdented capacitors', 'Computer starts in safe mode')
    choice = randint(0,1)
    number_to_find = randint(1,2)
    if choice == 1:
        correct, incorrect, component = ram, cmos + other, 'RAM'
        workon = "Symptoms of bad ram"
        weblink = "https://gigabytekingdom.com/signs-of-bad-ram/"
    else:
        correct, incorrect, component = cmos, ram + other, 'CMOS'
        workon = "Symptoms of CMOS battery failure"
        weblink = "https://www.techwalla.com/articles/the-signs-of-a-bad-cmos-battery"
    q = cf.SelectMcDrag(None, correct, incorrect, None, (), 1, number_to_find, randint(5,6))
    q.workon, q.weblink = workon, weblink
    q.questionBase = f"A technitian is troubleshooting what appears to be a {component} issue on a PC. Which {number_to_find} of the following symptoms indicate that this is a {component} issue?"
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), cf.currentFuncName(), module_path(),"ae")
    return q.returnAll()

def ae_ab_spillage_on_hardware():
    correct = ('Remove the case and organise the parts','Document the screw locations')
    incorrect = ('Search the internet for repair tutorials', 'Google the liquid and device', 'Consult colleagues for advice', f'Place the device in rice for a few days', 'Ask what time it happened', 'Ask what the brand of the liquid was')
    q = cf.SelectMcDrag(None, correct, incorrect, None, (), 1, 2, randint(5,6))
    q.questionBase = f"A {q.item(vl.users)} accidentally spills {q.item(vl.liquids)} on a laptop and, naturally, wants the device to be fixed and would like to know how much it will cost. Which of the following steps should the technician take NEXT to verify if the device is repairable before committing to a price?"
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), cf.currentFuncName(), module_path(),"ae")
    return q.returnAll()



def ae_ac_dropped_laptop():
    items = (
        ('the laptop will not turn on','DC jack'),
        ('the laptop will not turn on unless plugged into the mains', 'Battery'),
        ('the laptop makes unusual clicking and scratching sounds','Hard drive'),
        ('the laptop emits a strange smell whilst charging','Power adapter'),
        ('the laptop randomly shuts down after period of use','Cooling fan'),
    )
    q = cf.SelectMcDrag(None, None, None, items, (), 1, 1, 4)
    q.questionBase = f"A customer accidentally drops a laptop while it is charging. The next day, the customer notices {items[q.choice][0]} andcalls a technician to investigate. The technician confirms the laptop will not turn on even though it is connected to the power adapter. Which of the following components is the MOST likely cause of this behavior?"
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), cf.currentFuncName(), module_path(),"ae")
    return q.returnAll()


def ae_ad_grounding_hardware():
    correct =('Multimeter',)
    incorrect = ('Cable tester','Tone generator','Voltmeter',
                'grounding meter', 'Ethernet tester')
    q = cf.SelectMcDrag(
        None, correct, incorrect, None, (), 1, 1, randint(4, len(incorrect))
        )
    q.questionBase = f"During an inspection, it was found that data racks were not properly grounded. To pass the inspection and address a growingconcern to protect data cabling and equipment, a technician must make sure all racks are properly grounded. Which of the following tools should the {q.item(vl.technitians)} technician use to verify this has been completed?"
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), cf.currentFuncName(), module_path(),"ae")
    return q.returnAll()

def ac_cb_server_ram_upgrade():
    correct = ('The server needs DDR4 memory, and DDR3 is installed',)
    incorrect = ('The power supply is not supplying enogh power for the memory','The memory has too many ECC errors and is shutting down', 'The server is overheating when all of the mmeory is installed')
    q = cf.SelectMcDrag(None, correct, incorrect, None, (), 1, 1, 4)
    q.questionBase = f"A technician upgraded the memory on a server from two 8GB sticks to eight 32GB sticks. The server memory is now at full capacity per the user guide. When the technician powers on the system, only 128GB of memory is recognized by the OS and the BIOS. The technician decides to upgrade to the latest version of the firmware on the system, which does not help. Next, the technician installs the memory in sets of 64GB at a time. Each individual set of 64GB is fully recognized by the server. Which of the following will not allow the server to recognize all of the memory installed at the same time?"
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), cf.currentFuncName(), module_path(),"ae")
    return q.returnAll()


def ae_ba_slow_workstation_mc():
    correct = ('Check the event log for any cache issues',)
    incorrect = ('Replace the write cache battery', 'Clear the RAID configuration file and restart the PC', 'Replace the RAID controller write cache module', f'recommend changing to RAID 5')
    q = cf.SelectMcDrag(None, correct, incorrect, None, (), 1, 1, 4)
    q.questionBase = f"A technician is troubleshooting a Windows {q.item(vl.workstations)} workstation that is running slow. The computer uses RAID 10 and has dual GPU cards. The {q.item(vl.users)} using the workstation states that the same application runs faster on an identical workstation. Which of the following should the technician perform FIRST to troubleshoot the problem?"
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), cf.currentFuncName(), module_path(),"ae")
    return q.returnAll()

def ae_ca_broken_display_mc():
    correct = ('Document and label the cable and screw locations',)
    incorrect = ('Replace the screen with a non-OEM', 'Update the firmware on the device before repairing it', 'Replace the screen with an OEM', 'Immediately place the screen in a container to prevent liquid crystal leakage', 'Consult colleagues for advice', 'Remove the screen and inspect connectors for faults', 'Verify the settings in IPConfig','Research the problem based on symptoms', 'Tell the user to stay off the internet', "Wait for the vendor to provide more information")
    q = cf.SelectMcDrag(None, correct, incorrect, None, (), 1, 1, randint(5,len(incorrect)))
    q.questionBase = f"A {q.item(vl.technitians)} technician is replacing a broken screen on a new company laptop but does not have repair information from the vendor. Which of the following is the BEST way to proceed?"
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), cf.currentFuncName(), module_path(),"ae")
    return q.returnAll()

def ae_cb_dim_laptop_display_mc():
    items = (
        ("laptop display has suddenly become very dim. The image of the display can only be seen with a bright, externallight, as adjusting the brightness/contrast controls does not cause much change",'Inverter'),
        ("laptop screen appears to have dead pixels and a line of black pixels continuously at the same place.", "LCD panel"),
        ("laptop display has suddenly started displaying strange artefacts and stuttering. Restarting the laptop doesn't seem to help.","Video card"),
        ("touchscreen device seems to open applications at random, and is slow to respond to touch commands.", "Digitizer"),
    )
    fillers = ("RAM", "USB port", "CMOS battery", "Networking card")
    if randint(0,1) ==0:
        q = cf.SelectMcDrag(None, None, None, items, fillers, 1, 1, randint(4,7))
        q.questionBase = f"A {q.item(vl.technitians)} {q.item(vl.users)}'s {items[q.choice][0]} Which of the following components MOST likely needs to be replaced?"
    else:
        q = cf.SelectMcDrag('drag', None, None, items, fillers, 1, randint(1,3), randint(4,7))
        q.questionBase = f"Match the symptoms with the most probable faulty component"
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), cf.currentFuncName(), module_path(),"ae")
    return q.returnAll()

def ae_cc_projector_artefacts_mc():	
    correct =('Increase the projector contrast.','Modify the laptop™s display resolution.')
    incorrect = ('Update the video drivers on the laptop.','Replace the original laptop.','Change the aspect ratio on the projector.','Replace the bulb in the projector.',)
    q = cf.SelectMcDrag(None, correct, incorrect, None, (), 1, 2, randint(5,6))
    q.questionBase = f"A {q.item(vl.technitians)} technician is troubleshooting a laptop/projector combination that is displaying artifacts on the screen. When a differentlaptop is connected to the projector, the image appears to be correct but is very dim. Which of the following steps should the technician take to address these issues? (Choose two.)"
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), cf.currentFuncName(), module_path(),"ae")
    return q.returnAll()

def ae_da_smartphone_repair_mc():
    correct = ('Airplane mode',)
    incorrect = ('Tethering', 'Disabled hotspot', 'VPN', 'WiFi switched off', "SIM card faulty", "SIM card missing")
    q = cf.SelectMcDrag(None, correct, incorrect, None, (), 1, 1, randint(5,6))
    q.questionBase = f"A {q.item(vl.technitians)} {q.item(vl.users)} brings in a smartphone for repair. The device is unable to send/receive calls or connect to WiFi. All applications on the device are working unless they require connectivity. Which of the following is MOST likely causing the problem?"
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), cf.currentFuncName(), module_path(),"ae")
    return q.returnAll()


def ae_db_laptop_shuts_down_mc():	
    correct =('CMOS battery failure',)
    incorrect = ('Residual energy on the motherboard','System overheating','Distended capacitors','Loose battery connection',)
    q = cf.SelectMcDrag(None, correct, incorrect, None, (), 1, 1, 4)
    q.questionBase = f" A user's laptop is shutting down unexpectedly. The technician discovers the shutdowns only happen when the laptop is moved from one room to another. The technician reseated the hard drive, memory, battery, and LCD cable, but the laptop continues to shut down. Which of the following is the MOST probable cause of the issue?"
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), cf.currentFuncName(), module_path(),"ae")
    return q.returnAll()

def ae_ea_network_printer_not_working_mc():	
    items =(
        ('their network printer, which is connected through the print server, is not printing.', 'Clear the print queue.'),
        ('their printouts contain random characters.', "Reinstall the drivers on users' PCs."),
        ('some areas on their printouts are much lighter than others.',"Change the toner' PCs.")
    )
    fillers = ('Replace the USB cable.','Have users restart their PCs.',)
    if randint(0,1) ==0:
        q = cf.SelectMcDrag(None, None, None, items, fillers, 1, 1, randint(4,5))
        q.questionBase = f"Multiple {q.item(vl.technitians)} {q.item(vl.users)} report that {items[q.choice][0]} Which of the following should a {q.item(vl.technitians)} technician do FIRST to remedy this situation?"
    else:
        q = cf.SelectMcDrag('drag', None, None, items, fillers, 1, randint(1,3), randint(4,5))
        q.questionBase = f"Match the symptoms with a course of action likely to resolve the issue."
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), cf.currentFuncName(), module_path(),"ae")
    return q.returnAll()

def ae_eb_printer_to_share():
    correct =('Create a share on the manager\'s computer and give the users rights to the share.',)
    incorrect = ('Install the printer on the users\' desktops and point it to the IP address of the manager\'s computer.','Purchase a wireless printer so the users can access the printer via the network.','Provide flash drives to the users so they can transfer data to the manager\'s computer for printing.',)
    q = cf.SelectMcDrag(None, correct, incorrect, None, (), 1, 1, 4)
    q.questionBase = f"A printer stops working in the {q.item(vl.businesses)} department and cannot be repaired. A new printer has been ordered and a {q.item(vl.technitians)} technician is tasked with allowing other users to print to the manager's printer until the new printer arrives. The manager's printer is currently used via USB connection, and there are no network jacks available for use. Which of the following is the BEST way for the technician to allow access to the printer?"
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), cf.currentFuncName(), module_path(),"ae")
    return q.returnAll()

def ae_fa_malware_mc():
    correct = ('Document findings, actions, and outcomes','Run a virus scan.')
    incorrect = ('Reboot the device to verify the fix', 'Reconnect the device to the network', 'Consult colleagues for advice', f'Place the device in rice for a few days', 'Ask what time it happened', 'Verify the settings in IPConfig','Research the problem based on symptoms', 'Tell the user to stay off the internet', "set up teamviewer with the device to monitor the situation")
    q = cf.SelectMcDrag(None, correct, incorrect, None, (), 1, 2, randint(5,6))
    q.questionBase = f"A {q.item(vl.users)} is unable to access {q.item(vl.websites)} websites and has reported connectivity issues with pop-ups on the screen. A technician removes malware, and then is able to ping the router and access the websites. Which of the following NEXT steps should the technician perform in troubleshooting this issue? (Choose two)"
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), cf.currentFuncName(), module_path(),"ae")
    return q.returnAll()

def ae_fb_no_internet_after_holiday_mc():
    correct = ('ipconfig /flushdns',)
    incorrect = ('ipconfig /all', 'ipconfig /release', 'ipconfig /setclassid','Ipconfig /renew', 'ipconfig /registerdns',  'ipconfig /displaydns',)
    q = cf.SelectMcDrag(None, correct, incorrect, None, (), 1, 1, randint(5,6))
    q.questionBase = f"A {q.item(vl.users)} is no longer able to browse the Internet after returning from vacation. The user is able to log in and navigate to the local intranet, but not to any their favourite {q.item(vl.websites)} sites on the internet. A technician pings a well-known website by name but gets no reply. The technician then pings its IP address and gets a reply. Which of the following commands will MOST likely resolve the issue?"
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), cf.currentFuncName(), module_path(),"ae")
    return q.returnAll()

def ae_fc_ipconfig_commands_dr():
    items = (
        ('display all of your current IP information for all adapters', 'ipconfig /all'),
        ('forget your current IP information and obtain a new IP Address from the DHCP server', 'ipconfig /release'),
        ('get a new your IP Address if you set to obtain IP Address automatically', 'ipconfig /renew'),
        ('show your current DNS resolver cache logs', 'ipconfig /displaydns'),
        ('clear your current DNS resolver cache logs', 'ipconfig /flushdns'),
        ('update the DNS settings on the Windows computer', 'ipconfig /registerdns'),
    )
    if randint(0,1) ==0:
        q = cf.SelectMcDrag(None, None, None, items, (), 1, 1, randint(4,5))
        q.questionBase = f"which command can be used to {items[q.choice][0]}?"
    else:
        q = cf.SelectMcDrag('drag', None, None, items, (), 1, randint(1,3), randint(4,5))
        q.questionBase = "Match the descriptions with their commands."
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), cf.currentFuncName(), module_path(),"ae")
    return q.returnAll()

def ae_fc_windows_network_commands_dr():
    items = (
        ('identify server problems and latency by tracing the path of packets across the internet', 'tracert site.com'),
        ('get the IP address for a domain name', 'nslookup site.com'),
        ('get the domain name for an IP address', 'nslookup xxx.xxx.xxx.xxx'),
        ('determine what ports are open and being used, what programs are using your ports and what kind of TCP and UDP connections are present', 'netstat'),
        ('displays all active TCP connections and And TCP / UDP ports', 'netstat -a'),
        ('displays ethernet statistics', 'netstat -e'),
        ('displays all active programs that are listening', 'netstat -b'),
        ('winsock reset', 'netsh winsock reset'),
        ('reset or rebuild the Windows TCP/IP IP Stack', 'netsh int ip reset resetlog.txt'),
        ('get your computers local MAC address', 'getmac'),
        ('get the MAC address of your router or other devices on your local network', 'arp -a'),
    )
    if randint(0,1) ==0:
        q = cf.SelectMcDrag(None, None, None, items, (), 1, 1, randint(5,len(items)))
        q.questionBase = f"which command can be used to {items[q.choice][0]}?"
    else:
        q = cf.SelectMcDrag('drag', None, None, items, (), 1, randint(5,len(items)), len(items))
        q.questionBase = "Match the descriptions with their commands."
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), cf.currentFuncName(), module_path(),"ae")
    return q.returnAll()

def ae_fd_ping_commands_dr():
    items = (
        ('ping an ip address', 'ping xxx.xxx.xxx.xxx'),
        ('ping a website', 'ping site.com'),
        ('ping until ctrl stop is used to stop the command', 'ping xxx.xxx.xx.xx -t'),
        ('send out d number of pings', 'ping xxx.xxx.xx.xx -n d'),
        ('set packet size in bytes', 'ping xxx.xxx.xx.xx -l d'),
        ('set a time out for the ping in milliseconds, where d is an integer', 'ping xxx.xxx.xx.xx -w d'),
        ('resolve the host of an IP Address', 'ping -a xxx.xxx.xx.xx'),
    )
    if randint(0,1) ==0:
        q = cf.SelectMcDrag(None, None, None, items, (), 1, 1, randint(5,len(items)))
        q.questionBase = f"which command can be used to {items[q.choice][0]}?"
    else:
        q = cf.SelectMcDrag('drag', None, None, items, (), 1, randint(4,len(items)), len(items))
        q.questionBase = "Match the descriptions with their commands."
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), cf.currentFuncName(), module_path(),"ae")
    return q.returnAll()

def ae_fe_ip_in_use_mc():
    correct = ('Set the laptop configuration to DHCP to prevent conflicts',)
    incorrect = ('Remove the static IP configuration from the desktop', 'Replace the network card in the laptop, as it may be defective', 'Bridge the LAN connection between the laptop and the desktop',)
    q = cf.SelectMcDrag(None, correct, incorrect, None, (), 1, 1, 4)
    q.questionBase = f"A {q.item(vl.users)}, also a part time accountant, reports that after turning on their new laptop, they received a message stating their IP address is already in use on the system. They tried going back to their old desktop, which they now only use for {q.item(vl.online_activities)}, but received the same message. The technician checks the account and sees a comment that the {q.item(vl.users)} requires a special network setup to connect to the banking software. Which of the following should the technician do to resolve the issue?"
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), cf.currentFuncName(), module_path(),"ae")
    return q.returnAll()

def ae_ff_network_printer_mc():	
    correct =('Confirm that the laptop wireless card is turned on.',)
    incorrect = ('Confirm that the laptop is in range for the access point.','Confirm that the correct wireless network is selected.','Confirm the user\'s network login ID and password.',)
    q = cf.SelectMcDrag(None, correct, incorrect, None, (), 1, 1, 4)
    q.questionBase = f"A {q.item(vl.users)} reports that a laptop is not connecting to the corporate wireless network. A {q.item(vl.technitians)} technician confirms with a smartphone that the corporate wireless network is available and can be accessed. The technician observes that the Ethernet connection to the corporate network is working. The technician disconnects the Ethernet cable. Which of the following should the technician do NEXT to troubleshoot this problem?"
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), cf.currentFuncName(), module_path(),"ae")
    return q.returnAll()

def ae_fg_proprietory_data_mc():	
    correct =('Check corporate policies for guidance.',)
    incorrect = ('Get authorization from the manager.','Delete proprietary data before leaving the building.','Remove the HDD and send the device for repair.',)
    q = cf.SelectMcDrag(None, correct, incorrect, None, (), 1, 1, 4)
    q.questionBase = f"A {q.item(vl.businesses)}company has very strict rules regarding proprietary information leaving the premises. All computers host proprietaryinformation. A technician is called to repair a computer on-site at the company™s corporate office. The technician identifies theproblem and goes through the troubleshooting steps to create a plan of action. The technician determines the computer needs to be taken off-site for repair. Which of the following should the {q.item(vl.technitians)} technician do NEXT?"
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), cf.currentFuncName(), module_path(),"ae")
    return q.returnAll()

def ae_fb_new_wireless_network():
    correct =('Ensure the options are configured to provide a DNS server.',)
    incorrect = ('Verify the Windows Firewall is turned off.','Configure the wireless network™s SSID to be hidden.','Enable file and printer sharing in the OS.',)
    q = cf.SelectMcDrag(None, correct, incorrect, None, (), 1, 1, 4)
    q.questionBase = f"A {q.item(vl.technitians)} technician is setting up a new wireless network at a branch office that previously had only wired connectivity with statically assigned IP addresses. After setting up the network, the technician configures a server to provide IP addresses to wireless clients. During testing, they are unable to access the Internet or named network resources, although they receive a valid IP address from the DHCP server and can ping the default gateway. Which of the following should be technician check NEXT to resolve this issue?"
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), cf.currentFuncName(), module_path(),"ae")
    return q.returnAll()

def ae_fc_wired_computers_mc():	
    correct =('Check the DHCP server.',)
    incorrect = ('Check the closest AP for the area.','Check each wireless adapter switch.','Check the group™s network switch.',)
    q = cf.SelectMcDrag(None, correct, incorrect, None, (), 1, 1, 4)
    q.questionBase = f"Several computers are having network connectivity issues. Two of the computers are wired and are not having any issues.The technician verifies that none of the computers having issues have been assigned a static IP.Which of the following should the technician check NEXT?"
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), cf.currentFuncName(), module_path(),"ae")
    return q.returnAll()

def ae_fd_wired_computers_mc():	
    correct =('Virtual CPU',)
    incorrect = ('Virtual security','Virtual storage','Virtual switch', 'Virtual RAM',)
    q = cf.SelectMcDrag(None, correct, incorrect, None, (), 1, 1, 4)
    q.questionBase = f"A {q.item(vl.technitians)} technitian is setting up a VM for use in testing software deployments. The VM is offline, but the hypervisor is not. Which of the following settings should they change to resolve the issue?"
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), cf.currentFuncName(), module_path(),"ae")
    return q.returnAll()
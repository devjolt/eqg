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

def allSectionsList():
    section_lists = []
    sections = {
        'a':'IP basics and ports', 
        'b':'network devices',
        'c':'SOHO network installation',
        'd':'SOHO network configuration',
        'e':'802.11 wireless networks',
        'f':'cellular networks',
        'g':'network services',
        'h':'internet protocol',
        'i':'internet connection types',
        'j':'network types',
        'k':'network tools'
        }
    for key, value in sections.items():
        section_lists.append({key:(value, cf.moduleListGen(list_functions(), key, 2, 3)[0])})
    print(section_lists)
    return section_lists

def modulesList():#this list is used by views to automatically generate views!
    return cf.moduleListGen(list_functions(), 'a', 0, 1)

def module_path():
    return '/comptia_a_plus/core_1_220_1001/'

#paper, series, question, name, marks in names
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

def ab_aa_Networking_acronyms():
    correct = (
        "DSL stands for digital subscriber line",
        "DSL used to stand for digital subscriber loop",
        "ADSL stands for asymmetric digital subscriber loop",
        "DSL and ADSL are interchangable",
        "IP stands for internet protocol",
        "TCP stands for transmission control protocol", 
        "UDP stands for user datagram protocol ",
        "HTTP stands for Hyper Text Transport Protocol",
    )
    incorrect = (
        "DSL stands for digital service line",
        "DSL used to stand for digital secure loop",
        "ADSL stands for asymmetric digital service line",
        "DSL and ADSL are not interchangable",
        "IP stands for international protocol",
        "TCP stands for transport control protocol", 
        "UDP stands for usernet digital protocol ",
        "HTTP stands for Hyper Transport Telenet Protocol",
        "DSL stands for digital subscriber link",
        "DSL used to stand for digital subscriber linkage",
        "ADSL stands for asymmetric digital subscriber link",
        "IP and TCP are interchangable",
        "IP stands for interweb protocol",
        "TCP stands for transmission closed protocol", 
        "UDP stands for unicode datagram protocol",
        "HTTP stands for Hyper Terminal Transport Protocol",
    )
    number = randint(1,3)
    if randint(0,1):
        q = cf.SelectMcDrag(None, correct, incorrect, None, (), 1, number, randint(6,8))
        q.questionBase = f"Choose all correct statements:"
    else:
        q = cf.SelectMcDrag(None, incorrect, correct, None, (), 1, number, randint(6,8))
        q.questionBase = f"Choose all incorrect statements:"
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), cf.currentFuncName(), module_path(),"ab") 
    return q.returnAll()

def ab_ab_Network_payloads():
    correct = (
        "the ethernet payload is contained between an ethernet header and an ethernet trailer",
        "the ethernet payload consists of an IP header followed by an IP payload",
        "the IP payload consists of a TCP header followed by a TCP payload",
        "the TCP payload is often HTTP data",
    )
    incorrect = (
        "the ethernet payload is contained between a TCP header and a TCP trailer",
        "the ethernet payload consists of an HTTP header followed by an IP payload",
        "the IP payload consists of an ethernet header followed by an IP payload",
        "the TCP payload is often IP data",
        "the ethernet payload is contained between a HTML header and a HTML trailer",
        "the ethernet payload consists of an HTTP header followed by a TCP payload",
        "the IP payload consists of an ethernet header followed by an SMTP payload",
        "the TCP payload is always POP3 data",
    )
    number = randint(1,3)
    mod_name = cf.currentFuncName()
    if randint(0,1):
        q = cf.SelectMcDrag(None, correct, incorrect, None, (), 1, number, randint(4,5))
        q.questionBase = f"Choose all correct statements about {cf.underscoreless(mod_name)}:"
    else:
        q = cf.SelectMcDrag(None, incorrect, correct, None, (), 1, number, randint(4,5))
        q.questionBase = f"Choose all incorrect statements about {cf.underscoreless(mod_name)}:"
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), mod_name, module_path(),"ab") 
    return q.returnAll()

def ab_ac_transmission_control_protocol(): 
    correct = (
        "TCP is described as reliable",
        "TCP is connection oriented",
        "TCP requires a formal connection setup and close",
        "TCP can manage messages out of sequence",
        "TCP can manage retransmissions",
        "TCP allows the reciever to manage how much data is sent",
        "TCP enables recovery from eroneous transmissions",
        "TCP is suited to sending files",
    )
    incorrect = (
        "TCP is described as unreliable",
        "TCP is connectionless",
        "TCP does not require a formal connection setup and close",
        "TCP does not manage messages out of sequence",
        "TCP does not manage retransmissions",
        "TCP allows the sender to manage how much data is sent",
        "TCP is suited to steaming",
    )
    mod_name = cf.currentFuncName()
    number = randint(1,3)
    if randint(0,1):
        q = cf.SelectMcDrag(None, correct, incorrect, None, (), 1, number, randint(4,5))
        q.questionBase = f"Choose all correct statements about {cf.underscoreless(mod_name)}:"
    else:
        q = cf.SelectMcDrag(None, incorrect, correct, None, (), 1, number, randint(4,5))
        q.questionBase = f"Choose all incorrect statements about {cf.underscoreless(mod_name)}:"
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), mod_name, module_path(),"ab") 
    return q.returnAll()

def ab_ad_user_datagram_protocol():
    correct = (
        "UDP is described as unreliable",
        "UDP is connectionless",
        "UDP does not require a formal open or close to the connection",
        "UDP does not allow error recovery",
        "UDP does not allow reordering of data",
        "UDP does not manage retransmissions",
        "UDP enables the sender to determine the amount of data transmitted",
        "UDP is suited to streaming data",
        "UDP is suited for online gaming",
        "UDP is suited to watching content live",  
    )
    incorrect = (
        "UDP is described as reliable",
        "UDP is connection oriented",
        "UDP requires a formal open or close to the connection",
        "UDP allows error recovery",
        "UDP allowS reordering of data",
        "UDP manages retransmissions",
        "UDP enables the reciever to determine the amount of data transmitted",
        "UDP is suited to transmitting files",
    )
    mod_name = cf.currentFuncName()
    number = randint(1,3)
    if randint(0,1):
        q = cf.SelectMcDrag(None, correct, incorrect, None, (), 1, number, randint(4,5))
        q.questionBase = f"Choose all correct statements about {cf.underscoreless(mod_name)}:"
    else:
        q = cf.SelectMcDrag(None, incorrect, correct, None, (), 1, number, randint(4,5))
        q.questionBase = f"Choose all incorrect statements about {cf.underscoreless(mod_name)}:"
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), mod_name, module_path(),"ab") 
    return q.returnAll()


def ab_ae_UDV_vs_TCP():
    correct = (
        "UDP is faster at transmitting data than TCP",
        "TCP is slower at transmitting data than UDP",
        "TCP provides better data integrity than UDP", 
        "UDP us better for online gaming applications", 
        "UDP is better for livestreaming applications", 
        "TCP is better for sending files", 
        "TCP and UDP are suited to different purposes", 
        "UDP is faster than TCP",
    )
    incorrect = (
        "UDP is slower at transmitting data than TCP",
        "TCP is faster at transmitting data than UDP",
        "UDP provides better data integrity than TCP", 
        "TCP us better for online gaming applications", 
        "TCP is better for livestreaming applications", 
        "UDP is better for sending files", 
        "TCP is better than UDP because it is more reliable",
        "UDP is better than TCP because it is more reliable", 
    )
    mod_name = cf.currentFuncName()
    number = randint(1,3)
    if randint(0,1):
        q = cf.SelectMcDrag(None, correct, incorrect, None, (), 1, number, randint(4,5))
        q.questionBase = f"Choose all correct statements about {cf.underscoreless(mod_name)}:"
    else:
        q = cf.SelectMcDrag(None, incorrect, correct, None, (), 1, number, randint(4,5))
        q.questionBase = f"Choose all incorrect statements about {cf.underscoreless(mod_name)}:"
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), mod_name, module_path(),"ab") 
    return q.returnAll()

def ab_af_IP_sockets():
    correct = (
        "a server socket consists of a server IP address, protocol and a server application port number", 
        "a client socket consists of a client IP address, protocol and a client application port number", 
        "a socket includes an IP address, protocol and a port number",
        "a socket includes, among other things, an IP address",
        "a socket includes, among other things, protocol",
        "a socket includes, among other things, a port number",
    )
    incorrect = (
        "a client socket consists of a server IP address, protocol and a server application port number", 
        "a server socket consists of a client IP address, protocol and a client application port number", 
        "a socket includes an IP address, protocol and HTTP",
        "a socket includes an IP address, SSL and a port number",
        "a socket includes an IDSN address, protocol and a port number",
        "a socket includes, among other things a VIN number,",
        "a socket includes, among other things, ethernet connectors",
        "a socket includes, among other things, an RJ45 connector",
        "a socket includes, among other things, an antivirus check",    
    )
    mod_name = cf.currentFuncName()
    number = randint(1,3)
    if randint(0,1):
        q = cf.SelectMcDrag(None, correct, incorrect, None, (), 1, number, randint(4,5))
        q.questionBase = f"Choose all correct statements about {cf.underscoreless(mod_name)}:"
    else:
        q = cf.SelectMcDrag(None, incorrect, correct, None, (), 1, number, randint(4,5))
        q.questionBase = f"Choose all incorrect statements about {cf.underscoreless(mod_name)}:"
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), mod_name, module_path(),"ab") 
    return q.returnAll()

def ab_ag_TCP_and_UDP_port_values():
    noneph = randint(0, 1023)
    eph = randint(1024, 65535)
    ports = randint(0,65535)
    nonports = randint(65536, 100000)
    correct = (
        "ports 0-1023 are usually non-ephemeral",  
        "ports 1024-65535 are usually ephemeral",
        "TCP can use TCP ports 0-65535",
        "UDP can use UDP ports 0-65535",
        "TCP and UDP use seperate ports",
        f"tcp/{ports} is a valid port",
        f"udp/{ports} is a valid port",
        f"tcp/{nonports} is an invalid port",
        f"udp/{nonports} is an invalid port",
        f"tcp/{eph} is an ephemeral port",
        f"udp/{eph} is an ephemeral port",
        f"tcp/{noneph} is a non-ephemeral port",
        f"udp/{noneph} is a non-ephemeral port",
    )
    incorrect = (
        "UDP and TCP share ports",
        f"tcp/{ports} is an invalid port",
        f"udp/{ports} is an invalid port",
        f"tcp/{nonports} is a valid port",
        f"udp/{nonports} is a valid port",
        f"tcp/{eph} is a non-ephemeral port",
        f"udp/{eph} is a non-ephemeral port",
        f"tcp/{noneph} is an ephemeral port",
        f"udp/{noneph} is an ephemeral port",
    )
    mod_name = cf.currentFuncName()
    number = randint(1,3)
    if randint(0,1):
        q = cf.SelectMcDrag(None, correct, incorrect, None, (), 1, number, randint(4,5))
        q.questionBase = f"Choose all correct statements about {cf.underscoreless(mod_name)}:"
    else:
        q = cf.SelectMcDrag(None, incorrect, correct, None, (), 1, number, randint(4,5))
        q.questionBase = f"Choose all incorrect statements about {cf.underscoreless(mod_name)}:"
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), mod_name, module_path(),"ab") 
    return q.returnAll()

def ab_ah_ephemeral_and_non_ephemeral_ports():
    noneph = randint(0, 1023)
    eph = randint(1024, 65535) 
    correct = (
        "non-ephemeral ports are fixed",
        "non-ephemeral ports are usually linked to a server or service",
        "ephemeral ports are temporary",
        "ephemeral ports are assigned in real time by a client",
        "ports 0-1023 are usually non-ephemeral",  
        "ports 1024-65535 are usually ephemeral",
        f"tcp/{eph} is an ephemeral port",
        f"udp/{eph} is an ephemeral port",
        f"tcp/{noneph} is a non-ephemeral port",
        f"udp/{noneph} is a non-ephemeral port",
    )
    incorrect = (
        "ephemeral ports are fixed",
        "ephemeral ports are usually linked to a server or service",
        "non-ephemeral ports are temporary",
        "non-ephemeral ports are assigned in real time by a client",
        f"tcp/{eph} is a non-ephemeral port",
        f"udp/{eph} is a non-ephemeral port",
        f"tcp/{noneph} is an ephemeral port",
        f"udp/{noneph} is an ephemeral port",
    )
    mod_name = cf.currentFuncName()
    number = randint(1,3)
    if randint(0,1):
        q = cf.SelectMcDrag(None, correct, incorrect, None, (), 1, number, randint(4,5))
        q.questionBase = f"Choose all correct statements about {cf.underscoreless(mod_name)}:"
    else:
        q = cf.SelectMcDrag(None, incorrect, correct, None, (), 1, number, randint(4,5))
        q.questionBase = f"Choose all incorrect statements about {cf.underscoreless(mod_name)}:"
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), mod_name, module_path(),"ab") 
    return q.returnAll()


def ports_protocols():
 #(0'tcp/udp', 1'port', 2'Full name', 3'XXX',4'description'),
    return (
        ('tcp/17', "Quote of the day protocol", "QTDP", "return a string of text and close the connection" ),
        ("tcp/20", "File Transfer Protocol (active mode data)", "FTP (data)","transfer file data between systems"),
        ("tcp/21", "File Transfer Protocol (control)", "FTP (control)", "control transfer of file data between systems"),
        ("tcp/22", "Secure Shell", "SSH", "use an encrypted communication link"),
        ("tcp/23", "Telecommunication Network", "Telnet", "login to devices remotely and In-the-clear communication"),
        ("tcp/53", "Domain name system", "DNS", "convert names to IP addresses"),
        ("udp/67", "Dynmanic host configuration protocol", "DHCP (server)", "automate configuration of IP address, subnet mask and other options"),
        ("udp/68",  "Dynmanic host configuration protocol", "DHCP (client)", "automate configuration of IP address, subnet mask and other options"),
        ("tcp/80", "Hypertext transfer protocol", "HTTP","web server communication"),
        ("tcp/110", "Post office Protocol 3", "POP3","basic mail transfer functionality"),
        ("udp/119", 'Network News Transfer Protocol', 'NTP', 'transfer usenet news articles'),
        ("udp/123", "Network time protocol", "NTP", "synchronise clocks and recieve timestamps"),
        ("tcp/143", "Internet message access protocol", "IMAP4","Email with inbox management from multiple clients"),
        ('udp/161', 'Simple network management protocol',"SNMP", "gather query statistics from network devices"),
        ("udp/162", 'Simple network management protocol',"SNMP", "gather traps statistics from network devices"),
        ("tcp/389", "Lightweight Directory Access Protocol","LDAP", "store and retrieve information in a network directory"),    
        ("udp/427", "Service location protocol", "SLP", "dertermine location of a device"),
        ("tcp/443", "Hypertext transfer protocol secure", "HTTPS","web server communication with encryption"),
        ("tcp/445", "NetBIOS-less SMB commication", "CIFS","file and printer sharing"),
        ("tcp/3389", "Remote desktop protocol", "RDP", "share an application or entire desktop from a remote location"), 
        #19
        ("udp/137", "NetBIOS name service (nbname)", "nbname",""),
        ("udp/138", "NetBIOS datagram service (nbdatagram)", "nbdatagram",""),
        ("udp/139", "NetBIOS session services (nbsession)", "nbsessnio",""),
        ("tcp/548", "Apple Filing Protocol file services"),
    )

def ab_ai_network_protocol_uses():
    pplist = ports_protocols()[:-4]
    itemnos = {randint(0,len(pplist)-1)}
    while len(itemnos) != 10:
        itemnos.add(randint(0,len(pplist)-1))
    if randint(0,1) == 0:
        if randint(0,1) == 0:
            items = [(pplist[i][2],pplist[i][3]) for i in itemnos]
            q = cf.SelectMcDrag(None, None, None, items, (), 1, 1, randint(4,5))
            q.questionBase = f"What is {items[q.choice][0]} used for?"
        else:
            items = [(pplist[i][3],pplist[i][2]) for i in itemnos]
            q = cf.SelectMcDrag(None, None, None, items, (), 1, 1, randint(4,5))
            q.questionBase = f"Which protocol would you use to {items[q.choice][0]}?"
    else:
        items = [(pplist[i][3],pplist[i][2]) for i in itemnos]
        q = cf.SelectMcDrag('drag', None, None, items, (),1, randint(2,4), randint(5,7))
        q.questionBase = "Match the following protocols with the following services:"
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), cf.currentFuncName(), module_path(),"ab")
    return q.returnAll()

def ab_aj_internet_service_protocols():
    pplist = ports_protocols()
    itemnos = {randint(0,len(pplist)-1)}
    while len(itemnos) != 10:
        itemnos.add(randint(0,len(pplist)-1))
    if randint(0,1) == 0:
        if randint(0,1) == 0:
            items = [(pplist[i][0],pplist[i][1]) for i in itemnos]
            q = cf.SelectMcDrag(None, None, None, items, (), 1, 1, randint(4,5))
            q.questionBase = f"Which service would you access through {items[q.choice][0]}?"
        else:
            items = [(pplist[i][1],pplist[i][0]) for i in itemnos]
            q = cf.SelectMcDrag(None, None, None, items, (), 1, 1, randint(4,5))
            q.questionBase = f"Which port would you open to allow {items[q.choice][0]}?"
    else:
        items = [(pplist[i][1],pplist[i][0]) for i in itemnos]
        q = cf.SelectMcDrag('drag', None, None, items, (),1, randint(2,4), randint(5,7))
        q.questionBase = "Match the following ports with their respective services:"
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), cf.currentFuncName(), module_path(),"ab")
    return q.returnAll()

def ab_ak_firewall_configuration():
    pplist = ports_protocols()[:-4]
    itemnos = {randint(0,len(pplist)-1)}
    while len(itemnos) != 10:
        itemnos.add(randint(0,len(pplist)-1))        
    if randint(0,1) == 0:
        items = [(pplist[i][0],pplist[i][3]) for i in itemnos]
        q = cf.SelectMcDrag(None, None, None, items, (), 1, 1, randint(4,5))
        q.questionBase = f"A network engineer configures a firewall to allow traffic through {items[q.choice][0]}. Which service are they trying to access?"
    else:
        items = [(pplist[i][3],pplist[i][0]) for i in itemnos]
        q = cf.SelectMcDrag(None, None, None, items, (), 1, 1, randint(4,5))
        q.questionBase = f"An network engineer is attempting to unsuccessfully {items[q.choice][0]}. Investigating further, they realise that the functionality is being blocked by their firewall. Which port should they open to allow the desired functionality?"
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), cf.currentFuncName(), module_path(),"ab")
    return q.returnAll()

def ab_al_client_server_ports():
    pplist = ports_protocols()[:-4]
    itemnos = {randint(0,len(pplist)-1)}
    while len(itemnos) != 10:
        itemnos.add(randint(0,len(pplist)-1))
    items = [pplist[i] for i in itemnos]
    right = []
    for i in range(5):
        right.append(items.pop(randint(0,len(items)-1)))
    correct = []
    for item in right:
        correct.append(f'From source port {randint(1024, 65535)} to destination {item[0]} to {item[3]} ({item[2]})')
    incorrect = []
    item = items.pop()
    incorrect.append(f'From source port {randint(1024, 65535)} to destination {randint(1024, 65535)} to {item[3]} ({item[2]})')
    incorrect.append(f'From source port {randint(1024, 65535)} to destination {randint(1024, 65535)} to {item[3]} ({item[2]})')
    incorrect.append(f'From source port {item[0]} to destination {item[0]} to {item[3]} ({item[2]})')
    incorrect.append(f'From source port {item[0]} to destination {item[0]} to {item[3]} ({item[2]})')
    incorrect.append(f'From source port {item[0]} to destination {randint(1024, 65535)} to {item[3]} ({item[2]})')
    mod_name = cf.currentFuncName()
    number = randint(1,4)
    if randint(0,1):
        q = cf.SelectMcDrag(None, correct, incorrect, None, (), 1, number, randint(6,7))
        q.questionBase = f"Identify valid source (client) and destination (server) port configurations:"
    else:
        q = cf.SelectMcDrag(None, incorrect, correct, None, (), 1, number, randint(6,7))
        q.questionBase = f"Identify valid source (client) and destination (server) port configurations:"
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), mod_name, module_path(),"ab") 
    return q.returnAll()
'''
which of these are valid source (client) and destination (server) ports to be used to access the following data:
which of these are invalid source (client) and destination (server) ports to be used to access the following data:

source > 1023
correct protocol udp tcp
correct protocol port

HTTP data from TCP source port 3000 to TCP destination port 80
VoiP data from UDP source port 7100 to UDP destination port 5004
Email data from TCP source port 
'''


def ab_am_network_ports():
    items = (
        ('File Transfer Protocol, data transfer', 20),
        ('File Transfer Protocol, command and control', 21),
        ('Secure Shell', 22),
        ('Time protocol', 37),
        ('WHOIS', 43),
        ('Domain Name Service', 53),
        ('Hypertext Transfer Protocol', '80 and 443'),
        ('Trivial File Transfer Protocol', 69),
    )
    fillers = (501, 404, 99, 127, 8080)
    if randint(0,1) == 0:
        q = cf.SelectMcDrag(None, None, None, items, fillers, 1, 1, randint(4, 8))
        q.questionBase = f"Which of the following ports deals with {items[q.choice][0]}?"
    else:
        q = cf.SelectMcDrag('drag', None, None, items, fillers, 1, randint(4, 6), randint(6, 10))
        q.questionBase = f"Match the ports with their functions."
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), cf.currentFuncName(), module_path(),"ab")
    return q.returnAll()

def ab_an_network_ports():
    items = (
        ('close to block remote logins to a server', 21),
        ('change to another port because it is the default SSL port well known to hackers', 22),
    )
    fillers = (43, 53, 80, 443, 69)
    q = cf.SelectMcDrag(None, None, None, items, fillers, 1, 1, randint(4, 5))
    q.questionBase = f"Which of the following ports should a technitian {items[q.choice][0]}?"
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), cf.currentFuncName(), module_path(),"ab")
    return q.returnAll()

def ab_ba_network_devices():
    items = (
        ('can be used to connect multiple devices within a network without broadcasting to every network port', 'Unmanaged switch'),
        ('connects multiple computers or other network devices together without the need for an IP address', 'Hub',),
        ('is a network security system that monitors and controls incoming and outgoing network traffic based on predetermined security rules', 'Firewall'),
        ('provides bi-directional data communication via radio frequency channels on a hybrid fibre-coaxial', 'Cable modem'),
        ('allows a personal computer or a router to receive Internet access via a mobile broadband connection', 'Wireless modem')
    )
    q = cf.SelectMcDrag(None, None, None, items, (), 1, 1, 4)
    q.questionBase = f"Which of the following {items[q.choice][0]}?"
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), cf.currentFuncName(), module_path(),"ab")
    return q.returnAll()

def ab_ca_cable_type_soho_mc():
    correct = ("Ethernet",)
    incorrect = ("Coaxial", "USB", "Thunderbolt", "Lightning", "Bluetooth")
    q = cf.SelectMcDrag(None, correct, incorrect, None, (), 1, 1, randint(4, len(incorrect)))
    q.questionBase = f"Which of the following cable types should be used to connect a cable modem to a SOHO router?"
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), cf.currentFuncName(), module_path(),"ab")
    return q.returnAll()




def ab_da_networking_numbers():
    items = (
        ("a channel commonly used on an 802.11 wireless network","6"),
        ("an ip address known as local host", "127.0.0.1"),
        ("an ip adress you would expect to be associated with a router","192.168.X.X"),
        ("a port number assigned to commonly used internet communication protocol","80"),
        ("a port number associated with DNS","500"),
        ("an alternative port for http","8080"),
    )
    if randint(0,1) ==0:
        q = cf.SelectMcDrag(None, None, None, items, (), 1, 1, randint(4, len(items)))
        q.questionBase = f"Which one of the following is {items[q.choice][0]}?"
    else:
        q = cf.SelectMcDrag('drag', None, None, items, (), 1, randint(1,4), randint(4, len(items)))
        q.questionBase = f"Match the description with the number."
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), cf.currentFuncName(), module_path(),"ab")
    return q.returnAll()

def ab_db_wireless_printer():
    correct =('Connect the printer to the company wireless network.',)
    incorrect = ("Set up the user's computer to act as a print server.",'Configure the printer to use the Internet printing protocol.',"Ensure the user's computer is set to DHCP.",)
    q = cf.SelectMcDrag(None, correct, incorrect, None, (), 1, 1, 4)
    q.questionBase = f"A {q.item(vl.users)} purchases a wireless printer and sets it up in an office. They install all necessary software for the printer on thecomputer and connects the printer to the guest wireless network. However, when they attempt to print to the printer, nothing happens. Which of the following will resolve the issue?"
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), cf.currentFuncName(), module_path(),"ab")
    return q.returnAll()

def ab_ea_internal_external_networking_mc():
    correct = ("MAN","LAN")
    incorrect = ("WAN", "PAN", "SAN", "WLAN", "VPN", "Enterprise Internal Private Network", "System Area Network", "Skynet", "Mobile Network")
    q = cf.SelectMcDrag(None, correct, incorrect, None, (), 1, 2, randint(4, len(incorrect)))
    q.questionBase = f"A {q.item(vl.businesses)} business client has three locations within city limits that need to be networked. Vendor network requirements for all three locations are a minimum of 1GB. Which of the following are the types of networks that will MOST likely be used for internal office and office-to-office networking? (Choose two.)"
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), cf.currentFuncName(), module_path(),"ab")
    return q.returnAll()

def ab_eb_networking_acronyms_dr():
    items = (
        ('a computer network that interconnects users with computer resources in a geographic region of the size of a metropolitan area', 'MAN'),
        ('a computer network that interconnects computers within a limited area such as a residence, school, laboratory, university campus or office building', 'LAN'),
        ('a telecommunications network that extends over a large geographic area', 'WAN'),
        ('a computer network for interconnecting electronic devices centered on an individual person\'s workspace', 'PAN'),
        ('a computer network which provides access to consolidated, block-level data storage', 'SAN'),
        ('a computer network that links two or more devices using wireless communication', 'WLAN'),
        ('a service which extends a private network across a public network and enables users to send and receive data across shared or public networks as if their computing devices were directly connected to the private network', 'VPN'),
    )
    if randint(0,1) ==0:
        q = cf.SelectMcDrag(None, None, None, items, (), 1, 1, randint(4, len(items)-1))
        q.questionBase = f"Which one of the following is {items[q.choice][0]}?"
    else:
        q = cf.SelectMcDrag('drag', None, None, items, (), 1, randint(4,5), randint(5, len(items)-1))
        q.questionBase = f"Match the definitions with their acronyms."
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), cf.currentFuncName(), module_path(),"ab")
    return q.returnAll()

def ab_ea_internal_external_networking_mc():
    items = (
        ("office to office networking within a city", "MAN"),
        ("computer network within the office", "LAN"),
        ("5G services nationwide","WAN"),
        ("connectivity for devices within employees personal space", "PAN"),
        ("access to consolidated, block level storage","SAN"),
        ("wireless facilities for employees at an office","WLAN"),
        ("increased security and privacy for employees","VPN"),
    )
    if randint(0,1) ==0:
        q = cf.SelectMcDrag(None, None, None, items, (), 1, 1, randint(4, len(items)))
        q.questionBase = f"A {q.item(vl.businesses)} business wishes to provide {items[q.choice][0]}. Which of the following technologies are best suited to provide this service? (Choose one)"
    else:
        q = cf.SelectMcDrag('drag', None, None, items, (), 1, randint(4,5), randint(5, len(items)))
        q.questionBase = f"Match the described services with the accronyms of the technology which makes them possible."
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), cf.currentFuncName(), module_path(),"ab")
    return q.returnAll()

def ab_eb_reducing_password_tickets_mc():
    items = (
        ("Several company users are frequently forgetting passwords for their mobile devices and applications. Which of the following should the systems administrator do to reduce the number of help desk tickets submitted?",'Implement single sign-on.'),
        ("A business owner requires a high level of security on all of their devices. Which of the following could be implemented at the lowest cost to achieve this?", 'Enable multifactor authentication.'),
        ("A business requires that all devices are only able to be accessed by the emplyee to which it is issued. Which of the following would achieve this most effectively?", 'Configure biometric authentication.'),
    )
    fillers = ('Remove complex password requirements.','Remove password requirements', 'Adopt one password for all employees', 'Set each password to the employees employee number')
    if randint(0,1) ==0:
        q = cf.SelectMcDrag(None, None, None, items, fillers, 1, 1, randint(4, 6))
        q.questionBase = f"A {q.item(vl.businesses)} business wishes to provide {items[q.choice][0]}. Which of the following technologies are best suited to provide this service? (Choose one)"
    else:
        q = cf.SelectMcDrag('drag', None, None, items, fillers, 1, randint(4,5), randint(5, 6))
        q.questionBase = f"Match the described problems with solutions."
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), cf.currentFuncName(), module_path(),"ab")
    return q.returnAll()


def ab_fa_hosting_virtual_machines():
    correct =('Hypervisor',)
    incorrect = ('Disk management','Terminal services','Device Manager','Virtual LAN',)
    q = cf.SelectMcDrag(None, correct, incorrect, None, (), 1, 1, 4)
    q.questionBase = f"A {q.item(vl.technitians)} systems administrator is configuring a server to host several virtual machines. The administrator configures the server andis ready to begin provisioning the virtual machines. Which of the following features should the administrator utilize to complete the task?"
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), cf.currentFuncName(), module_path(),"ab")
    return q.returnAll()


def ab_fb_lan_security():
    items = (
        ('install a device that will proactively stop outside attacks from reaching the LAN', 'IPS'),
        ('install some software which will alert them when attempts are made to compromise their system','IDS'),
        ('identify something to act as a firewall and web filter','Proxy server'),
        ("identify something to verify users' identities before they access applications", 'Authentication server')
    )
    q = cf.SelectMcDrag(None, None, None, items, (), 1, 1, 4)
    q.questionBase = f"A {q.item(vl.technitians)} network administrator must install {items[q.choice][0]}. Which of the following devices would BEST meet the organization's needs?"
    q.previousQ, q.nextQ, q.currentQname, q.nextQname, q.previousQname = cf.previousNext(list_functions(), cf.currentFuncName(), module_path(),"ab")
    return q.returnAll()



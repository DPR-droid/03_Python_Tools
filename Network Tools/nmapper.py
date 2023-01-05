# https://www.geeksforgeeks.org/port-scanner-using-python-nmap/

import nmap
   
# take the range of ports to 
# be scanned
begin = 75
end = 80
  
# assign the target ip to be scanned to
# a variable
target = '192.168.5.52'
   
# instantiate a PortScanner object
scanner = nmap.PortScanner()
   
for i in range(begin,end+1):
   
    # scan the target port
    res = scanner.scan(target,str(i))
   
    # the result is a dictionary containing 
    # several information we only need to
    # check if the port is opened or closed
    # so we will access only that information 
    # in the dictionary
    res = res['scan'][target]['tcp'][i]['state']
   
    print(f'port {i} is {res}.')


nmScan = nmap.PortScanner()

# scan localhost for ports in range 21-443
nmScan.scan(target, '75-80')

# run a loop to print all the found result about the ports
for host in nmScan.all_hosts():
     print('Host : %s (%s)' % (host, nmScan[host].hostname()))
     print('State : %s' % nmScan[host].state())
     for proto in nmScan[host].all_protocols():
         print('----------')
         print('Protocol : %s' % proto)
 
         lport = nmScan[host][proto].keys()
         lport.sort()
         for port in lport:
             print ('port : %s\tstate : %s' % (port, nmScan[host][proto][port]['state']))
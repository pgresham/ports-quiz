#!/usr/bin/python3

#the following was used to build the array for this program:
#a = ''
#services = []
#while True:
#    a = str(input('service: '))
#    if a == 'done':
#        break
#    b = str(input('port: '))
#    services.append([a,b])
#print(services)


import random
import time
import os
import copy

def clear():
    os.system('clear')
def menu():
    print('Network+ Ports Quiz')
    print('1 Practice The Ports')
    print('2 Test Your Knowledge')
    print('00 Exit (Works Any Time)')


def practice(SERVICES):

    services = copy.deepcopy(SERVICES)
        #Use a local copy to avoid killing the global one
    while len(services)>0:
        index = random.randint(0,len(services)-1)
        quiz = str(input(services[index][0]+'> '))
        if quiz == '00':
            break
        elif quiz == services[index][1]:
            print('correct!')
            del services[index]
            time.sleep(.75)
            clear()
        else:
            print(services[index][1])
            time.sleep(.75)
            clear()

            
def quiz(SERVICES):
    services = copy.deepcopy(SERVICES)
    total = len(services)
    correct = 0
    while len(services)>0:
        index = random.randint(0,len(services)-1)
        quiz = str(input(services[index][0]+'> '))
        if quiz == '00':
            break
        elif quiz == services[index][1]:
            correct +=1        
        else:
            pass
        del services[index]
        clear()
    print('%.2f'%((correct/total)*100)+'%')
if __name__ == '__main__':
    #This could easily be replaced with a file
    services = [['ssh', '22'], ['dns', '53'], ['smtp', '25'], ['sftp', '22'], ['ftp', '20,21'], ['tftp', '69'], ['telnet', '23'], ['dhcp', '67,68'], ['http', '80'], ['https', '443'], ['snmp', '161'], ['rdp', '3389'], ['ntp', '123'], ['sip', '5060,5061'], ['smb', '445'], ['pop', '110'], ['imap', '143'], ['ldap', '389'], ['ldaps', '636']]
   
    clear()
    menu()
    while True:
        try:
            choice = str(input('Enter your choice: '))
            if choice == '1':
                clear()
                practice(services)
                menu()
            elif choice == '2':
                clear()
                quiz(services)
                menu()
            elif choice == '00':
                print('goodbye!')
                exit(0)
            else:
                clear()
                menu()
        except Exception as e:
            print('Error: '+e)



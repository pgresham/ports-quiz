#!/usr/bin/python3

import random
import time
import os
import copy

#Windows/Posix compatible!
if os.name == 'nt':
    def clear():
        os.system('cls')
else:
    def clear():
        os.system('clear')	


    
def menu():
    print('Network+ Ports Quiz')
    print('1 Practice The Ports')
    print('2 Test Your Knowledge')
    print('00 Exit (Works Any Time)')


def gen(file='default.txt'):
    #Error handling done in the mainloop for this block
    #Usually I would want to handle errors within the function.
    services = []
    with open(file,'r') as f:
        for line in f:
            services.append(line.strip().split(':'))
            #current code supports only single line questions and answers 
            #formatted as question:answer in specified text file
        f.close()
    return services

    
### Practice asks each question in turn and either returns
### 'correct' if answered correctly or flashes the correct
### answer on the screen. Incorrectly answered questions
### are recycled and asked again until right. 
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


###Quiz destructively runs through a copy of the array and 
###returns a grade based on how many right versus the total
###number of questions asked
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



###Let's put it all together...
if __name__ == '__main__': 

###Load services variable: The main quiz array formatted as
### [ ['question1','answer1'],['question2','answer2']...['question n','answer n']]
### from a file formatted as question:answer delimited by newlines.
    while True:
        fname = str(input('select quiz file [default.txt]: '))
        if fname == '':
            try:
                services = gen('default.txt')
                break
            except Exception as e:
                print(e)
                tryagain = str(input('try again? y/n: '))
                while tryagain != 'y' and tryagain != 'n':
                    tryagain = str(input('try again? y/n: '))
                    if tryagain =='n':
                    	exit()
                    elif tryagain == 'y':
                        break
                    else:
                        exit()
        else:
            try:
                services = gen(fname)
                break
            except Exception as e:
                print(e)
                tryagain = str(input('try again? y/n: '))
                if tryagain == 'n':
                    exit()
                elif tryagain == 'y':
                    pass
                else:
                    while tryagain != 'y' or 'n':
                        tryagain = str(input('try again? y/n: '))
                        if tryagain == 'n':
                            exit()
                        elif tryagain == 'y':
                            break
                        else:
                            exit()
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



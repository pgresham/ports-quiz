#!/usr/bin/python3

import os

if os.name == 'nt':
    def clear():
        os.system('cls')
else:
    def clear():
        os.system('clear')	

def isfile(fname):
	try:
		with open(fname,'r') as f:
		    f.close()
	except:
		return False
	return True
	
if __name__ == '__main__':
    clear()
    print('This script is intended to speed up the')
    print('process of generating quiz files for its')
    print('companion script ports_quiz.py\n')
    print('Basically it formats your questions and')
    print('answers like so in a specified text file:\n')
    print('question 1:answer 1\nquestion 2:answer 2\n...\nquestion n:answer n\n')
    print('type 00 when you are done and ready to write the file.')
    try:

        fname = input('ready? Enter filename for your quiz: ')
        if isfile(fname):
            yn = str(input('File exists! append (a)/overwrite (w)/exit [exit]:'))
            if yn == 'append' or yn =='a':
                quizfile = open(fname,'a')
            elif yn =='overwrite' or yn == 'w':
                quizfile = open(fname,'w')
            elif yn =='exit' or yn == '':
                exit(0)
            else:
                exit(0)
        else:
            quizfile = open(fname,'w')
    except Exception as e:
        print(e)
        exit(0)
    try:
        services = []
        while True:
            a = str(input('question: '))
            if a == 'done':
                break
            else:
                pass
            b = str(input('answer: '))
            if b == 'done':
                break
            else:
                pass
            services.append([a,b])
        for i in services:
	        quizfile.write(i[0]+':'+i[1]+'\n')
    except Exception as e:
        print(e)
    finally:
        quizfile.close()

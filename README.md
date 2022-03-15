# ports-quiz 
## Ports Quiz for Network+ Exam 
 
### What is it?
This is a simple study tool to learn the port/protocol associations on the CompTIA Network+ exam among others. 

### How do I use it?
To use the default program, simply run the ports_quiz.py script in the same directory as the default.txt quiz file. The script will first ask for a file to read from. Pressing enter accepts the default vale of `default.txt`. I will discuss custom files later in this readme.<br/>
<br/>
You are then confronted with the main menu:<br/>

`Network+ Ports Quiz`<br/>
`1 Practice The Ports`<br/>
`2 Test Your Knowledge`<br/>
`00 Exit (Works Any Time)`<br/><br/>
Let's select option 1. *As a note if you want to exit at any point, type `00` to get back to the last menu or exit.*<br/>
You shold now see the name of a protocol. Type your answer as the port or ports associated with that protocol.<br/><br/>
For instance let's say you select Practice see `ssh>` <br/>
You would answer `22` and get the response `correct!`<br/>
If you entered `23` however, it will tell you the right answer and recycle the question back into the rotation.<br/>
Let's say you get one like DHCP that has two ports. You would type`67,68` with a comma and no spaces between the two numbers.
Correctly answered questions are removed from the list until all questions have been answered correctly<br/>
<br/><br/>
Selecting option 2 provides a similar format but without feedback when a question is answered wrong. Each question is also asked only once and the number of right versus wrong answers are tallied and returned as a percentage "grade" at the end. Again `00` will stop the test and exit back to the main menu.<br/><br/>
### Great, now I know my ports. Can I make a custom file?
Yes! The code can easily be adapted to quiz just about anything using the quiz_maker.py script included with the main file. If you want to manually make your own file, format your text file as follows:
<br/>
`question 1:answer 1`<br/>
`question 2:answer 2`<br/>
...and so on to `question n: answer n`<br/>

As a note, the parser reads each line as a question answer pair, so multi-line questions will need to be put on a single line.

### Can I use this code or any part of if for my own project?
It's Licensed under CC0. Go nuts. 

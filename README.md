# ports-quiz
## Ports Quiz for Network+ Exam

### What is it?
This is a simple study tool to learn the port/protocol associations on the CompTIA Network+ exam among others. 

### How do I use it?
To use the default program, simply run the ports_quiz.py script in the same directory as the default.txt quiz file. The script will first ask for a file to read from. Pressing enter accepts the default vale of `default.txt`. I will discuss custom files later in this readme.<br/>
It will show you a protocol and you answer with the port or ports associated with it.<br/><br/>
For instance let's say you see `ssh>` <br/>
you'd answer `22` and get the response `correct!`<br/>
If you entered `23` however, it will tell you the right answer and recycle the quetion back into the rotation.
<br/><br/>
### Great, I know my ports. Can I make a custom file?
Yes! The code can easily be adapted to quiz just about anything using the quiz_maker.py script included with the main file. If you want to manually make your own file, format your text file as follows:
<br/>
`question 1:answer 1`<br/>
`question 2:answer 2`<br/>
...and so on to `question n: answer n`<br/>

As a note, the parser reads each line as a question answer pair, so multi-line questions will need to be put on a single line.

### Can I use this code or any part of if for my own project?
It's Licensed under CC0. Go nuts. 

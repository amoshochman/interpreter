# interpreter

An exercise that fills the below instructions:

Implementing an Interpreter for a simple programming language called ALPL.

The interpreter input is a text file containing the ALPL program, the interpreter should run the ALPL program.

Description + language rules:

● The language only deals with positive or negative integer numbers </br>
● There are ten registers numbered R0 - R9, each register can hold an integer number</br>
● All the language tokens are in UPPERCASE</br>
● Each line includes exactly one command or label, there are no multiline commands</br>
● A label is an alphanumeric token followed by a colon (the token can’t be a command or a register name)</br>
● When the program reaches the end of file it is ended</br>
● List of commands:</br>

![image](https://user-images.githubusercontent.com/36486045/226184206-420fda6e-fbfe-48ce-a0c9-ea5007d237ae.png)

1: The LET expression is composed of:</br>
● Left operand : register or integer</br>
● Operator : + or * (plus or multiply) - optional</br>
● Right operand: register or integer - required if operator exists</br>

2: The IF operator can be : =, <, > (equal to, less than, greater than)</br>

![image](https://user-images.githubusercontent.com/36486045/226184243-4bb1f1f7-3251-4c54-8748-8b3ccc1136af.png)

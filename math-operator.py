


# Task 1 - basic math operations

print('Task 1 - basic math operations')

# add (+)
int_num1 = 12
int_num2 = 34
answer_main = int_num1 + int_num2 
print(int_num1, '+', int_num2, '=', answer_main )

int_num1 = 3
int_num2 = 90
answer_main = int_num1 + int_num2 
print(int_num1, '+', int_num2, '=', answer_main )

# subtract (-)
int_num1 = 86
int_num2 = 56
answer_main = int_num1 - int_num2 
print(int_num1, '-', int_num2, '=', answer_main )

int_num1 = 43
int_num2 = 56
answer_main = int_num1 - int_num2 
print(int_num1, '-', int_num2, '=', answer_main )


# multiply (*)
int_num1 = 4
int_num2 = 4
answer_main = int_num1 * int_num2 
print(int_num1, '*', int_num2, '=', answer_main )

int_num1 = 40
int_num2 = 4
answer_main = int_num1 * int_num2 
print(int_num1, '*', int_num2, '=', answer_main )


# divide (/)
int_num1 = 4
int_num2 = 5
answer_main = int_num1 / int_num2 
print(int_num1, '/', int_num2, '=', round(answer_main,2) )

int_num1 = 40
int_num2 = 5
answer_main = int_num1 / int_num2 
print(int_num1, '/', int_num2, '=', round(answer_main,2) )


# modulo (%) --> divides and returns only the integer 
int_num1 = 16
int_num2 = 5
answer_main = int_num1 % int_num2 
print(int_num1, '%', int_num2, '=', answer_main)

int_num1 = 28
int_num2 = 5
answer_main = int_num1 % int_num2 
print(int_num1, '%', int_num2, '=', answer_main)

# power (**)
int_num1 = 2
int_num2 = 4
answer_main = int_num1 ** int_num2 
print(int_num1, '**', int_num2, '=', answer_main) 

int_num1 = 4
int_num2 = 3
answer_main = int_num1 ** int_num2 
print(int_num1, '**', int_num2, '=', answer_main) 


# floor (//) --> divides and returns the integer in 'float type'
int_num1 = 12.2
int_num2 = 3
answer_main = int_num1 // int_num2 
print(int_num1, '//', int_num2, '=', round(answer_main,2)) 


int_num1 = 21.3
int_num2 = 3
answer_main = int_num1 // int_num2 
print(int_num1, '//', int_num2, '=', round(answer_main,2)) 


# boolean (True, False)
print('True * False', '=',  True * False) 
print('True * True', '=',  True * True) 

# Basic math Operations on Mixed Data Types
# complex (e.g 2-3j)
int_num1 = 5
complex_num1 = (2 - 3j)
complex_num2 =  int_num1 * complex_num1 
print('5 * (2 - 3j', '=', complex_num2)

int_num1 = 5
complex_num1 = (int_num1 + 1j) 
complex_num2 = complex_num1 * 4
print(int_num1, '+ 1j', '=', complex_num2)


import math
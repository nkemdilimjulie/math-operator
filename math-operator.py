


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
print('4 * (int_num1 + 1j)', '=', complex_num2)


# Task2: basic math function

print('Task2: basic math function')


import math


# maximum number
print('max(2, 2.0, -0.5)', '=', max(2, 2.0, -0.5))
print('max(-20, 2.0, -0.5)', '=', max(-20, 2.0, -0.5))

# minimum number
print('minimum number')
print('min(23, 22, 55.0)', '=', min(23, 22, 55.0))
print('min(23, 22, -55.0)', '=', min(23, 22, -55.0))


# absoluteb number
print('absoluteb number')
print('abs(-34.23)', '=', abs(-34.23)) # returms 34.23
print('abs(-84.23)', '=', abs(-84.23))

# power
print('power')
print('pow(3, 4)', '=', pow(3, 4)) # meaning 3^4
print('pow(7, 2)', '=', pow(7, 2)) 

# cell function
print('cell function')
print('ceil(34/5)', '=', math.cell(34/5)) # the cell function after division returns the next integer number = 7
print('ceil(82/4)', '=', math.cell(82/4)) 


# floor function
print('floor function')
print('floor(34/5)', '=', math.floor(34/5)) # the floor function after division returns the lower integer number = 6 
print('floor(34/3)', '=', math.floor(34/3)) 


# maximum boolean
print('maximum boolean')
print('max(True, False)', '=', max(True, False)) # returns TRUE as maximium
print('max(True, True)', '=', max(True, True)) # returns TRUE as maximium


# absolute complex
print('absolute complex')
print('abs(4 - 3j)', '=', abs(4 - 3j))  # returns 5.0)
print('abs(8 - 2j)', '=', abs(8 - 2j))  
 
print('More is yet to come ...')
print('Python is indeed a high-level (human understandable) programming language')
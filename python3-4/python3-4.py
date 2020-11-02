#Numbers - int float complex

#int
iVal = 34
print(f'iVal = {iVal}')

#float
fVal = 3.14
print(f'fVal = {fVal}')
import sys
print(sys.float_info) # https://docs.python.org/3/library/sys.html#sys.float_info

#complex - complex([real[, imag]])
cVal = 3 +6j
print(f'cVal = {cVal}')
cVal = complex(5,3)
print(f'cVal = {cVal}')
print(f'real = {cVal.real}, imag = {cVal.imag}')

#Basic numerical operations

x = 3
print(f'x = {x}')

y = x + 3 #add
print(f'add = {y}')

y = x - 1 #subtract
print(f'subtract = {y}')

y = x * 6.846 #multiply
print(f'multiply = {y}')

y = x / 0.5 #divide
print(f'divide = {y}')

y = x ** 2 #pow
print(f'pow = {y}')

y = x % 2.5 #remain
print(f'remain = {y}')



from mpmath import mp
from sympy.parsing.mathematica import parse_mathematica
from sympy import mathematica_code

# Set the desired precision in mpmath
mp.dps = 15

# Define the mathematical expression as a string
expression_string = "Sin[Pi/4] + Sqrt[2]"  # Use SymPy compatible format

# Parse the expression using SymPy
expression_sympy = parse_mathematica(expression_string)

# Convert the SymPy expression to an mpmath expression
expression_mpmath = mathematica_code(expression_sympy)

# Evaluate the expression using mpmath
namespace = {'sin': mp.sin, 'pi': mp.pi, 'sqrt': mp.sqrt}  # Define necessary functions
result = eval(expression_mpmath, namespace) 

# Print the result
print(result)
from re import findall, split, compile
from itertools import permutations, accumulate
from functools import reduce

"""
Los sumandos son los operadores en la operacion suma, por
ejemplo en ab + cd, ab y cd son sumandos.

Por conmutatividad ab + cd es lo mismo que cd + ab

Los factores son los operadores de la operacion
multiplicacion, por ejemplo en 4ab, 4, a, y b son factores.

Por conmutatividad 4ab, a4b, ab4, ba4, ab4 y a4b son lo mismo.

Se si tuviera la expresion ab + cd y considerado la propiedad
conmutativa de la operacion suma y la operacion multiplicacion
todas las respuestas correctas
serian ab + cd, ba + cd, ab + dc, ba + dc, cd + ab, cd + ba,
dc + ab y dc + ba.
"""

def commutativity(expression: str) -> list[str]:
  """
  Input: Receives a mathematical expression.
  Output: Returns an array with all possible
  permutations of the expression considering
  the commutative property of addition and
  multiplication.
  """

  expression.replace(" ", "")

  summands = get_summands(expression) # get summands
  #print(summands)
  
  factor_permutations = []
  for summand in summands:
    factors = get_factors(summand) # get factors of each summand
    factor_permutations.append(get_permutations(factors))
  #print(factor_permutations)
  
  queue_1 = []
  queue_2 = []
  for perm in factor_permutations:
    queue_1.append(perm["number_of_permutations"])
    queue_2.append(perm["permutations"])
  #print(queue_1)
  #print(queue_2)
  
  results = []
  
  # With one summands
  if(len(queue_1) == 1):
    for i in range(queue_1[0]):
      for j in permutations([queue_2[0][i]]):
        results.append(j)
		
  # With two summands
  if(len(queue_1) == 2):
    for i in range(queue_1[0]):
      for j in range(queue_1[1]):
        for k in permutations([queue_2[0][i], queue_2[1][j]]):
          results.append(k)
		  
  # With three summands
  if(len(queue_1) == 3):
    for i in range(queue_1[0]):
      for j in range(queue_1[1]):
        for k in range(queue_1[2]):
          for l in permutations([queue_2[0][i], queue_2[1][j], queue_2[2][k]]):
            results.append(l)
  
  results_2 = []
  result_expression = ""
  first_expression = True

  for summands in results:
    #print(summands)
    # Each resulting multiplication is used as an summand
    for summand in summands:
      if("-" in summand):
        # Correct the position of the minus sign in the multiplication
        expression = correct_the_summnad(summand)
        #print(expression)
      else:
        expression = summand
      if(first_expression == True):
        result_expression = expression
        first_expression = False
      else:
        result_expression = result_expression + "+" + expression
    results_2.append(result_expression)
    result_expression = ""
    first_expression = True
    #expression = ""
  
  #print(results_2)

  # The +- in the sum is corrected
  results_3 = []
  for result in results_2:
    # Replace +- sign with -, for example 3+-4 would be 3-4
    results_3.append(replace_sign(result, '\+-', r'-'))

  return results_3

def correct_the_summnad(summand):
  # Correct the position of the minus sign in the summnad
  remove_minus_sign = replace_sign(summand, '\-', r'')
  return "-" + remove_minus_sign

def get_permutations(factors): # cambiar nombre a: obtener las permutaciones de los factores
  perms = permutations(factors)
  perms_obtained = []
  for i in perms:
    perms_obtained.append("".join(i)) # convert from tuple to string
  return {"permutations": perms_obtained, "number_of_permutations": len(perms_obtained)}

def get_factors(expression):
  return findall("-[a-z]\^[0-9]|-[0-9]|-[a-z]|[a-z]\^[0-9]|[0-9]|[a-z]", expression)

def get_summands(expression):  
  # Substraction becomes addition of a negative number.
  # Replace - sign with +-, for example 3-4 would be 3+-4
  expression_2 = replace_sign(expression, '\-', r'+-')
  result = split("\+", expression_2)
  if "" in result:
    result.remove("")
  return result
  
def replace_sign(expression, original_sign, new_sign):
  p = compile(original_sign)
  return p.sub(new_sign, expression)

people = [
            ['Bilbo', 'Baggins'],
            ['Gollum'],
            ['Tom', 'Bombadil'],
            ['Aragorn']
        ]

# Change everything below here to use while loops instead
"""for person in people:
    to_print = ""
    for name in person:
        to_print += name + " "
    print(to_print)
    """

# VOID FUNCTIONS
# all function below are void. try printing the output of their function calls
"""
def void_func_1(message):
  print(message)

def void_func_2(message):
  print(message)
  return None

def void_func_3(message):
  print(message)
  return

res_1, res_2, res_3 = void_func_1('hi'), void_func_2('hei'), void_func_3('ho')
print("void returning:", res_1, res_2, res_3)


# FRUITFUL FUNCTIONS
# adding a value to the return statement makes a function "fruitful" - it gives it a value that can be worked forward with

def fruitful_func(message):
  # print(message)  # whether or not this is here, the function call produces a value
  return message

f_res = fruitful_func('yay')
print("fruitful returning:", f_res)
"""

"""
# fix the code so it works as expected
# use return to create an output for the function
# assign the output to a variable
# print that variable
name = "Mycroft"

def print_name_box():
  print(name)

  def smaller_box():
    '''
    (re)assigning a variable within the same scope
    overwrites the same variable from an outer scope
    -> you cannot use it *before* assigning it,
    if you assign it at all anywhere in that scope.
    --TASK--: uncomment the below print() statement
        and interpret the results when running it
    '''

    print(name)
    name = "Sherlock"

    def smallest_box():
      '''
      inner scopes always draw from the next-outer layer
      after 'name' got overwritten, the name that will
      be printed is NOT the global-scope name anymore
      '''

      print(name)

    smallest_box(name)

  smaller_box()

print_name_box()
"""

def shout(name):
    loud_name = name.upper()
    return loud_name
    print(loud_name)
#thing = loud_name
#print(thing)

shout("wilma")
#print(loud_name)
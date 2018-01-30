def ACamelCaseFunction():
    print("It works!")

class a_snake_case_class():
    def ACamelCaseMethod():
        pass

aWrongVar = None 

import pepize

assert(a_snake_case_class is ASnakeCaseClass)
assert(a_camel_case_function is ACamelCaseFunction)
assert(a_wrong_var is aWrongVar)

a_camel_case_function()
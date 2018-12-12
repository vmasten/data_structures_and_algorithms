"""Validate whether brackets properly close when opened, like a linter."""
from ...data_structures.stack.stack import Stack


def validate(string):
    """Validate open and closing brackets in a string input."""
    """Loops over the string, stores opening brackets in a stack
        and returns true if brackets are valid, false if not."""
    result = True
    validate_stack = Stack()

    if string[0] == ')' or string[0] == ']' or string[0] == '}':
        return False
        # no need to check anything else

    for i in range(len(string)):
        if string[i] == '(' or string[i] == '[' or string[i] == '{':
            validate_stack.push(string[i])

        if string[i] == ')':
            if validate_stack.top.val == '(':
                validate_stack.pop()

        if string[i] == ']':
            if validate_stack.top.val == '[':
                validate_stack.pop()

        if string[i] == '}':
            if validate_stack.top.val == '{':
                validate_stack.pop()

    if validate_stack.top:
        result = False
        return result

    return result

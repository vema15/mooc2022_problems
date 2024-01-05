

def balanced_brackets(my_string: str):  
    stripped_string = [item for item in my_string if item in "[]()"]
    if len(stripped_string) == 0:
        return True
    if not ((stripped_string[0] == '(' and stripped_string[-1] == ')') or (stripped_string[0] == '[' and stripped_string[-1] == ']')):
        return False

    # remove first and last character
    return balanced_brackets(stripped_string[1:-1])

if __name__ == "__main__":
    ok = balanced_brackets("([([])])")
    print(ok)
    
    ok = balanced_brackets("(python version [3.7]) please use this one!")
    print(ok)
    
    # this is no good, the closing bracket doesn't match
    ok = balanced_brackets("(()]")
    print(ok)
    
    # different types of brackets are mismatched
    ok = balanced_brackets("([bad egg)]")
    print(ok)
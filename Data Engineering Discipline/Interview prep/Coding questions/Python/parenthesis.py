def arebracketsbalanced(expr):
    stack = []
    
    for char in expr:
        if char in ['(', '{', '[']:
            stack.append(char)
        else:
            if not stack:
                return False
            current_char = stack.pop()
            if current_char == '(':
                if char != ')':
                    return False
            if current_char == '[':
                if char != ']':
                    return False
            if current_char == '{':
                if char != '}':
                    return False
    if stack:
        return False
    return True


if __name__ == "__main__":
    expr = "1{()}[]"
    print(arebracketsbalanced(expr))
    
    if arebracketsbalanced(expr):
        print("Balanced")
    else:  
        print("Not Balanced")
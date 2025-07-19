def tokenize(expression: str):
    expression = expression.replace('×', '*').replace('x', '*').replace('÷', '/')
    tokens = []
    number = ''
    i = 0
    while i < len(expression):
        char = expression[i]

        if char == '*' and i + 1 < len(expression) and expression[i + 1] == '*':
            if number:
                tokens.append(number)
                number = ''

            tokens.append('^') 
            i += 2
            continue

        if char.isdigit() or char == '.':
            number += char

        elif char == '-' and (i == 0 or expression[i-1] in '(-+*/^'):
            number = '-'

        else:
            if number:
                tokens.append(number)
                number = ''

            if char in '+-*/^()':
                tokens.append(char)

        i += 1

    if number:
        tokens.append(number)

    i = 0
    while i < len(tokens) - 1:
        curr, nxt = tokens[i], tokens[i+1]
        if (curr.replace('.', '', 1).lstrip('-').isdigit() or curr == ')') and (nxt == '(' or nxt.replace('.', '', 1).lstrip('-').isdigit()):
            tokens.insert(i+1, '*')

        i += 1

    return tokens

def precedence(op: str):
    if op == '^': return 3

    if op in ('*', '/'): return 2

    if op in ('+', '-'): return 1

    return 0

def to_postfix(tokens: list[str]):
    output = []
    stack = []
    for token in tokens:
        if token.replace('.', '', 1).lstrip('-').isdigit():
            output.append(token)

        elif token == '(':
            stack.append(token)

        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())

            stack.pop()

        else:
            while stack and stack[-1] != '(':
                if precedence(token) < precedence(stack[-1]) or (precedence(token) == precedence(stack[-1]) and token != '^'):
                    output.append(stack.pop())

                else:
                    break

            stack.append(token)

    while stack:
        output.append(stack.pop())

    return output

def evaluate_postfix(postfix: list[str]):
    stack = []
    for token in postfix:
        if token.replace('.', '', 1).lstrip('-').isdigit():
            stack.append(float(token))

        else:
            b = stack.pop()
            a = stack.pop()
            if token == '+': stack.append(a + b)

            elif token == '-': stack.append(a - b)

            elif token == '*': stack.append(a * b)

            elif token == '/': stack.append(a / b)

            elif token == '^': stack.append(a ** b)

    return stack[0]

def handle_expression(expression: str):
    tokens = tokenize(expression)
    postfix = to_postfix(tokens)
    result = evaluate_postfix(postfix)
    return result

expression = input("Enter expression: ")
print("Result:", handle_expression(expression))
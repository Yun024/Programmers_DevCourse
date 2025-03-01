class ArrayStack:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]


def splitTokens(exprStr):
    tokens = []
    val = 0
    valProcessing = False
    for c in exprStr:
        if c == ' ':
            continue
        if c in '0123456789':
            val = val * 10 + int(c)
            valProcessing = True
        else:
            if valProcessing:
                tokens.append(val)
                val = 0
            valProcessing = False
            tokens.append(c)
    if valProcessing:
        tokens.append(val)

    return tokens


def infixToPostfix(tokenList):
    prec = {
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        '(': 1,
    }

    opStack = ArrayStack()
    postfixList = []
    
    for i in tokenList:
        if i in prec:
            if i == '(' or opStack.isEmpty():
                pass
            elif prec[i] <= prec[opStack.peek()]:
                postfixList.append(opStack.pop())
            opStack.push(i)
        else:
            if i == ')':
                while opStack.peek() != '(':
                    postfixList.append(opStack.pop())
                opStack.pop()
            else:
                postfixList.append(i)
            
    while not(opStack.isEmpty()) :
        postfixList.append(opStack.pop())
        
    return postfixList


def postfixEval(tokenList):
    
    ans = ArrayStack()
    
    for i in tokenList:
        if str(i) in '*/+-':
            a,b = ans.pop(), ans.pop()
            if i == '*':
                ans.push(b*a)
            elif i =='+':
                ans.push(b+a)
            elif i =='-':
                ans.push(b-a)
            else:
                ans.push(b/a)
            
        else:
            ans.push(i)
            
    return ans.peek()
    
                
def solution(expr):
    tokens = splitTokens(expr)
    postfix = infixToPostfix(tokens)
    val = postfixEval(postfix)
    return val
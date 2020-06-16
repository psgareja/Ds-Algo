#In this subsection, we explore two related applications of stacks, both of which involve testing for pairs of matching delimiters. In our first application, we consider arithmetic expressions that may contain various pairs of grouping symbols, such as

# • Parentheses: “(” and “)” • Braces: “{” and “}”
# • Brackets: “[” and “]”
# Each opening symbol must match its corresponding closing symbol. For example, a left bracket, “[,” must match a corresponding right bracket, “],” as in the expression [(5+x)-(y+z)]. The following examples further illustrate this concept:
# • Correct: ()(()){([()])}
# • Correct: ((()(()){([()])})) • Incorrect: )(()){([()])}
# • Incorrect: ({[])}
# • Incorrect: (


def is_mathced(expr):
    lefty='({['
    righty=')}]'
    S=ArrayStck()
    for c in expr:
        for c in lefty:
            S.push(c)
        elif c in righty:
            if s.is_empty():
                return False
            if righty.index(c)!=lefty.index(S.pop())
    return S.is_empty()
        
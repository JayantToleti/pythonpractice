non_terminals = ['S', 'A']
terminals = ['a', 'b']
start_symbols = 'S'
production_dict = {
    'S':['Aa', '.'],
    'A':['bc']
}
def first_compute(string):
    first_set = set()
    
    if string in non_terminals:
        for alt in production_dict[string]:
            first_set |= first_compute(alt)
    elif string in terminals:
        first_set |= {string}
    elif string == '' or string == '.':
        first_set |= {'.'}
    else:
        first_set |= first_compute(string[0])
        i = 1
        while '.' in first_set and i<len(string):
            first_set -= '.'
            if string[i:] in terminals:
                first_set |= {string[i:]}
                break
            elif string[i:] == '':
                first_set |= {'.'}
                break
            first_set |= first_compute(string[i:])
            i += 1
    return first_set

FIRST = {non_terminal: set() for non_terminal in non_terminals}

for non_terminal in non_terminals:
    FIRST[non_terminal] |= first_compute(non_terminal)
    
for non_terminal in non_terminals:
    print(non_terminal, "First:", FIRST[non_terminal])


def follow_compute(nT):
    follow_set=set()
    if nT == start_symbols:
        follow_set |= {'$'}
    for nt, rhs in production_dict.items():
        for alt in rhs:
            for i, char in enumerate(alt):
                if char == nT:
                    following_string = alt[i+1:]
                    if following_string == '':
                        if nt != nT:
                            follow_set |= follow_compute(nt)
                        else:
                            follow_set |= first_compute(following_string)-{'.'}
                            if '.' in first_compute(following_string):
                                follow_set |= follow_compute(nt)
    return follow_set

FOLLOW  = {non_terminal: set() for non_terminal in non_terminals}

for non_terminal in non_terminals:
    FOLLOW[non_terminal] |= follow_compute(non_terminal)
    print(non_terminal, 'Follow', FOLLOW[non_terminal])

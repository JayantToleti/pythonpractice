import os
def fix_recursion(grammar):
    new_grammar = {}
    for nt, prods in grammar.items():
        new_prods = []
        rec_prods = []
        for p in prods:
            if p.startswith(nt):
                rec_prods.append(p[1:] + nt)
            else:
                new_prods.append(p)
        if rec_prods:
            new_nt = nt + "'"
            new_grammar[nt] = [np + new_nt for np in new_prods]
            new_grammar[new_nt] = [rp + new_nt for rp in rec_prods] + ['@']
        else:
            new_grammar[nt] = prods
    return new_grammar

def fix_factoring(grammar):
    new_grammar = {}
    for nt, prods in grammar.items():
        pref = os.path.commonprefix(prods)
        if pref:
            new_nt = nt + "'"
            new_prods = [p[len(pref):] for p in prods if p.startswith(pref)]
            new_grammar[nt] = [pref + new_nt] + [p for p in prods if not p.startswith(pref)]
            new_grammar[new_nt] = new_prods
        else:
            new_grammar[nt] = prods
    return new_grammar

g = {
    'S': ['Bb', 'Cd'],
    'B': ['aB', '@'],
    'C': ['cC', '@']
}
fixed_g = fix_factoring(fix_recursion(g))
print("Fixed Grammar:")
print(fixed_g)
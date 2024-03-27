productions = {
    'S': ['Bb', 'Cd'],
    'B': ['aB', '@'],
    'C': ['cC', '@']
}

augmented = {'S\'': ['S']}
augmented.update(productions)

closure = {}
for nt, rhs in augmented.items():
    closure[nt] = [f'.{r}' for r in rhs]

for nt, rhs in closure.items():
    for r in rhs:
        print(f"{nt} -> {r}")
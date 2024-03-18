import ast


tree_ast = ast.parse('''
subjects = ['computer science', 'alorithm']
name = 'Ricky'
for sub in subjects:
    print('{} learn {}'.format(name, sub))
''')


print(ast.dump(tree_ast))
import ast

class BinOpTransformer(ast.NodeTransformer):
    def visit_BinOp(self, node):
        print(f"found BinOp at line: {node.lineno}")
        self.generic_visit(node)
        return node

code = """
left_op = 1
right_op = 2
sum_two_things = left_op + right_op
other_sum = sum_two_things - 1
print(sum_two_things)
print(other_sum)
"""

tree = ast.parse(code)

print("Original AST:")
print(ast.dump(tree))

transformer = BinOpTransformer()
transformed_tree = transformer.visit(tree)

print("\nTransformed AST:")
print(ast.dump(transformed_tree))

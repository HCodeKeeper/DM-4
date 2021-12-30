from pprint import pprint
from tools import *

matrix = [
    [1,0,1,0,1],
    [1,0,1,1,0],
    [0,1,0,0,1],
    [1,0,1,0,0],
    [1,0,0,0,0]
]

root = Tree("+", Tree("^", Tree("5"), Tree("2")), Tree("*", Tree("/", Tree("8"),Tree("2")),Tree("-",Tree("7"),Tree("4"))))
prefix = root.get_prefix(root)
postfix = root.get_postfix(root)

pprint(matrix)
print("Check if the graph is oriented")
is_oriented(matrix)
print()
print("Using the expression : 5^2 + 8/2 * (7-4)")
print("Polish Notation: ")
print(prefix)
Tree.count_prefix(prefix)
print()
print("Reversed Polish Notation: ")
print(postfix)
Tree.count_postfix(postfix)
print()

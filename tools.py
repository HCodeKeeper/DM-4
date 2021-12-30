
def _is_oriented(matrix : list):
    for i, arr in enumerate(matrix):
        for j, elem in enumerate(arr):
            if elem != matrix[j][i]:
                return False
    return True

class Tree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        self.straight = []
        self.reverse = []
    
    
    def get_prefix(self, tree):
        if (tree != None): #!
            self.straight.append(tree.value)
            self.get_prefix(tree.left)
            self.get_prefix(tree.right)
        return self.straight

    def get_postfix(self, tree):
        if tree != None:
            self.get_postfix(tree.left)
            self.get_postfix(tree.right)
            self.reverse.append(tree.value)
        return self.reverse

    def remove_element(chars, index): 
        #op num num
        del chars[index]
        del chars[index-1]
        del chars[index-2]
        return chars

    def evaluate(array, _exp, i):
        if len(array) >= 3:  
            exp = "".join(_exp)
            if "^" not in _exp:  
                answer = str(int(eval(exp)))
            else:
                answer = str(int(pow(int(_exp[0]), int(_exp[2])))) #thats scary
            print(f'{"".join(array)}\t{exp}' + f"={answer}")
            array = Tree.remove_element(array, i)
            array.insert(i-2, answer)
        return array



    def count_prefix( array : list):
        if len(array) < 3:
            print(array)
            return None
        #volatile numbers
        vol_n1 = None
        vol_n2 = None
        op = None #operator
        for i, elem in enumerate(array):
            try:
                int(elem)
                if op != None:
                    if vol_n1 != None:
                        vol_n2 = elem
                        break
                    else:
                        vol_n1 = elem
            except:
                if vol_n1 != None:
                    #rewrite with default values
                    vol_n1 = None
                    vol_n2 = None
                op = elem
        #evaluating, updating an array, recursion
        Tree.count_prefix(Tree.evaluate(array, [vol_n1, op, vol_n2], i))


    def count_postfix( array : list):
        if len(array) < 3:
            print(array)
            return None
        #volatile numbers
        vol_n1 = None
        vol_n2 = None
        op = None #operator
        for i, elem in enumerate(array):
            try:
                int(elem)
                if vol_n1 == None:
                    vol_n1 = elem
                else:
                    if vol_n2 == None:
                        vol_n2 = elem
                    else:
                        vol_n1 = vol_n2
                        vol_n2 = elem
            except:
                op = elem
                break
        #evaluating, updating an array, recursion
        Tree.count_postfix(Tree.evaluate(array, [vol_n1, op, vol_n2], i))



def is_oriented(matrix : list[list]):
    if not _is_oriented(matrix):
        print("Is oriented")
    else:
        print("Can be either oriented or disoriented ")
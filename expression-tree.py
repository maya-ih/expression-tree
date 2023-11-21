import sys

operators = ['+', '-', '*', '/', '//', '%', '**']

# Stack Class
# Purpose: Used by the Tree Class to keep track of parenthesis and operators.
class Stack (object):
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if(not self.is_empty()):
            return self.stack.pop()
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0


# Node Class
# Purpose: Used by the Tree Class to represent one operand or operators
#          in a binary expression. It includes data (a character) and
#          two pointers, to the left and right child nodes.
class Node(object):
    def __init__ (self, data = None, lChild = None, rChild = None):
        self.data = data
        self.lChild = lChild
        self.rChild = rChild


# Tree Class
# Purpose: To represent the string representation of operators and operands 
#          of a binary expression so it can be evaluated. 
class Tree (object):
    def __init__ (self):
        self.root = Node(None)
    
    # Input - String binary expression
    # Process - Converts the string to a binary expression tree representation
    # Output - The address of the root of the binary expression tree
    def create_tree (self, expr):
        
        # split expr into tokens
        tokens = expr.split()
        
        # convert operands to int or float
        for i in range(len(tokens)):
            if '.' in tokens[i]:
                tokens[i] = float(tokens[i])
            elif tokens[i].isdigit():
                tokens[i] = int(tokens[i])
        
        # create a stack to keep track of expressions and operators
        stack = Stack()
        
        # set current to the root
        current = self.root
        
        # process each token in the string
        for token in tokens:
            
            # left parenthesis
            if token == '(':
                current.lChild = Node(None)
                stack.push(current)
                current = current.lChild
            
            # operator
            elif token in operators:
                current.data = token
                stack.push(current)
                current.rChild = Node(None)
                current = current.rChild
            
            # operand
            elif type(token) == int or type(token) == float:
                current.data = token
                current = stack.pop()
            
            # right parenthesis
            elif token == ')':
                if not stack.is_empty():
                    current = stack.pop()
                
    # Input - Binary Expression Tree
    # Process - Evaluates tree nodes to arrive at algebraic result 
    # Output - Integer or double expression result
    def evaluate (self, aNode):
        # empty tree
        if aNode == None:
            return 0.0
        # not empty
        else:
            # recur on left and right subtrees
            left_subtree = self.evaluate(aNode.lChild)
            right_subtree = self.evaluate(aNode.rChild)
            
            # if node contains operand, return operand
            if type(aNode.data) == int or type(aNode.data) == float:
                return float(aNode.data)
            
            # if node contains operator, evaluate subtree
            elif aNode.data in operators:
                if aNode.data == operators[0]:
                    return float(left_subtree + right_subtree)
                elif aNode.data == operators[1]:
                    return float(left_subtree - right_subtree)
                elif aNode.data == operators[2]:
                    return float(left_subtree * right_subtree)
                elif aNode.data == operators[3]:
                    return float(left_subtree / right_subtree)
                elif aNode.data == operators[4]:
                    return float(left_subtree // right_subtree)
                elif aNode.data == operators[5]:
                    return float(left_subtree % right_subtree)
                elif aNode.data == operators[6]:
                    return float(left_subtree ** right_subtree)
        
    # Input - Binary Expression Tree
    # Process - Performs preorder traversal of tree
    # Output - String version of expression in preorder notation 
    def pre_order (self, aNode):
        expr = ''
        # empty tree
        if aNode == None:
            return ''
        # not empty - start at root and end at rightmost node
        else:
            expr += str(aNode.data) + ' '           # process current node
            expr += self.pre_order(aNode.lChild)    # process left subtree
            expr += self.pre_order(aNode.rChild)    # process right subtree
            return expr

    # Input - Binary Expression Tree
    # Process - Performs postorder traversal of tree
    # Output - String version of expression in postorder notation
    def post_order (self, aNode):
        expr = ''
        # empty tree
        if aNode == None:
            return ''
        # not empty - start at leftmost node and end at root
        else:
            expr += self.post_order(aNode.lChild)   # process left child
            expr += self.post_order(aNode.rChild)   # process right child
            expr += str(aNode.data) + ' '           # process parent
            return expr

# Do not change main(), except to change the debug flag before you submit.

def main():

    # Debug flag - set to False before submitting
    debug = False
    if debug:
        in_data = open('expression.in')
    else:
        in_data = sys.stdin
    
    # read infix expression
    line = in_data.readline()
    expr = line.strip()
 
    tree = Tree()
    tree.create_tree(expr)
    
    # evaluate the expression and print the result
    print(expr, "=", str(tree.evaluate(tree.root)))

    # get the prefix version of the expression and print
    print("Prefix Expression:", tree.pre_order(tree.root).strip())

    # get the postfix version of the expression and print
    print("Postfix Expression:", tree.post_order(tree.root).strip())

if __name__ == "__main__":
    main()

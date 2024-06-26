# A Node is basically a point of tree
# A Node has a value and a list of input_nodes.abs
# The value is the value of the node, and the childen represent
# the nodesthat lie below this one and their derivatives.
# A node without childern is a variable, while a node with input_nodes is
# an operation.

#This is intented to be used as default value for the evaluate function.
#If you created a lambda for evaluate, you would have 
#a lot of function doing the same thing, but occupied 
#more memory space.
def trivial_return(x):
    return x

"""Node class represents a node in a tree structure.

Attributes:
  value (any): The value stored in this node. 
  input_nodes (list): The child nodes below this node.
  evaluate (callable): The function to evaluate this node. Default is trivial_return.
"""
class Node:
    def __init__(self, value, input_nodes=[], evaluate=trivial_return):
        self.value = value
        self.input_nodes = input_nodes
        self.evaluate=evaluate

    def __add__(self,other):
        return add(self,other)
    
    def __mul__(self,other):
        return mul(self,other)
   
    def __neg__(self):
        return neg(self)

    def __sub__(self,other):
        return sub(self,other)
    
    def __pow__(self, other):
        return pow(self,other)

    def __truediv__(self,other):
        return div(self,other)

#auxiliary variables
One=Node(1)
NegOne=Node(-1)
Zero=Node(0)

from .BinaryOps import add, mul, sub, pow, div
from .UnaryOps import neg
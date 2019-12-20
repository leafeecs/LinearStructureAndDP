'''
Look at node_implementation.py, singly_linked_list.py and stack_ex.py together
'''

from singly_linked_list import SinglyLinkedList

class Stack(object):
    lstInstance = SinglyLinkedList()

    def pop(self):
        return self.lstInstance.removeAt(0)
    
    def push(self, value):
        return self.lstInstance.insertAt(value, 0)

stack = Stack()
stack.push('a')
stack.push('b')
stack.push('c')

print(stack.pop())
print(stack.pop())
print(stack.pop())

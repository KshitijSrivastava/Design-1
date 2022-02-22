"""
## Problem 2:
Design MinStack (https://leetcode.com/problems/min-stack/)
"""


class MinStack:

    def __init__(self):
        #Define both stack and min stack
        self.stack = []
        self.min_stack = []
        
    def isEmpty(self):
        #if the stack is empty
        return len(self.stack) == 0

    def push(self, val: int) -> None:
        #if stack is empty or if thew value is less than or equal to minimum element add to minstack
        if self.isEmpty() or val <= self.getMin():
            self.min_stack.append(val)
        #add the element to the stack
        self.stack.append(val)  

    def pop(self) -> None:
        #if the stack is empty return 
        if self.isEmpty():
            return
        # if the top of the stack is equal to the minimum element, pop the min_stack
        if self.top() == self.getMin():
            self.min_stack.pop()
        self.stack.pop()

    def top(self) -> int:
        #return the top of the stack, if stack is not empty
        if not self.isEmpty():
            return self.stack[-1]

    def getMin(self) -> int:
        # if the stack is not empty return the minimum element of the stack
        if not self.isEmpty():
            return self.min_stack[-1]
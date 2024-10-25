class Queue:
    def __init__(self):  # Corrected __init__ method
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

# Move infix_to_postfix outside Queue or make it a method within Queue
def infix_to_postfix(expression):  # Separate standalone function
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    output_queue = Queue()
    operator_stack = []

    for token in expression:
        if token.isalnum():
            output_queue.enqueue(token)
        elif token == '(':
            operator_stack.append(token)
        elif token == ')':
            while operator_stack and operator_stack[-1] != '(':
                output_queue.enqueue(operator_stack.pop())
            operator_stack.pop()  # Pop the '('
        else:  # token is an operator
            while operator_stack and precedence.get(operator_stack[-1], 0) >= precedence.get(token, 0):
                output_queue.enqueue(operator_stack.pop())
            operator_stack.append(token)

    while operator_stack:
        output_queue.enqueue(operator_stack.pop())

    postfix_expression = ""
    while not output_queue.is_empty():
        postfix_expression += output_queue.dequeue()

    return postfix_expression

infix_expression = str(input("Enter the infix expression: (a+b)*c-(d/e+f) "))
postfix_expression = infix_to_postfix(infix_expression)
print("Postfix expression:", postfix_expression)

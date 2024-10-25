#Evaluate Postfix notation

class Evaluate:

	# Constructor to initialize the class variables
	def __init__(self, capacity):
		self.top = -1
		self.capacity = capacity
		
		# This array is used a stack
		self.array = []

	# Check if the stack is empty
	def isEmpty(self):
		return True if self.top == -1 else False

	# Return the value of the top of the stack
	def peek(self):
		return self.array[-1]

	# Pop the element from the stack
	def pop(self):
		if not self.isEmpty():
			self.top -= 1
			return self.array.pop()
		else:
			return "$"

	# Push the element to the stack
	def push(self, op):
		self.top += 1
		self.array.append(op)

	# The main function that converts given infix expression
	# to postfix expression
	def evaluatePostfix(self, exp):

		# Iterate over the expression for conversion
		for i in exp:

			# If the scanned character is an operand
			# (number here) push it to the stack
			if i.isdigit():
				self.push(i)

			# If the scanned character is an operator,
			# pop two elements from stack and apply it.
			else:
				val1 = self.pop()
				val2 = self.pop()
				self.push(str(eval(val2 + i + val1)))

		return int(self.pop())



# Driver code
if __name__ == '__main__':
	exp = "231*+9-"
	obj = Evaluate(len(exp))
	
	# Function call
	print("postfix evaluation: %d" % (obj.evaluatePostfix(exp)))


'''
Evaluate a prefix expression


def is_operand(c):
    """
    Return True if the given char c is an operand, e.g. it is a number
    """
    return c.isdigit()


def evaluate(expression):
    """
    Evaluate a given expression in prefix notation.
    Asserts that the given expression is valid.
    """
    stack = []

    # iterate over the string in reverse order
    for c in expression[::-1]:

        # push operand to stack
        if is_operand(c):
            stack.append(int(c))

        else:
            # pop values from stack can calculate the result
            # push the result onto the stack again
            o1 = stack.pop()
            o2 = stack.pop()

            if c == '+':
                stack.append(o1 + o2)

            elif c == '-':
                stack.append(o1 - o2)

            elif c == '*':
                stack.append(o1 * o2)

            elif c == '/':
                stack.append(o1 / o2)

    return stack.pop()


# Driver code
if __name__ == "__main__":
    test_expression = "+9*26"
    print(evaluate(test_expression))

'''

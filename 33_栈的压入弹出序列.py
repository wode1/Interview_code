
'''
输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序。
假设压入栈的所有数字均不相等。
例如序列1,2,3,4,5是某栈的压入顺序，序列4，5,3,2,1是该压栈序列对应的一个弹出序列，
但4,3,5,1,2就不可能是该压栈序列的弹出序列。（注意：这两个序列的长度是相等的）
'''

class Solution(object):

	# 方法1
	def IsPopOrder(self, pushV, popV):
		if pushV==[] or popV==[]:
			return False 

		stack=[] # 辅助栈 
		for i in pushV:
			stack.append(i)
			if stack[-1]!=popV[0]:
				continue
			else:
				stack.pop()
				popV.pop(0)
		while len(stack)>0 and stack[-1]==popV[0]:
			stack.pop()
			popV.pop(0)
		if len(stack)==0: #   判断条件是辅助栈中空不空
			return True
		else:
			return False

	def IsPopOrder1(self, pushV, popV):
		if pushV==[] or popV==[]:
			return False 

		stack=[]
		for i in pushV:
			stack.append(i)
			if stack[-1]!=popV[0]:
				continue
			else:
				stack.pop()
				popV.pop(0)
		while len(stack)>0 and stack[-1]==popV[0]:
			stack.pop()
			popV.pop(0)

		if len(stack)==0:
			return True
		else:
			return False

	# 方法2 相对于1进行了优化
	def IsPopOrderO(self, pushV, popV):
		if pushV==[] or popV==[]:
			return False 
		stack=[] # 辅助栈
		for i in pushV:
			stack.append(i)
			while len(stack) and stack[-1]==popV[0]:
				stack.pop()
				popV.pop(0)
		if len(stack): # 判断条件是辅助栈中空不空
			return False 
		else:
			return True

	def IsPopOrderO1(self, pushV, popV):
		stack=[]
		if pushV==[] or popV==[]:
			return False 

		for i in pushV:
			stack.append(i)
			while len(stack) and stack[-1]==popV[0]:
				stack.pop()
				popV.pop(0)
				
		if len(stack):
			return False
		else:
			return True


pushV = [1, 2, 3, 4, 5]
popV = [4, 5, 3, 2, 1]
popVF = [4, 5, 2, 1, 3]
S = Solution()
print(S.IsPopOrderO(pushV, popVF))
print(S.IsPopOrderO(pushV, popV))







































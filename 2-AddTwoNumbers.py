class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        num1 = 0
        num2 = 0
        i = 0
        while True:
        	if l1 == None:
        		break
        	num1 += l1.val * (10 ** i)
        	i += 1
        	l1 = l1.next

        i = 0
        while True:
        	if l2 == None:
        		break
        	num2 += l2.val * (10 ** i)
        	i += 1
        	l2 = l2.next

        result = num1 + num2
        if result == 0:
        	return ListNode(0)

        li = []
        while result > 0:
        	node = ListNode(0)
        	node.val = result % 10
        	node.next = None
        	result /= 10
        	li.append(node)

        for i in range(len(li) - 1):
        	li[i].next = li[i+1]

        return li[0]

if __name__ == '__main__':
    l1_1 = ListNode(0)
    #l1_2 = ListNode(4)
    #l1_3 = ListNode(3)
    #l1_1.next = l1_2
    #l1_2.next = l1_3

    l2_1 = ListNode(0)
    #l2_2 = ListNode(6)
    #l2_3 = ListNode(4)
    #l2_1.next = l2_2
    #l2_2.next = l2_3


    l3_1 = Solution().addTwoNumbers(l1_1,l2_1)
    
    while l3_1 != None:
        print l3_1.val
        l3_1 = l3_1.next





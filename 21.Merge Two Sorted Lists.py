class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        arr = []
        if l1 == None and l2 == None:
            return None
        if l1 == None and l2 != None:
            return l2 
        if l2 == None and l1 != None:
            return l1

        while True:
            if l1 == None:
                while l2 != None:
                    arr.append(ListNode(l2.val))
                    l2 = l2.next
                break
                
            if l2 == None:
                while l1 != None:
                    arr.append(ListNode(l1.val))
                    l1 = l1.next
                break

            if l1.val < l2.val:
                arr.append(ListNode(l1.val))
                l1 = l1.next
            else:
                arr.append(ListNode(l2.val))
                l2 = l2.next

        for i in range(len(arr) - 1):
            arr[i].next = arr[i+1]

        return arr[0]



if __name__=='__main__':
    l1_1 = ListNode(-9)
    l1_2 = ListNode(3)
    #l1_3 = ListNode(5)
    l1_1.next = l1_2
    #l1_2.next = l1_3

    l2_1 = ListNode(5)
    l2_2 = ListNode(7)
    #l2_3 = ListNode(6)
    l2_1.next = l2_2
    #l2_2.next = l2_3
    
    l3 = Solution().mergeTwoLists(l1_1, l2_1)
    print "---------------"
    while l3 != None:
        print l3.val
        l3 = l3.next



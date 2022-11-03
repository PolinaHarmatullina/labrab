class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        arr = []
        new_list = head
        new_list_head = head
        while head != None:
            if head.val != val:            
                arr.append(head.val)
            head = head.next
        for i in range(len(arr)):
            new_list.val = arr[i]
            if(i == len(arr) - 1):
                new_list.next = None
            else:
                new_list = new_list.next
        if len(arr) == 0:
            new_list_head = None
        return new_list_head
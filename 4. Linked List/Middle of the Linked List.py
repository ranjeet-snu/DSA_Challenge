class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        self.count=0
        self.mid=0
        self.li=[]
        n=head
        while n!=None:
            self.count+=1
            n=n.next
        if self.count%2==0:
            self.mid=int((self.count+2)/2)
        else:
            self.mid=int((self.count+1)/2)
        
        self.c=1
        m=head
        while m!=None:
            if self.c==self.mid:
                #self.li.append(m.val)
                head=m
            self.c+=1
            m=m.next
        
        return head
        

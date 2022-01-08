'''A critical point in a linked list is defined as either a local maxima or a local minima.

A node is a local maxima if the current node has a value strictly greater than the previous node and the next node.

A node is a local minima if the current node has a value strictly smaller than the previous node and the next node.

Note that a node can only be a local maxima/minima if there exists both a previous node and a next node.

Given a linked list head, return an array of length 2 containing [minDistance, maxDistance] where minDistance is the minimum distance between any two distinct critical points 
and maxDistance is the maximum distance between any two distinct critical points. If there are fewer than two critical points, return [-1, -1].

Example 1:


Input: head = [3,1]
Output: [-1,-1]
Explanation: There are no critical points in [3,1].'''

class Solution:
    def nodesBetweenCriticalPoints(self, head):
        n=head
        
        list1=[]
        
        while n!=None:
            list1.append(n.val)
            n=n.next
            
        length=len(list1)
        
        if length==1 or length==2:
            return [-1,-1]
        else:
            list_min=[]
            list_max=[]
            
            for i in range(1,length-1):
                if list1[i]>list1[i-1] and list1[i]>list1[i+1]:
                    list_max.append(i)
                elif list1[i]<list1[i-1] and list1[i]<list1[i+1]:
                    list_min.append(i)
             
            if list_min==[] and list_max==[]:
                return [-1,-1]
            else:
                minimum=9999999999
                maximum=-999999999
                
                list_max.extend(list_min)
                list_max.sort()
                
                length2=len(list_max)
                if length2<2:
                    return [-1,-1]
                
                maximum=max(maximum,abs(list_max[0]-list_max[-1]))
                
                for i in range(length2-1):
                        minimum=min(minimum,abs(list_max[i]-list_max[i+1]))
                        
                        
                if minimum==9999999999 and maximum==-999999999:
                    return [-1,-1]
                else:
                    return [minimum,maximum]

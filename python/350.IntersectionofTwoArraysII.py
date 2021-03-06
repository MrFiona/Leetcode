class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        table={}
        result = []
        for n in nums1:
            if n in table:
                table[n]+=1
            else:
                table[n]=1
        for n in nums2:
            if n in table: 
                if table[n]>0:
                    result+=[n]
                    table[n]-=1
        return result

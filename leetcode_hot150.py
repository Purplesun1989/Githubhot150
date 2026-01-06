from typing import List

class Solutions:

    def Merge_Sorted_Array(self, nums1: List[int], m: int, nums2: List[int], n: int):
        if n == 0:
            return
        p  = m + n -1
        p1 = m-1
        p2 = n-1
        while(p!=-1 and p2!=-1):
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1-= 1
                p -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
                p -= 1

            if p1 == -1:
                for i in range(0,p+1):
                    nums1[i] = nums2[i];
                break;

    def Remove_Element(self, nums: List[int], val: int):
        l = len(nums)
        k = 0;
        if l == 0:
            return
        s = 0;
        f = 0;
        while(f < l):
            if(nums[f] != val):
                nums[s] = nums[f]
                f+=1;
                s+=1;
            else:
                k+=1
                f+=1
        return l-k
    def leetcode26(self, nums: List[int]):
        l = len(nums);
        if l == 0:
            return 0;
        s = 0
        f = s+1

        while(f < l):
            if(nums[s] == nums[f]):
                f+=1

            else:
                s+=1;
                nums[s] = nums[f]
                f+=1
        return s+1








if __name__ == "__main__":
    sol = Solutions()
    # n1 = [1]
    # sol.Merge_Sorted_Array(n1, 1, [], 0)
    # print(f"Test 1 Result: {n1}")
    # print(sol.Remove_Element([3,2,2,3],3))
    print(sol.leetcode26([0,0,1,1,1,2,2,3,3,4]))







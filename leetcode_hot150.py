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

    def leetcode80(self, nums: List[int]):
        l = len(nums)
        if l<3 :
            return l;

        f = 2
        s = 2
        # f s are 2 pointers starts at index 2, indicates we neglect first 2 elements as they always remain ;
        # Always start the pointer at same position;
        while(f < l):
            if nums[f] == nums[s-2]:
                # Decide if we meet a triple repetition;
                f+=1;
                # forward f pointer to find the first none repetition elements;
            else:
                nums[s] = nums[f]
                # Over-write the current s pointer as we include the element;
                f+=1
                s+=1
                # Forward f and s together
        return s;

    def leetcode169(self, nums: List[int]):
        count = 0;
        # count the number of current candidate
        # if this goes zero then we induce that the number of current candidates isn't n/2
        candidate = 0;
        for n in nums:
            if count == 0:
                candidate = n
            # change candidate
            if candidate == n:
                count += 1
            else:
                count -= 1

        return candidate

    def leetcode189(self, nums: List[int], k: int):

        l = len(nums)
        k %= l

        nums[:] =  nums[l-k:] +  nums[:l-k]
        # list[:a] for all first ath elements
        # list[a:] for all elements after ath elements
        # list[:-a] last a elements
        # list[-a:] all but last k

        return nums

    def leetcode121(self, prices: List[int]):
        if not prices:
            return 0

        min_price = float('inf')
        max_profit = 0

        for n in prices:

            profit = n - min_price
            if n < min_price:
                min_price = n

            if max_profit < profit:
                max_profit = profit

        return max_profit

    def leetcode122_dp(self, prices: List[int]):
        if not prices:
            return 0

        past_sold = 0
        past_buyin = -prices[0]

        for p in prices:
            # 状态转移方程为：
            # 每一天都有两种状态 即：
            # 1.手中没有股票：按照今天的价格，把股票全部出掉了 或者 之前就已经清仓 今天没有补货
            # 2.手中持有股票：按照今天的价格，购入了股票，或者 之前就有持仓 今天没有卖出
            # 两种状态同时记录 都选取每种状态对应的两种情况中 盈利最多的计入状态方程
            # 我们只需要维护 past_sold past_buyin即可

            past_sold = max(past_sold, p + past_buyin)
            past_buyin = max(past_buyin, past_sold - p)

        return past_sold

    def leetcode122_greedy(self, prices: List[int]):

        if not prices:
            return 0

        r = 0
        f = 1
        l = len(prices)
        balance = 0
        while f < l:
            if prices[f] > prices[r]:
                balance += prices[f] - prices[r]
            #     只要第二天比第一天的价格高 我们就在第一天买入 第二天卖出

            f+=1
            r+=1
        return balance

    def leetcode55_dp(self, nums: List[int]):
        l = len(nums)
        dp = [-1] * l
        dp[0] = 1
        # 转移方程为：
        # 如果 当前位置的之前某一位可达到
        # 并且 这一位可以跳到当前位置
        # 那么 当前位置也可以达到
        for i in range(1,l):
            for j in range (i):
                if dp[j] == 1 and nums[j] + j >= i:
                    dp[i] = 1
                    break
        return dp[l-1]==1

    def leetcode55_greedy(self, nums: List[int]):

        l = len(nums)
        flag = False
        cover = nums[0]
        # cover即当前位置的覆盖范围
        i = 0;
        while i <= cover:

            if i+nums[i] > cover:
                cover = i+nums[i]
            #    如果当前位置的覆盖范围更大 我们更新覆盖范围
            if cover >= l-1:
                flag = True
                # 如果 最后一位落在当前的覆盖范围中 我们认为最后一位可以达到
                break
            i+=1

        return flag









if __name__ == "__main__":
    sol = Solutions()
    # n1 = [1]
    # sol.Merge_Sorted_Array(n1, 1, [], 0)
    # print(f"Test 1 Result: {n1}")
    # print(sol.Remove_Element([3,2,2,3],3))
    # print(sol.leetcode26([0,0,1,1,1,2,2,3,3,4]))
    # print(sol.leetcode80([1,1,1,2,2,3]))
    # print(sol.leetcode169([1,2,2,2,2,3]))
    # print(sol.leetcode189([1,2,3,4,5,6,7,8,9],3))
    # print(sol.leetcode121([7,1,5,3,6,4]))
    # print(sol.leetcode122_greedy([5,4,3,2,1]))
    # print(sol.leetcode122_dp([7,1,5,3,6,4]))
    # print(sol.leetcode55_dp([3,2,1,0,4]))
    # print(sol.leetcode55_greedy([0,1]))







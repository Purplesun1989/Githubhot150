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

    def leetcode134(self, gas: List[int], cost: List[int]):

        cur_sum = 0
        start_at = 0

        if sum(gas) < sum(cost):
            return -1
        #如果整体来讲是加油大于消耗油，那么就一定存在一个起始点 可以anticlock遍历所有的点一圈

        for i in range(len(gas)):
            surplus = gas[i] - cost[i]
            #计算在本点加油后 出发下一个点 油箱的盈余
            cur_sum += surplus
            #如果油箱为空甚至为负，那么就认为 从目前的起始点 是无法到达本点的
            if cur_sum < 0:
                start_at = i + 1
                cur_sum = 0
                #所以 重置当前的start_at 为当前节点+1

        return start_at

    def leetcode135(self, ratings: List[int]):
        res = [1]*len(ratings)
        l = len(ratings)
        for i in range(1,l):
            if ratings[i] > ratings[i-1]:
                # 从左往右遍历，如果next比当前大，那么就给下一个增1
                res[i] = res[i-1] + 1

        for i in range(l-1,0,-1):
            if ratings[i-1] > ratings[i]:
                # 从右往左遍历，如果下一个比当前的大，那么就取 当前自增1 和 下一个 中较大的哪个
                res[i-1] = max(res[i]+1,res[i-1])


        return sum(res)

    def leetcode13(self, s: str):

        my_hash = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        res  = 0
        for i in range(len(s)-1) :
            if(my_hash[s[i]] < my_hash[s[i+1]]):
                res -= my_hash[s[i]]

            else:
                res += my_hash[s[i]]

        res += my_hash[s[-1]]

        return res

    def leetcode42(self, height: List[int]):
        l = len(height)
        r_max = [0]*l
        l_max = [0] * l
        # 利用前缀法的思路,lmax记录当前index之前最大的数,rmax记录当前index之后最大的数

        res = 0
        for i in range(1,l):
            l_max[i] = max(height[i-1],l_max[i-1])
        #     查找当前下标之前最大的数

        for i in range(l-2,-1,-1):
            r_max[i] = max(height[i+1],r_max[i+1])
        #     查找当前下标之后最大的数

        for i in range(l):
            diff = min(l_max[i],r_max[i]) - height[i]
            # 当前下标上能存储的雨水,取决于左最大和右最大中比较小的那一个与当前下标高度做diff
            if diff > 0:
                res += diff
        return res

    def leetcode42_rearrange(self, height: List[int]):
        # 这个绝妙的解法利用了两次加法的交换率 即 (a+b) + (c+d) = a+d + c + b
        l = len(height)
        r_max = height[-1]
        l_max = height[0]
        sum = 0
        for i in range(0,l):
            # 每个index可以积蓄的雨水,等同于左边最大与右边最大中较小者与当前index的高度做差
            # 整个数组可以积蓄的雨水,等同于每个点积蓄的雨水之和
            # 也就是 total = sum(Wi) = sum(min(lmax,rmax)-height[i])
            # 由数学定义 min(lmax,rmax) = lmax + rmax -max(lmax,rmax)
            # 那么 total = sum(lmax + rmax -max(lmax,rmax)-height[i])
            l_max = max(l_max,height[i])
            r_max = max(r_max,height[l-1-i])
            sum += r_max + l_max -height[i]
            # sum(lmax + rmax -height[i]) 中lmax和rmax可以由加法交换律 任意匹配 也就是
            # index为1 的lmax 可以与 index 为len-1-1的rmax相结合 这样的好处是可以用一个正向循环把lmax和 rmax同时维护
        return sum - l* r_max
            # max(lmax,rmax) 一定等于全数组最大值,即gmax,借此 我们可以使用加法交换律提出每一个点上的max(lmax,rmax) 为gmax
            # 即 total = sum(lmax + rmax -height[i]) - len*gmax

    def leetcode12(self, num: int):
        roman_map = {
            # 个位 (Ones)
            1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V',
            6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX',0:"",

            # 您跳过了十位 (10-90)，为了完整性我补在这里，如果不需要可以删除
            10: 'X', 20: 'XX', 30: 'XXX', 40: 'XL', 50: 'L',
            60: 'LX', 70: 'LXX', 80: 'LXXX', 90: 'XC',

            # 百位 (Hundreds)
            100: 'C', 200: 'CC', 300: 'CCC', 400: 'CD', 500: 'D',
            600: 'DC', 700: 'DCC', 800: 'DCCC', 900: 'CM',

            # 千位 (Thousands) - 标准写法通常截止于 3000 (MMM)
            1000: 'M',
            2000: 'MM',
            3000: 'MMM',
        }
        res = ""
        dvd = 1000
        while dvd >= 1:
            res += roman_map[(num//dvd)*dvd]
            num %= dvd
            dvd /= 10

        return res





if __name__ == "__main__":
    sol = Solutions()
    # sol.Merge_Sorted_Array([1] 1, [], 0)
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
    # print(sol.leetcode134([1,2,3,4,5],[3,4,5,1,2]))
    # print(sol.leetcode135([1,3,2,2,1]))
    # print(sol.leetcode13("MCMXCIV"))
    # print(sol.leetcode42([4,2,0,3,2,5]))
    # print(sol.leetcode42_rearrange([4,2,0,3,2,5]))
    print(sol.leetcode12(58))








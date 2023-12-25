class Solution(object):
    def isAble(self, s):
        if int(s) <= 26 and int(s) > 0:
            return True
        return False

    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s[0] == "0":
            return 0

        ways = [[s[0]]]
        for i in range(1, len(s), 1):
            tempWays = []
            print(ways)
            countAble = 0
            for way in ways:
                lastChar = way[len(way)-1]

                # print(lastChar)
                # print(s[i])
                # print(way)
                comb = lastChar + s[i]
                if self.isAble(comb):
                    tempWay = way.copy()
                    tempWay[len(way)-1] = comb

                    countAble += 1
                    tempWays.append(tempWay)
                
                if self.isAble(s[i]):
                    tempWay = way.copy()
                    tempWay.append(s[i])

                    countAble += 1
                    tempWays.append(tempWay)
                
            if countAble == 0:
                return 0
            
            print(tempWays)
            print()
            ways = tempWays
        
        return len(ways)

p = Solution()
print(p.numDecodings("11106"))


                



# 2266
# 2 (266)
# 2 2 (66)
# [2, 22] (66)
# [2, 22] 6 (6)
# [2 2 6, 22 6, 2 26] 6
# [2 2 6 6, 22 6 6, 2 26 6]

# 21211
# 2 (1211)
# [2] 1 (211)
# [2 1, 21] 2 (11)
# [2 1 2, 2 12, 21 2] 1 (1)
# [2 1 2 1, 2 12 1, 21 2 1, 21 21] 1
# [2 1 2 1 1, 2 1 2 11, 2 12 1 1, 2 12 11, 21 2 1 1, 21 2 11, 21 21 1]


# 22

# 2 26 6
# 2 2 6 6
# 22 6 6
        
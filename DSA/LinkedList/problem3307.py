class Solution:
    noOf0 = 1
    word = "a"
    l1 = 0
    l0 = 0
    def kthCharacter(self, k: int, operations) -> str:
        for i in operations:
            print(i)
            if i == 0:
                self.copy()
            else:
                self.update()
        print(Solution.word)
        return Solution.word[k]

    def copy(self):
        Solution.noOf0 += 1
        Solution.l0 = len(Solution.word)
        Solution.word += Solution.word
        print(Solution.word)

    def update(self):
        if (Solution.l1 == 0):

        curr = len(Solution.word)
        print('curr: ',curr)
        new_segment = Solution.word[Solution.l1:Solution.l0]
        print('new segment: ',new_segment)
        updated = self.actUpd(new_segment)
        combined = new_segment + updated
        Solution.word += combined * Solution.noOf0
        print(Solution.word)
        Solution.l1 = curr

    def actUpd(self, s):
        res = ''
        for j in s:
            if j == 'z':
                res += 'a'
            else:
                res += chr(ord(j) + 1)
        return res
s = Solution()
s.kthCharacter(10, [0, 1, 0,1])
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        res1 = []
        for i in range(len(strs)):
            target = "".join(sorted(strs[i]))
            if target not in hashmap:
                hashmap[target] = []
            hashmap[target].append(strs[i])

            

        return (list(hashmap.values()))



        
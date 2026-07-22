class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for word in strs:

            signature = "".join(sorted(word))
            
            # 2. Check if the signature drawer exists in our cabinet yet
            if signature not in hashmap:

                hashmap[signature] = []
                
            # 3. Add the original word to the list inside that drawer
            hashmap[signature].append(word)
            
        # 4. Return all the lists grouped together 
        # (hashmap.values() grabs just the values, ignoring the keys)
        return list(hashmap.values())
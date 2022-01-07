class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dict_s = defaultdict(list)
        dict_t = defaultdict(list)

        for i in range(len(s)):
            dict_s[s[i]].append(i)
            dict_t[t[i]].append(i)

        return sorted(list(dict_s.values())) == sorted(list(dict_t.values()))

        

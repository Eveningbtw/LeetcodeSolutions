class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list) # Mapping character count to list of anagrams

        for string in strs:
            count = [0] * 26 # a . . . z

            for char in string:
                count[ord(char) - ord("a")] += 1

            hashMap[tuple(count)].append(string)

        return list(hashMap.values())
public class Solution {
    public IList<IList<string>> GroupAnagrams(string[] strs) {
        var hashMap = new Dictionary<string, List<string>>();
        
        foreach (var str in strs) {
            // Count characters
            int[] count = new int[26];
            foreach (char c in str) {
                count[c - 'a']++;
            }

            // Build a key string from count array
            string key = string.Join("#", count);

            // Add to dictionary
            if (!hashMap.ContainsKey(key)) {
                hashMap[key] = new List<string>();
            }
            hashMap[key].Add(str);
        }

        // Convert dictionary values to result list
        var result = new List<IList<string>>();
        foreach (var group in hashMap.Values) {
            result.Add(group);
        }
        
        return result;
    }
}
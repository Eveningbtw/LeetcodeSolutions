public class Solution {
    public bool IsAnagram(string s, string t) {

    if (s.Length != t.Length){
        return false;
    }

    return String.Concat(s.OrderBy(c => c)) == String.Concat(t.OrderBy(c => c));
    }
}
public class Solution {
    public bool ContainsDuplicate(int[] nums) {
        HashSet<int> hashset = new HashSet<int>();
        foreach (int num in nums)
        {
            if (hashset.Contains(num))
            {
                return true;
            }

            hashset.Add(num);
        }

        return false;
    }
}
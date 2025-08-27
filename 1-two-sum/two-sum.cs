public class Solution
{
    public int[] TwoSum(int[] nums, int target)
    {
        Dictionary<int, int> map = new Dictionary<int, int>(); // value -> index mapping

        for (int i = 0; i < nums.Length; i++)
        {
            int difference = target - nums[i];
            if (map.ContainsKey(difference))
            {
                return new int[] { map[difference], i };
            }
            if (!map.ContainsKey(nums[i]))  // To avoid overwriting the first index
            {
                map[nums[i]] = i;
            }
        }
        
        return Array.Empty<int>(); // return empty array if no solution
    }
}
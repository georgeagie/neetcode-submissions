class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> occurences = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (occurences.containsKey(complement)) {
                return new int[] {occurences.get(complement), i};
            }
            occurences.put(nums[i], i);
        }

        return new int[] {};
    }
}

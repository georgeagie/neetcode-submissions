class Solution {
    public int trap(int[] height) {
        int left = 0;
        int right = height.length - 1;
        int maxLeft = height[left];
        int maxRight = height[right];
        int result = 0;
        while (left < right) {
            if (maxLeft > maxRight) {
                right--;
                maxRight = Math.max(maxRight, height[right]);
                int water = maxRight - height[right];
                if (water > 0) result += water;
            } else {
                left++;
                maxLeft = Math.max(maxLeft, height[left]);
                int water = maxLeft - height[left];
                if (water > 0) result += water;
            }
        }
        return result;
    }
}

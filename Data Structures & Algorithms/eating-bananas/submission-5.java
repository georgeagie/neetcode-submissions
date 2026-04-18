class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        int left = 1;
        int right = 0;
        for (int pile: piles) {
            right = Math.max(right, pile);
        }
        int result = right;
        while (left <= right) {
            int rate = (left + right) / 2;
            long count = 0;
            for (int pile: piles) {
                count += (int) Math.ceil((double) pile / rate);
            }
            if (count <= h) {
                result = rate;
                right = rate - 1;
            } else {
                left = rate + 1;
            }
        }
        return result;
    }
}


class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> hm = new HashMap<>();
        for (int num: nums) {
            if (hm.containsKey(num)) {
                hm.put(num, hm.get(num) + 1);
            } else {
                hm.put(num, 1);
            }
        }
        ArrayList<int[]> arr = new ArrayList<>();
        for (Map.Entry<Integer, Integer> entry: hm.entrySet()) {
            arr.add(new int[] {entry.getValue(), entry.getKey()});
        } 
        arr.sort((a, b) -> b[0] - a[0]);
        int[] result = new int[k];
        for (int i = 0; i < result.length; i++) {
            result[i] = arr.get(i)[1];
        }
        return result;
    }
}

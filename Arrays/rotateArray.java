package SiddhantSinghDSA.Arrays;

public class rotateArray {
    public void rotate(int[] nums, int k) {
        int[] result = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            result[(i + k) % nums.length] = nums[i];
        }
        for (int i = 0; i < nums.length; i++) {
            nums[i] = result[i];
        }
    }

    /*
     * Input: nums = [1,2,3,4,5,6,7], k = 3
     * Output: [5,6,7,1,2,3,4]
     * Explanation:
     * rotate 1 steps to the right: [7,1,2,3,4,5,6]
     * rotate 2 steps to the right: [6,7,1,2,3,4,5]
     * rotate 3 steps to the right: [5,6,7,1,2,3,4]
     * 
     * Algorithm:
     * 1-Sabse pehle poore array ko rotate karo.
     * [7 6 5 4 3 2 1]
     * 2- Fir 0th index to K-1 tak reverse karo
     * 3-Fir K to arr.length-1 tak rreverse karo
     * [5 6 7 4 3 2 1]
     * [5 6 7 1 2 3 4]
     * 
     * 
     */

    public void rotateArraySecond(int[] nums, int k) {
        k %= nums.length;
        reverse(nums, 0, nums.length - 1);
        reverse(nums, 0, k - 1);
        reverse(nums, k, nums.length - 1);
    }

    // Reverse using Recursion
    public void reverse(int[] nums, int start, int end) {
        if (start <= end)
            return;
        int temp = nums[start];
        nums[start] = nums[end];
        nums[end] = temp;
        reverse(nums, start + 1, end - 1);
    }

    public void rotateImage(int[] nums, int k) {
        k %= nums.length;
        reverse(nums, 0, nums.length - 1);
        reverse(nums, 0, k - 1);
        reverse(nums, k, nums.length - 1);
    }

    public void reverseArray(int[] nums, int start, int end) {
        while (start <= end) {
            int swap = nums[start];
            nums[start] = nums[end];
            nums[end] = swap;
            start++;
            end--;
        }
    }
}

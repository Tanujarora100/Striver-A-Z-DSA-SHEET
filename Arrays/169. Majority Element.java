package SiddhantSinghDSA.Arrays;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class majorityElementProblem {
    public int majorityElement(int[] nums) {
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            map.put(nums[i], map.getOrDefault(nums[i], 0) + 1);
        }
        int majorityElement = Integer.MIN_VALUE;
        for (Map.Entry<Integer, Integer> entry : map.entrySet())
            if (entry.getValue() > nums.length / 2)
                majorityElement = entry.getKey();

        return majorityElement;
    }

    public int majorityElementusingVotingApproach(int[] nums) {
        int vote = 0;
        int candidate = nums[0];
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == candidate)
                vote++;
            else
                vote--;
            if (vote <= 0) {
                candidate = nums[i];
                vote = 1;
            }
        }
        return candidate;
    }

    public int majorityElementUsingSorting(int[] nums) {
        Arrays.sort(nums);
        return nums[nums.length / 2];
    }

}

// https://leetcode.com/problems/running-sum-of-1d-array/description/
public class RunningSumOf1dArray {
    class Solution {
        public int[] runningSum(int[] nums) {
            int[] newArr = new int[nums.length];
            newArr[0] = nums[0];

            for(int i =1; i<nums.length ; i++){
                newArr[i] = nums[i] + newArr[i-1];
            }
            return newArr;

        }
    }
}

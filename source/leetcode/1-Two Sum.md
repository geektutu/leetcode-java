### [Two Sum](https://leetcode.com/problems/two-sum/)

> Given an array of integers, return indices of the two numbers such that they add up to a specific target. <br/>
> You may assume that each input would have exactly one solution.

题目大意：给定一个数组，和一个目标值，找出数组中相加恰好等于目标值的2个数的下标，结果只有1个

题目难度：Easy

```java
import java.util.Arrays;
/**
 * Created by gzdaijie on 16/5/1.
 * 从大到小排序，首先将首尾相加，首尾指针start，end初始化为0， len-1
 * 如果和小于目标值，++start，大于目标值，--end
 * 复杂度 O(NlgN)
 */
public class Solution {
    public int[] twoSum(int[] nums, int target) {
        int len = nums.length;
        int start = 0, end = len - 1;
        int[] origin_nums = (int[])nums.clone();
        Arrays.sort(nums);
        while (start < end) {
            int t = nums[start] + nums[end];
            if(t < target){
                ++start;
            } else if(t > target) {
                --end;
            } else {
                break;
            }
        }

        start = nums[start];
        end = nums[end];

        int[] result = new int[2];
        int index = 0;
        for (int i = 0; i < len; i++) {
            if(origin_nums[i] == start || origin_nums[i] == end) {
                result[index++] = i;
                if (index == 2)break;
            }
        }
        return result;
    }
}

```
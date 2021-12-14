class Solution {
    //returns the count of numbers smaller than tbe element at idx
    public static int findCount(int [] nums ,int idx){
        int count = 0;
        for(int i = 0; i < nums.length; i++){
            if(i == idx)
                continue;
            if(nums[i] <  nums[idx])
                count++;
        }
        return count;
    }

    public int[] smallerNumbersThanCurrent(int[] nums) {
        int [] count = new int [nums.length];
        for(int i = 0; i < nums.length; i++){
            count[i] = findCount(nums,i);
        }
        return count;
    }
}

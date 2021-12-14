class Solution {

    //insertion Sort
    public void insertionSort(int [] nums ){
        int outr,innr,temp;
        for(outr = 1; outr < nums.length; outr++){
            innr = outr;
            temp = nums[outr];
            while(innr > 0 && nums[innr - 1] > temp){
                nums[innr] = nums[innr - 1];
                innr--;
            }
            nums[innr] = temp;
        }
    }
    public void sortColors(int[] nums) {
        insertionSort(nums);
    }
}

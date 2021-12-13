class Solution {
    public List<Integer> targetIndices(int[] nums, int target) {
        List<Integer> ls = new ArrayList<>();
        int min = 0;
        for(int i = 0; i < nums.length  - 1; i++){
            min = i;
            for(int j = i + 1; j < nums.length; j++){
                if(nums[min] > nums[j])
                    min = j;
            }
            int minValue = nums[min];
            nums[min] = nums[i];
            nums[i] = minValue;
        }

        int k ;
        for(k = 0 ; k < nums.length; k++){
            if(nums[k] == target)
                break;
        }

        if(k == nums.length)
            return ls;
        while(k < nums.length && nums[k] == target )
            ls.add(k++);
        return ls;



    }

}

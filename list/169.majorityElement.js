var majorityElement = function(nums) {
    // math
    if (nums.length == 1){
        return nums[0]
    };
    nums = nums.sort()
    console.log(nums)
    middle = nums.length/2
    console.log(middle)
    idx = Math.floor(middle)
    return nums[idx]
};

var n = [6,4,5,6]
majorityElement(n)

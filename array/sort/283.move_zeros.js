var moveZeroes = function(nums) {
    var count = 0
    for (let i=0; i < nums.length; i++){
        if (nums[i] == 0){
            count += 1
            continue
        }
        // 将非零数字放到最前面
        nums[i-count] = nums[i]
    }
   // 增加0到非零数字后
    for (let i = count; i > 0 ; i--){
        nums[nums.length-i] = 0
    }
};
/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
// var moveZeroes = function(nums) {
//     var count = 0
//     for (let i=0; i < nums.length; i++){
//         if (nums[i] == 0){
//             count += 1
//             continue
//         }
//         // 将非零数字放到最前面
//         nums[i-count] = nums[i]
//     }
//    // 增加0到非零数字后
//     for (let i = count; i > 0 ; i--){
//         nums[nums.length-i] = 0
//     }
// };

var moveZeroes = function(nums) {
    var c = 0
    for (let i=0; i< nums.length; i++) {
        // i-c: 指针左移
        // 比如: [0,1,0,3,12], 当i=4时, 数组变为 [1,3,12,0,0], i-c=2, nums[2]=12
        if(nums[i - c] == 0) {
            nums.splice(i - c, 1)
            nums.push(0)
            c++
        }
    }
};
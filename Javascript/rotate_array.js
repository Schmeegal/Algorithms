//use the length of the array to find out simplest k to rotate
//ex: if array.length() = 5 and k is 103, 103%5 = 3 so only need to perform 3 rotations
// if k == array.length(), return array

//brute force method - T O(n), S O(k)
//take k elements from the end and store in temp array
//shift elements in array k elements
//place temp array at beginning of the array
/*
const rotateArray = function (array,k){
    const length = array.length;
    k=k%length;
    const temp = array.slice(length-k); //slice is O(k) where k = end-start
    for(let i = length-k-1; i >= 0; i--){
        array[i+k] = array[i];
    }
    for(let i=0; i < k; i++){
        array[i]=temp[i];
    }
    return array;
}

array = [1,2,3,4,5];
console.log(rotateArray(array, 6));
*/

//correct solution - T O(n), S O(1)

const reverse = function(nums, start,end){
    while (start < end){
        [nums[start], nums[end]] = [nums[end], nums[start]];
        start++;
        end--;
    }
}

const rotate = function(nums, k){
    k = k%nums.length; //k=102, length =5, rotations
    //nums.reverse();
    reverse(nums, 0, nums.length-1);
    //start =0, end =k-1
    reverse(nums,0,k-1);
    //start =k, end =length-1
    reverse(nums, k, nums.length-1);
    return nums;
}

console.log(rotate([1,2,3,4,5,6], 6));
console.log(rotate([1,2,3,4,5,6], 3));
console.log(rotate([1,2,3,4,5,6], 1));
console.log(rotate([1,2,3,4,5,6], 4));
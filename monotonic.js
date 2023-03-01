//MD - non increasing, as you traverse array[i] >= array[i+1]
//MI - non decreasing, as you traverse array[i]<= array[i+1]
// T O(n)

const checkMonotonic = function (array){
    const first = array[0];
    const last = array[array.length-1];

    if (first === last){
        for (let i = 0; i < array.length-1; i++){
            if (array[i+1] !== array[i]) return false;
        }
    }
    else if (first < last){
        //non decreasing
        for (let i = 0; i < array.length-1; i++){
            if (array[i+i] < array[i]) return false;
        }
    }
    else {
        //non increasing
        for (let i = 0; i < array.length-1; i++){
            if (array[i+i] > array[i]) return false;
        }
    }
    return true;
}

console.log(checkMonotonic([1,2,3]));
console.log(checkMonotonic([3,2,1]));
console.log(checkMonotonic([1,3,2,5]));
console.log(checkMonotonic([3,3,3,3]));
console.log(checkMonotonic([9,7,8,5,6]));
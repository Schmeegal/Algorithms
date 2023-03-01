//brute force solution - not ideal (T O(nlogn) - O(n) for interation and O(logn) for sort function, S O(n))
/*
function sortedSquared(array){
    const newArray = new Array(array.length).fill(0);
    for(let i=0; i<array.length; i++){
        newArray[i] = Math.pow(array[i],2); //for each element, square and add to new array
    }
    newArray.sort(function(a,b){return a-b});  //if a-b is negative, it will put a ahead of b
    return newArray;
}
*/

//binary search and sort - T,S both O(n)
function sortedSquaredArray(array){
    const newArray = new Array(array.length).fill(0);
    let pointLeft = 0
    let pointRight = array.length-1;
    for (let i = array.length-1; i >= 0; i--){
        const leftSquared = Math.pow(array[pointLeft], 2);
        const rightSquared = Math.pow(array[pointRight], 2);
        if (leftSquared > rightSquared){
            newArray[i] = leftSquared;
            pointLeft++;
        } else {
            newArray[i] = rightSquared;
            pointRight--;
        }
    }
    return newArray;
}




let a = [1, 3, 4, 5];
let b = [4, 0, -3, -2, 7];
let c = [];
/*
console.log(sortedSquared(a));
console.log(sortedSquared(b));
console.log(sortedSquared(c));
*/

console.log(sortedSquaredArray(a));
console.log(sortedSquaredArray(b));
console.log(sortedSquaredArray(c));
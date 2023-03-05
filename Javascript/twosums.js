/*brute force T O(n^2), S O(1)

function findIdiciesSums(array, targetValue){
    for(let i = 0; i<array.length-1; i++){
        for (let j=i+1; j<array.length; j++){
            if (targetValue === array[i]+array[j]){
                return [i, j];
            }
        }
    }
    return [];
}

array = [1,2,3,4,5];
targetValue = 6;
console.log(findIdiciesSums(array,targetValue));
*/

//using hash table T O(n), S O(n)

function findIdiciesSums(array, targetValue){
    const hashTable = {};
    let neededValue;
    for (let i=0; i<array.length; i++){
        neededValue = targetValue - array[i];
        if (neededValue in hashTable){
            return [i, hashTable[neededValue]];
        }else{
            hashTable[array[i]] = i;
        }
    }
    return [];
}

array = [1,2,3,4,5]
targetValue = 6
console.log(findIdiciesSums(array, targetValue))
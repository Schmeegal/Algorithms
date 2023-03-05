/*brute force method checks every possibility and compare to max_area value
i is array value (y-axis), j is index position (x-axis)
T O(n^2) and S O(1)

container = [3,7,5,6,8,4]

const maxAreaBruteForce = function(array){
    let area = 0;
    for (let i = 0; i < array.length-1; i++){
        for (let j=i+1; j < array.length; j++){
            const height = Math.min(array[i], array[j]);
            const width = (j-i);
            area = Math.max(area, height*width);
        }
    }
    return area;
}

console.log(maxAreaBruteForce(container))
*/


//use pointer method starting at edges (starting with max width: last-first)
// S O(1), T O(n) (touch each element 1 time)
array = [3,7,5,6,8,4] 

const maxArea = function(array){
    let area = 0;
    let i = 0;
    let j = array.length-1;
    while (i<j){
        let height = Math.min(array[i], array[j]);
        let newArea = height*(j-1);
        area = Math.max(area,newArea);
        if (array[i] < array[j]) i++;
        else j--;

    }
    return area
}

console.log(maxArea(array))
//recursion method - T O(2^n), S O(n)
/*
const fibonacci = function(n){
    if (n <= 1) return n;
    else return fibonacci(n-1) + fibonacci(n-2)

}

console.log(fibonacci(8))
*/

//memoization - store values so you don't have to recompute them
//this will improve T Big O of recursion
//T O(n), S O(n)
const fibonacci = function(n){
    const ht = {0:0, 1:1};
    if (n in ht) return ht[n];
    else {
        ht[n] = fibonacci(n-1) + fibonacci(n-2);
        return ht[n];
    }
}

console.log(fibonacci(0))
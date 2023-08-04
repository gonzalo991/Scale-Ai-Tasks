function binarySearchSorting(arr) {
    if (arr.length <= 1) {
        return arr;
    } else {
        let mid = Math.floor(arr.length / 2);
        let left = binarySearchSorting(arr.slice(0, mid));
        let right = binarySearchSorting(arr.slice(mid));
        return concatBinarySearchSorting(left, right);
    }
}

function concatBinarySearchSorting(left, right){
    let searchResults = [];
    while (left.length && right.length) {
        if (left[0] < right[0]) {
            searchResults.push(left.shift());
        } else {
            searchResults.push(right.shift());
        }
    }

    return searchResults.concat(left.slice()).concat(right.slice());
}

function recursiveBinarySearch(arr, val, start = 0, end = arr.length - 1) {
    if (start > end) {
        return -1;
    }

    const mid = Math.floor((start + end) / 2);

    if (arr[mid] === val) {
        return mid;
    } else if (arr[mid] < val) {
        return recursiveBinarySearch(arr, val, mid + 1, end);
    } else {
        return recursiveBinarySearch(arr, val, start, mid - 1);
    }
}

let arr = [64, 34, 25, 12, 22, 11, 90];
let sortedArr = recursiveBinarySearch(arr, 90);
console.log(sortedArr); // Output: [11, 12, 22, 25, 34, 64, 90]
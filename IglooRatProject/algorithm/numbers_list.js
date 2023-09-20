/*
const nums = [-3, -8, -5, -10, 12, 3, 5, 7, 4, -9, 2, 6, 9, 4.5];
const total = nums.reduce((acc, val) => acc + val, 0);
const avg = total / nums.length;
const max = Math.max(...nums);
console.log(`The average value is: ${avg}`);
console.log(`The maximum value is: ${max}`);
*/

const nums = [12.5, 3.14159, 5.0, 7.0, 4.0, 1.0, 8.6, 2.0, 6.0, 9.5, 4.5, 5.6, 7.8, 11.65];

let total = 0;
let max = Number.NEGATIVE_INFINITY;

for (let i = 0; i < nums.length; i++) {
    total += nums[i];
    if (nums[i] > max) {
        max = nums[i];
    }
}

const avg = total / nums.length;

console.log(`The average value is: ${avg}`);
console.log(`The maximum value is: ${max}`);

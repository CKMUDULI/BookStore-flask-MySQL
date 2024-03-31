// function isNumeric(str) {
//     // Check if parsing as a number results in a number and is not NaN
//     return !isNaN(parseInt(str));
// }

// list = ["mb-3","3","btn"];

// console.log()

function filterFNumberStrings(stringArray) {
    return stringArray.filter(str => /^f\d+$/.test(str));
}

// Example usage
const stringArray = ["apple", "gf123", "banana", "f456", "cherry"];
const filteredStrings = filterFNumberStrings(stringArray);
console.log(filteredStrings); // Output: ["f123", "f456"]

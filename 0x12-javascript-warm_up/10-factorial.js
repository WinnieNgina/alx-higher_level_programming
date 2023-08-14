#!/usr/bin/node
function factorial (num) {
  if (isNaN(num)) {
    return (1);
  } else {
    if (num === 0 || num === 1) {
      return (1);
    } else {
      return (num * factorial(num - 1));
    }
  }
}
const a = parseInt(process.argv[2], 10);
console.log(factorial(a));

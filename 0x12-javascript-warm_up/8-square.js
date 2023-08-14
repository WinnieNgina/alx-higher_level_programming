#!/usr/bin/node
const num = parseInt(process.argv[2], 10); // returns NaN
if (isNaN(num)) {
  console.log('Missing number of occurrences');
} else {
  if (num > 0) {
    for (let i = 0; i < num; i++) {
      let row = '';
      for (let j = 0; j < num; j++) {
        row += 'X';
      }
      console.log(row);
    }
  }
}

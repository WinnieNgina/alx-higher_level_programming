#!/usr/bin/node
const num = parseInt(process.argv[2], 10); // returns NaN
if (isNaN(num)) {
  console.log('Missing number of occurrences');
} else {
  if (num > 0) {
    for (let i = 0; i < num; i++) {
      for (let j = 0; j < num; j++) {
        process.stdout.write('X');
      }
      process.stdout.write('\n');
    }
  }
}

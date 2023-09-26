#!/usr/bin/node
const fs = require('fs');
const args = process.argv;
const filePath = args[2];
fs.readFile(filePath, 'utf8', (error, data) => {
  if (error) {
    console.error(error);
    return;
  }
  console.log(data);
});

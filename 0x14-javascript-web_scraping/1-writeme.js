#!/usr/bin/node
const fs = require('fs');
const args = process.argv;
const filePath = args[2];
const data = args[3];
fs.writeFile(filePath, data, 'utf8', (error) => {
  if (error) {
    console.error(error);
  }
});

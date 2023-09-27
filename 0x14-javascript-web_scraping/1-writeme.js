#!/usr/bin/node

const fs = require('fs');
const args = process.argv;
const filePath = args[2];
const message = process.argv[3];

fs.writeFile(filePath, message, 'utf-8', error => {
  if (error) {
    console.log(error);
  }
});

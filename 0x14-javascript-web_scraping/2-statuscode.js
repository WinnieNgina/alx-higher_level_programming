#!/usr/bin/node
const request = require('request');
const args = process.argv;
const url = args[2];
request.get(url, (error, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('code: ', response && response.statusCode);
  }
});

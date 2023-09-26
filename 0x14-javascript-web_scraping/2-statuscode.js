#!/usr/bin/node
const request = require('request');
const args = process.argv;
const url = args[2];
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    console.log('Code:', response.statusCode);
  }
});

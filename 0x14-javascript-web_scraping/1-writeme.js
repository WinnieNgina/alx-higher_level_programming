#!/usr/bin/node
const request = require('request');
const args = process.argv;
const id = args[2];
const options = {
  method: 'GET',
  url: 'https://swapi-api.alx-tools.com/api/films/:id',
  headers: {
  }
};
request(options, function (error, response) {
  if (error) throw new Error(error);
  console.log(response.body);
});

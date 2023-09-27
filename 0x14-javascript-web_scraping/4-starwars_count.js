#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const films = JSON.parse(body).results;
    const moviesWithWedge = films.reduce((count, movie) => {
      return movie.characters.find((character) => character.endsWith('/18/'))
        ? count + 1 // if found
        : count; // if not found
    }, 0); // initiliazing count to zero
    console.log(moviesWithWedge);
  }
});

#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(body);
    for (const characterUrl of data.characters) {
      request(characterUrl, (error, response, body) => {
        if (error) {
          console.error(error);
        } else {
          const characterData = JSON.parse(body);
          let hasWedge = 0;
          for (const key in characterData) {
            if (characterData[key].name === 'Wedge Antilles') {
              hasWedge += 1;
            }
          }
          console.log(hasWedge);
        }
      });
    }
  }
});

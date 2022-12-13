#!/usr/bin/node
/*
  script that prints the number of movies where the character “Wedge Antilles
 */

const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const films = JSON.parse(body).results;
    let counter = 0;
    for (const film in films) {
      const person = films[film].characters;
      for (const id in person) {
        if (person[id].includes('18')) {
          counter++;
        }
      }
    }
    console.log(counter);
  } else {
    console.log('Error Code:' + response.statusCode);
  }
});

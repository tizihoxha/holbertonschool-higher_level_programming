#!/usr/bin/node
/*
 script that prints the title of a Star Wars movie where the episode number matches a given integer
 */

const request = require('request');
const endpoint = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request.get(endpoint, function (error, response, body) {
  if (error) throw error;
  console.log(JSON.parse(body).title);
});

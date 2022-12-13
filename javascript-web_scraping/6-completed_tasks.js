#!/usr/bin/node
/*
  script that prints the number of movies where the character “Wedge Antilles
 */

const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const dict = {};
    const tasks = JSON.parse(body);
    for (const nr in tasks) {
      if (tasks[nr].completed) {
        if (dict[tasks[nr].userId] === undefined) {
          dict[tasks[nr].userId] = 1;
        } else {
          dict[tasks[nr].userId]++;
        }
      }
    }
    console.log(dict);
  } else {
    console.log('Error code: ' + response.statusCode);
  }
});

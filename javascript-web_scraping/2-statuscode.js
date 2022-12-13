#!/usr/bin/node
/*
 script that display the status code of a GET request
 */

const request = require('request');

request.get(process.argv[2], function (error, response, body) {
  if (!error && response.statusCode === 200) {
    console.log('code:', response.statusCode);
  }
});

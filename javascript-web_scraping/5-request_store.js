#!/usr/bin/node
/*
 script that gets the contents of a webpage and stores it in a file
 */

const fs = require('fs');
const request = require('request');
request.get(process.argv[2], function (error, response, body) {
  if (error) throw error;
  fs.writeFile(process.argv[3], 'utf8', body);
});

#!/usr/bin/node
/*
 Write a script that writes a string to a file
 */

const fs = require('fs');

fs.writeFile(process.argv[2], process.argv[3], function (error) {
  if (error) throw error;
});

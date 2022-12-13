#!/usr/bin/node
/*
 Write a script that reads and prints the content of a file
 */

const fs = require('fs');

fs.readFile(process.argv[2], 'utf8', function(error, data) {
	if (error) throw error;
	console.log(data);
});
